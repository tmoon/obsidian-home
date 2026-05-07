"""
SignalPilot Receipt Protocol — dbt Verifier (reference spec)

DRAFT v0 — 2026-05-07
Lifts the 7-check post-build verifier from `benchmark/prompts/dbt_verify_subagent.md`
into a deterministic Python module that emits structured Receipts.

This is a SPEC, not production code. The product-repo implementation will refine
types, add error handling, optimize, and add tests. Treat this as the reference
contract for what the module must accept, do, and return.

Companion to: wiki/concepts/receipt-product-features-spec.md
                wiki/concepts/receipt-as-primitive.md
"""

from __future__ import annotations

from dataclasses import dataclass
from datetime import datetime, timezone
from enum import Enum
from pathlib import Path
from typing import Literal, Optional, Protocol


# ─────────────────────────────────────────────────────────────────────────────
# Enums + simple types
# ─────────────────────────────────────────────────────────────────────────────


class CheckStatus(str, Enum):
    PASS = "pass"
    WARN = "warn"
    FAIL = "fail"
    SKIP = "skip"  # per dbt prompt: "skip rather than fabricate when no reference exists"


class Decision(str, Enum):
    MERGE_OK = "MERGE_OK"
    MERGE_WARN = "MERGE_WARN"
    MERGE_BLOCKED = "MERGE_BLOCKED"
    MERGE_OVERRIDDEN = "MERGE_OVERRIDDEN"


class FixClass(str, Enum):
    """Bounded fix authority — per the dbt verifier prompt's "do no harm" preamble.
    Verifier may auto-attempt fixes in `policy.auto_fix.allowed`; never others."""

    MISSING_CAST = "missing_cast"
    MISSING_CTE = "missing_cte"
    DATE_SPINE_ERROR = "date_spine_error"
    # Forbidden (NEVER auto-fix even if asked):
    # JOIN_TYPE_CHANGE, ADD_NULL_FILTER, REMOVE_COALESCE, REWRITE_USER_SQL


# ─────────────────────────────────────────────────────────────────────────────
# Policy (loaded from YAML bundle, validated)
# ─────────────────────────────────────────────────────────────────────────────


@dataclass(frozen=True)
class CheckSpec:
    """One check declaration in the policy. Mirrors the YAML `checks:` entry."""

    id: str
    required: bool = True
    # Per-check optional config; ignored by checks that don't use it.
    strict_types: Optional[bool] = None  # column_schema_alignment
    reference: Optional[Literal["snapshot"]] = None  # row_count
    tolerance_pct: Optional[float] = None  # row_count
    sample_size: Optional[int] = None  # value_spot_check
    tolerance_numeric: Optional[float] = None  # value_spot_check
    flag: Optional[list[str]] = None  # cardinality_audit


@dataclass(frozen=True)
class PreflightSpec:
    ddl_block: bool = True
    function_denylist: tuple[str, ...] = ()
    limit_inject_default: int = 10_000
    budget_max_rows_scanned: float = 1e9
    budget_max_dollars: float = 5.0
    pii_redaction_fields: tuple[str, ...] = ()


@dataclass(frozen=True)
class OnFailureSpec:
    required_check_failed: Literal["block_save", "post_warning", "hard_refuse"] = (
        "block_save"
    )
    warn_check_failed: Literal["block_save", "post_warning"] = "post_warning"
    budget_exceeded: Literal["block_save", "hard_refuse"] = "hard_refuse"


@dataclass(frozen=True)
class OverrideSpec:
    required_role: Optional[str] = None  # e.g., "data-eng-lead"
    rollback_playbook: Literal["required", "optional", "none"] = "required"
    audit_log_entry: bool = True


@dataclass(frozen=True)
class AutoFixSpec:
    allowed: tuple[FixClass, ...] = ()
    # forbidden is documented in spec but not enforced here — bounded by `allowed`.


