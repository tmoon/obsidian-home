# spec/ — Reference implementation specs for The Receipt

> **Purpose:** buildable starting points for the engineering team. NOT production code. NOT canonical schemas (yet). These are *reference specs* that show the shape of what to build, derived from [[Receipt Product Features — Policy-as-Code, Action Loop, Honest Score, Vendor-Neutral Expansion]] (the strategic spec). When actual implementation begins, these become the seed; the canonical source moves to the SignalPilot product repo.
>
> **Why these live here (and not in the product repo yet):**
> - The product repo has its own structure, conventions, and review process; these specs are draft-form and would slow down review there
> - These specs are wiki-companions — they're meant to be edited together with the strategic concept page
> - When a customer or engineer asks "what does the policy schema actually look like?" we can point at one place
> - When implementation starts, we lift these into the product repo's chosen structure (likely under `signalpilot/spec/` or `signalpilot/policy/`) and apply real review

## Contents

| File | What it specifies | Used by |
|---|---|---|
| `dbt_verifier_protocol.py` | Python interface stubs lifting the 7-check verifier from `benchmark/prompts/dbt_verify_subagent.md` into a deterministic module that emits structured Receipts | Daniel / verifier engineer |
| `receipt_v1_schema.json` | JSON Schema (draft-07) for Receipt format v1 — strict enough to validate, loose enough to evolve | All consumers (gateway, GitHub App, CLI, customer integrations) |
| `policy_bundles/production-strict.yaml` | The opinionated default for prod environments — every check required, blocks on failure, override needs role token + rollback | Customers' day-1 default |
| `policy_bundles/dev-permissive.yaml` | The opinionated default for dev sandboxes — checks run as warnings, save proceeds | Customers' MVP onboarding default |
| `policy_bundles/ci-gate.yaml` | The opinionated default for CI/CD pipelines — required checks block merge, JSON receipt posted as PR comment | GitHub Action / CI integration |
| `policy_bundles/audit-trail-only.yaml` | All checks run, none block, full audit log emitted — for monitoring without enforcement | Observability-only customers |
| `pr_comment_templates.md` | Markdown templates for rendering Receipts as GitHub PR comments — pass case + block case + warning case | Luiz / GitHub App engineer |

## How to use these

**For engineers (Daniel / Luiz):** start from these stubs. Don't treat them as production-ready — refine, type, test, harden as you implement. Push refinements back here so the wiki spec stays consistent with what's actually shipping.

**For founders (Tarik) / GTM:** when explaining the product to a prospect, you can paste the JSON Schema and the production-strict YAML to make abstract claims concrete. *"Here is exactly what `production-strict` enforces. Here is exactly what a Receipt looks like. Pick a different bundle if you want different rules."*

**For investors:** when asked for technical detail beyond the strategic pitch, these specs ARE the answer. They demonstrate that "policy-as-code Receipt protocol" isn't hand-waving — it's structured, declared, signed, replayable.

## Status

| Spec | Status | Owner | Next action |
|---|---|---|---|
| dbt_verifier_protocol.py | Draft v0 | Daniel | Implement against existing 7-check prompt |
| receipt_v1_schema.json | Draft v0 | Daniel | Validate against 5 example receipts |
| policy_bundles/*.yaml | Draft v0 | Tarik to review wording, Daniel to validate against Python code | Loop with first design partner for one custom variant |
| pr_comment_templates.md | Draft v0 | Luiz | Implement renderer; A/B test pass-vs-block UX |

## Out of scope here

- Cryptographic signing implementation (Ed25519 key management, KMS integration) — Q4 2026 once first SOC2 customer asks
- sigstore / Rekor anchoring — Q1 2027 if EU AI Act enforcement creates demand
- Receipt-graph queryability (cross-receipt traversal) — Q1 2027 once a customer asks
- Multi-host MCP support beyond Claude Code — Q4 2026 (Cursor first)
- AutoFyn-Bayesian Score calibration replacing rules-v0 — Q4 2026 frozen-team test gate

These appear in the strategic spec but are deferred per [[Receipt-as-Primitive]] §"⚠ MLP SCOPE CUT."