@dataclass(frozen=True)
class Policy:
    """The contract. Loaded from YAML, validated, hashed for receipts."""

    id: str  # e.g., "production-strict"
    version: str  # e.g., "1.2"
    applies_to_models: tuple[str, ...]  # e.g., ("marts/**", "intermediate/**")
    applies_to_excludes: tuple[str, ...] = ()
    preflight: PreflightSpec = PreflightSpec()
    checks: tuple[CheckSpec, ...] = ()
    on_failure: OnFailureSpec = OnFailureSpec()
    override: OverrideSpec = OverrideSpec()
    auto_fix: AutoFixSpec = AutoFixSpec()

    @property
    def policy_hash(self) -> str:
        """Stable hash of the policy content. Receipt cites this hash so a
        receipt can be replayed against the exact policy version that produced it."""
        ...  # TODO: deterministic hash over canonical-form fields

    @classmethod
    def from_yaml(cls, path: Path) -> "Policy":
        """Load a bundle YAML file (e.g., spec/policy_bundles/production-strict.yaml)."""
        ...  # TODO: pyyaml + Pydantic validation


# ─────────────────────────────────────────────────────────────────────────────
# Change manifest + reference snapshot (vendor-neutral)
# ─────────────────────────────────────────────────────────────────────────────


@dataclass(frozen=True)
class ModelRef:
    """Vendor-neutral reference to a dbt model (or analogous)."""

    name: str
    materialization: Literal["table", "view", "incremental", "ephemeral"]
    schema: Optional[str] = None
    file_path: Optional[Path] = None


@dataclass(frozen=True)
class ChangeManifest:
    """What this PR / change actually touches. Adapter produces this."""

    pr_url: Optional[str]
    diff_hash: str  # sha256 of unified diff
    branch: str
    models_added: tuple[ModelRef, ...] = ()
    models_modified: tuple[ModelRef, ...] = ()
    models_removed: tuple[ModelRef, ...] = ()
    files_changed: tuple[Path, ...] = ()


@dataclass(frozen=True)
class Snapshot:
    """Reference snapshot — pre-build state captured for ground-truth diffing.
    Per the dbt verifier prompt: 'reference snapshot is source of truth, not
    prompt or comments.' Adapter is responsible for materializing this in a
    portable format (Parquet)."""

    snapshot_id: str
    captured_at: datetime
    # Implementation-specific; adapter provides query interface.


# ─────────────────────────────────────────────────────────────────────────────
# Check results + audit log linking
# ─────────────────────────────────────────────────────────────────────────────


@dataclass(frozen=True)
class AuditLogRef:
    """Pointer back to a gateway audit log entry. Closes the loop between
    governance and verifier — every check evidence references the tool calls
    that produced it."""

    log_id: str
    tool_name: str  # e.g., "list_tables", "check_model_schema"
    invoked_at: datetime


@dataclass(frozen=True)
class Evidence:
    """The proof the check looked at. Strongly typed per check kind in real
    implementation; here we keep flexible. CRITICAL: must reference audit_log
    entries — that's what makes receipts replayable + auditable."""

    summary: str
    audit_log_refs: tuple[AuditLogRef, ...]
    detail: dict  # check-specific structured data (schema diffs, row counts, samples)


@dataclass(frozen=True)
class CheckResult:
    """Output of one check. Goes directly into the Receipt."""

    check_id: str  # e.g., "value_spot_check"
    status: CheckStatus
    required: bool  # was this required by the policy?
    evidence: Evidence
    suggested_fix: Optional["FixSuggestion"] = None
    blocking_reason: Optional[str] = None  # populated only if status=FAIL and policy blocks


@dataclass(frozen=True)
class FixSuggestion:
    """When a check fails, the verifier may suggest a fix.
    Tier 1 (auto-fix): if fix_class in policy.auto_fix.allowed, can be applied.
    Tier 2 (delegate): otherwise, forms the context for opening Claude Code."""

    fix_class: FixClass
    description: str  # human-readable
    proposed_diff: Optional[str] = None  # unified diff if auto-fixable
    auto_applicable: bool = False  # only true if fix_class in policy.auto_fix.allowed


# ─────────────────────────────────────────────────────────────────────────────
# Score (rules-v0; AutoFyn-Bayesian replaces this in Q4 2026)
# ─────────────────────────────────────────────────────────────────────────────


@dataclass(frozen=True)
class ScoreFactor:
    name: str
    delta: int  # contribution to the 0..100 score (positive or negative)
    note: Optional[str] = None


@dataclass(frozen=True)
class Score:
    value: int  # 0..100
    method: Literal["rules_v0", "autofyn_v1", "autofyn_v2_with_transfer"] = "rules_v0"
    policy_strictness: str = ""
    factors: tuple[ScoreFactor, ...] = ()


def compute_score_v0(
    *,
    checks: tuple[CheckResult, ...],
    policy: Policy,
    customer_history: Optional["CustomerHistory"] = None,
    blast_radius_count: int = 0,
    test_coverage_pct: float = 0.0,
    change_lines: int = 0,
) -> Score:
    """Deterministic rules-v0 score. Per spec: every factor in factors[],
    explainable, customer-history-aware after 30d.

    Calibration target: Score 90 → 90% no-incident in 30d at this customer
    (or fleet baseline if customer < 30d tenure)."""

    factors: list[ScoreFactor] = []

    factors.append(ScoreFactor("baseline", 100))

    # Required check failures / warnings
    fail_count = sum(1 for c in checks if c.status == CheckStatus.FAIL and c.required)
    warn_count = sum(1 for c in checks if c.status == CheckStatus.WARN and c.required)
    if fail_count:
        factors.append(
            ScoreFactor("required_check_failures", -12 * fail_count, f"{fail_count} required checks failed")
        )
    if warn_count:
        factors.append(
            ScoreFactor("required_check_warnings", -4 * warn_count, f"{warn_count} required checks warned")
        )

    # Risk modifiers
    if blast_radius_count > 0:
        # 0..6 penalty; saturating at 30+ downstream
        delta = -min(6, max(0, (blast_radius_count - 2) // 2))
        factors.append(ScoreFactor("blast_radius", delta, f"{blast_radius_count} downstream"))

    if change_lines > 100:
        delta = -min(4, (change_lines - 100) // 200)
        factors.append(ScoreFactor("change_magnitude", delta, f"{change_lines} lines changed"))

    if test_coverage_pct >= 0.6:
        factors.append(ScoreFactor("test_coverage", +3, f"{int(test_coverage_pct*100)}%"))

    # Customer history (only after sufficient tenure)
    if customer_history and customer_history.tenure_days >= 30:
        factors.extend(customer_history.score_factors())

    # Policy strictness offset (most are 0; dev-permissive adds +5)
    factors.append(ScoreFactor("policy_strictness", policy_strictness_modifier(policy.id)))

    raw = sum(f.delta for f in factors)
    value = max(0, min(100, raw))

    return Score(
        value=value,
        method="rules_v0",
        policy_strictness=policy.id,
        factors=tuple(factors),
    )


def policy_strictness_modifier(policy_id: str) -> int:
    return {
        "production-strict": 0,
        "dev-permissive": +5,
        "ci-gate": 0,
        "audit-trail-only": 0,
    }.get(policy_id, 0)


@dataclass(frozen=True)
class CustomerHistory:
    """Per-customer history feeding score factors. Q3 2026: stub. Q4 2026:
    AutoFyn-derived (Bayesian per-customer prior)."""

    tenure_days: int
    recent_pass_rate: float = 0.0  # last 30d
    recent_incident_rate: float = 0.0  # last 30d

    def score_factors(self) -> list[ScoreFactor]:
        factors: list[ScoreFactor] = []
        if self.recent_pass_rate >= 0.95:
            factors.append(ScoreFactor("recent_pass_rate", +5, f"{int(self.recent_pass_rate*100)}% recent"))
        if self.recent_incident_rate > 0:
            penalty = -min(8, int(self.recent_incident_rate * 100))
            factors.append(
                ScoreFactor("recent_incident_rate", penalty, f"{self.recent_incident_rate:.1%} 30d")
            )
        return factors


# ─────────────────────────────────────────────────────────────────────────────
# Receipt — the artifact (this is what gets emitted, signed, posted to PR)
# ─────────────────────────────────────────────────────────────────────────────


@dataclass(frozen=True)
class Action:
    """A clickable action exposed in the PR comment."""

    id: str
    label: str
    kind: Literal["user_action", "rerun", "delegate", "apply_fix", "override"]
    endpoint: Optional[str] = None  # URL, claude:// scheme, or internal endpoint


@dataclass(frozen=True)
class Receipt:
    """The artifact. Cryptographically signed in production; v0 emits unsigned."""

    receipt_version: Literal["signalpilot.receipt/v1"]
    receipt_id: str  # ULID, content-derived
    created_at: datetime

    context: ChangeManifest
    policy: Policy
    preflight: dict  # gateway evidence; structured in real impl
    checks: tuple[CheckResult, ...]
    score: Score
    decision: Decision
    actions: tuple[Action, ...]
    audit_log_first: str
    audit_log_last: str
    audit_log_count: int

    signature: Optional[dict] = None  # {alg, key_id, value, signed_at} when signing on


# ─────────────────────────────────────────────────────────────────────────────
# WarehouseAdapter contract — the vendor-neutrality boundary
# ─────────────────────────────────────────────────────────────────────────────


class WarehouseAdapter(Protocol):
    """All adapters implement this. Receipt protocol code never imports
    vendor-specific modules. Adapter abstraction is the entire reason
    we can expand DuckDB → Snowflake → Databricks → BigQuery without
    changing receipt format / score formula / policy schema."""

    def parse_change(self, diff_unified: str) -> ChangeManifest:
        """Extract what changed (vendor-aware: dbt manifest parse, dialect)."""
        ...

    def reference_snapshot(self, models: tuple[str, ...]) -> Snapshot:
        """Capture pre-state for ground-truth diffing."""
        ...

    def run_checks(
        self, policy: Policy, change: ChangeManifest, snapshot: Snapshot
    ) -> tuple[CheckResult, ...]:
        """Execute the policy's required checks. Returns CheckResult tuple
        in protocol-standard format (independent of warehouse)."""
        ...

    def attempt_fix(
        self, check: CheckResult, fix: FixSuggestion
    ) -> Optional[str]:
        """Bounded auto-fix per warehouse. Returns unified diff if fix
        succeeded, None if can't safely auto-apply. Only invoked if
        fix.fix_class in policy.auto_fix.allowed."""
        ...

    def cost_estimate(self, change: ChangeManifest) -> tuple[int, float]:
        """Returns (rows_to_scan, dollars). Used for preflight budget check."""
        ...


# ─────────────────────────────────────────────────────────────────────────────
# The verifier orchestrator — the entry point
# ─────────────────────────────────────────────────────────────────────────────


def run_verifier(
    *,
    adapter: WarehouseAdapter,
    policy: Policy,
    diff_unified: str,
    customer_history: Optional[CustomerHistory] = None,
) -> Receipt:
    """The main entry point. Replaces the prompt-based verifier with
    deterministic Python code that produces a Receipt artifact.

    Flow:
    1. Adapter parses the change
    2. Adapter captures reference snapshot
    3. Preflight gateway checks (DDL block, budget, etc.)
    4. Adapter runs the policy's checks
    5. Score is computed deterministically from check results + factors
    6. Decision is derived mechanically from policy + score + check failures
    7. Actions are populated (one-click in PR)
    8. Receipt is built, signed (if enabled), returned

    The orchestrator is vendor-neutral. Vendor specifics live in the adapter."""

    change = adapter.parse_change(diff_unified)
    snapshot = adapter.reference_snapshot(
        models=tuple(m.name for m in change.models_added + change.models_modified)
    )

    # Preflight (gateway-side)
    preflight_evidence = _run_preflight(adapter=adapter, policy=policy, change=change)
    if preflight_evidence.get("status") == "hard_refuse":
        # No verification possible — gateway refuses outright
        return _build_refused_receipt(policy=policy, change=change, preflight=preflight_evidence)

    # Verification (post-build / post-action)
    checks = adapter.run_checks(policy=policy, change=change, snapshot=snapshot)

    # Score
    score = compute_score_v0(
        checks=checks,
        policy=policy,
        customer_history=customer_history,
        blast_radius_count=_blast_radius(adapter, change),
        test_coverage_pct=_test_coverage(adapter, change),
        change_lines=_lines_changed(change),
    )

    # Decision (mechanical from policy + checks + score)
    decision = _derive_decision(policy=policy, checks=checks, score=score)

    # Actions
    actions = _build_actions(policy=policy, decision=decision, checks=checks)

    return Receipt(
        receipt_version="signalpilot.receipt/v1",
        receipt_id=_generate_receipt_id(change=change),
        created_at=datetime.now(timezone.utc),
        context=change,
        policy=policy,
        preflight=preflight_evidence,
        checks=checks,
        score=score,
        decision=decision,
        actions=actions,
        audit_log_first="",  # filled by audit-log subsystem
        audit_log_last="",
        audit_log_count=0,
        signature=None,
    )


# ─────────────────────────────────────────────────────────────────────────────
# Internal helpers (sketch only)
# ─────────────────────────────────────────────────────────────────────────────


def _run_preflight(adapter: WarehouseAdapter, policy: Policy, change: ChangeManifest) -> dict:
    """Gateway-side: AST parsing, DDL block, LIMIT inject, budget cap, PII."""
    ...


def _build_refused_receipt(policy: Policy, change: ChangeManifest, preflight: dict) -> Receipt:
    """Receipt for the case where preflight refused outright (e.g., budget cap exceeded)."""
    ...


def _blast_radius(adapter: WarehouseAdapter, change: ChangeManifest) -> int:
    """Count downstream models / dashboards that reference the changed models."""
    ...


def _test_coverage(adapter: WarehouseAdapter, change: ChangeManifest) -> float:
    """Fraction of changed lines / models with associated tests."""
    ...


def _lines_changed(change: ChangeManifest) -> int:
    """Total lines in the unified diff."""
    ...


def _derive_decision(policy: Policy, checks: tuple[CheckResult, ...], score: Score) -> Decision:
    """Mechanical from policy.on_failure + checks + score.
    No editorial judgment — same inputs → same decision."""
    has_required_fail = any(c.status == CheckStatus.FAIL and c.required for c in checks)
    if has_required_fail and policy.on_failure.required_check_failed == "block_save":
        return Decision.MERGE_BLOCKED
    has_warn = any(c.status == CheckStatus.WARN for c in checks)
    if has_warn:
        return Decision.MERGE_WARN
    return Decision.MERGE_OK


def _build_actions(policy: Policy, decision: Decision, checks: tuple[CheckResult, ...]) -> tuple[Action, ...]:
    """Populate the action panel: rerun, delegate-to-Claude, apply-fix, override."""
    actions: list[Action] = [
        Action(id="rerun_verification", label="Re-run verification", kind="rerun"),
        Action(id="open_in_claude_code", label="Open in Claude Code with context", kind="delegate"),
    ]
    if decision == Decision.MERGE_OK:
        actions.insert(0, Action(id="approve_merge", label="Approve & merge", kind="user_action"))
    if decision == Decision.MERGE_BLOCKED:
        # One-click auto-fix per failed check IF fix is in policy.auto_fix.allowed
        for c in checks:
            if c.status == CheckStatus.FAIL and c.suggested_fix and c.suggested_fix.auto_applicable:
                actions.insert(0, Action(
                    id=f"apply_fix_{c.check_id}",
                    label=f"Apply fix: {c.suggested_fix.description}",
                    kind="apply_fix",
                ))
        # Override flow
        if policy.override.required_role:
            actions.append(Action(
                id="override",
                label=f"Override (requires {policy.override.required_role})",
                kind="override",
            ))
    return tuple(actions)


def _generate_receipt_id(change: ChangeManifest) -> str:
    """ULID, content-addressed by diff_hash + timestamp. Tamper-evident."""
    ...
