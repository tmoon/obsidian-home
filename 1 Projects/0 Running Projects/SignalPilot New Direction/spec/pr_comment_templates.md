# PR Comment Renderer Templates — SignalPilot Receipt

Markdown templates the GitHub App uses to render Receipts as PR comments. Three states (PASS / WARN / BLOCK) + one consolidated short-form variant for re-runs and updates.

Variables in `{{ }}` are substituted by the renderer from the JSON Receipt fields. See `receipt_v1_schema.json` for the data contract.

---

## Template 1 — PASS (MERGE_OK, Score >= configured threshold)

```markdown
## 🟢 SignalPilot Receipt — Score {{ score.value }}/100

| | |
|---|---|
| **Decision** | ✅ `MERGE_OK` |
| **Policy** | `{{ policy.id }}` v{{ policy.version }} |
| **Models** | {{ context.models_touched | join: ", " }} |
| **Receipt** | [`{{ receipt_id }}`]({{ links.html_view }}) |

### Verification ({{ checks_passed_count }}/{{ checks_required_count }} required passed)

{% for check in checks %}
- {{ status_emoji(check.status) }} **{{ check.id }}** — {{ check.evidence.summary }}
{% endfor %}

### Score factors

```
{% for factor in score.factors %}
{{ factor.delta | sign_pad }}  {{ factor.name | pad: 28 }}  {{ factor.note }}
{% endfor %}
                                ─────
                                  = {{ score.value }}
```

<details>
<summary>Pre-flight (gateway)</summary>

- DDL block: {{ preflight.ddl_block }}
- Limit injection: {{ preflight.limit_inject }}
- Budget: {{ preflight.budget.rows_scanned | format_si }} rows of {{ preflight.budget.limit | format_si }} ({{ preflight.budget.percent }}%)
- PII redaction: {{ preflight.pii_redaction }}

</details>

---

[ ✅ Approve & merge ]({{ action_url("approve_merge") }}) &nbsp;
[ 🔄 Re-run verification ]({{ action_url("rerun_verification") }}) &nbsp;
[ 🤖 Open in Claude Code ]({{ action_url("open_in_claude_code") }}) &nbsp;
[ 📋 Audit log ({{ audit_log_chain.log_count }} entries) ]({{ links.audit_log_url }})

<sub>SignalPilot v{{ version }} — `{{ policy.id }}@{{ policy.version }}` — receipt verified at {{ created_at | format_iso }}</sub>
```

---

## Template 2 — WARN (MERGE_WARN, non-required check warnings)

```markdown
## 🟡 SignalPilot Receipt — Score {{ score.value }}/100

| | |
|---|---|
| **Decision** | ⚠️ `MERGE_WARN` — review before merge |
| **Policy** | `{{ policy.id }}` v{{ policy.version }} |
| **Models** | {{ context.models_touched | join: ", " }} |
| **Receipt** | [`{{ receipt_id }}`]({{ links.html_view }}) |

### Verification ({{ checks_passed_count }}/{{ checks_required_count }} required passed, {{ checks_warned_count }} warnings)

{% for check in checks %}
- {{ status_emoji(check.status) }} **{{ check.id }}**
{% if check.status == "warn" %}
  > {{ check.evidence.summary }}
{% else %}
  — {{ check.evidence.summary }}
{% endif %}
{% endfor %}

### Score factors

```
{% for factor in score.factors %}
{{ factor.delta | sign_pad }}  {{ factor.name | pad: 28 }}  {{ factor.note }}
{% endfor %}
                                ─────
                                  = {{ score.value }}
```

---

[ ✅ Approve & merge ]({{ action_url("approve_merge") }}) &nbsp;
[ 🔄 Re-run verification ]({{ action_url("rerun_verification") }}) &nbsp;
[ 🤖 Open in Claude Code with context ]({{ action_url("open_in_claude_code") }})

<sub>SignalPilot v{{ version }} — `{{ policy.id }}@{{ policy.version }}` — warnings do not block merge under this policy</sub>
```

---

## Template 3 — BLOCK (MERGE_BLOCKED, required check failure or blast-radius cap)

```markdown
## 🔴 SignalPilot Receipt — Score {{ score.value }}/100

| | |
|---|---|
| **Decision** | ❌ `MERGE_BLOCKED` — {{ failure_count }} required {{ failure_count | pluralize: "check" }} failed |
| **Policy** | `{{ policy.id }}` v{{ policy.version }} |
| **Models** | {{ context.models_touched | join: ", " }} ({{ blast_radius_count }} downstream) |
| **Receipt** | [`{{ receipt_id }}`]({{ links.html_view }}) |

### Verification ({{ checks_passed_count }}/{{ checks_required_count }} required passed)

{% for check in checks %}
{% if check.status == "fail" and check.required %}
- ❌ **{{ check.id }}** — `BLOCK`
  > {{ check.evidence.summary }}
  >
{% if check.evidence.detail.affected_artifacts %}
  > **Affected:** {% for a in check.evidence.detail.affected_artifacts %}`{{ a }}`{% endfor %}
{% endif %}
{% if check.blocking_reason %}
  > **Reason:** {{ check.blocking_reason }}
{% endif %}
{% else %}
- {{ status_emoji(check.status) }} **{{ check.id }}** — {{ check.evidence.summary }}
{% endif %}
{% endfor %}

### Score factors

```
{% for factor in score.factors %}
{{ factor.delta | sign_pad }}  {{ factor.name | pad: 28 }}  {{ factor.note }}
{% endfor %}
                                ─────
                                  = {{ score.value }}
```

### Suggested fixes

{% for action in actions where kind in ["apply_fix", "delegate", "override"] %}
{% if action.kind == "apply_fix" %}
- 🔧 **Tier 1 (auto-fix):** [{{ action.label }}]({{ action_url(action.id) }})
  <sub>Will commit as a new commit by `signalpilot-bot`; verifier re-runs automatically</sub>
{% elif action.kind == "delegate" %}
- 🤖 **Tier 2 (delegate):** [{{ action.label }}]({{ action_url(action.id) }})
  <sub>Opens local Claude Code with full receipt + diff + suggested fix as context</sub>
{% elif action.kind == "override" %}
- 🚨 **Tier 3 (override):** [{{ action.label }}]({{ action_url(action.id) }})
  <sub>Requires `{{ policy.override.required_role }}` role token + auto-generated rollback playbook</sub>
{% endif %}
{% endfor %}

---

[ 🔄 Re-run verification ]({{ action_url("rerun_verification") }}) &nbsp;
[ 📋 Audit log ({{ audit_log_chain.log_count }} entries) ]({{ links.audit_log_url }})

<sub>SignalPilot v{{ version }} — `{{ policy.id }}@{{ policy.version }}` — under this policy, required-check failures block merge</sub>
```

---

## Template 4 — Short update (re-run / status change)

When a Receipt is re-emitted on the same PR (e.g., after auto-fix applied), edit the existing comment in place rather than posting a new one. Use this short-form for the most-recent-update area at top of the persistent comment:

```markdown
> **Updated {{ created_at | relative_time }}** — Score {{ score.value }} ({{ score_delta_signed }}) — Decision: {{ decision_emoji }} `{{ decision }}` — [{{ receipt_id }}]({{ links.html_view }})
```

The full Pass/Warn/Block body below it gets replaced with the latest receipt's full rendering.

---

## Helper functions (renderer responsibilities)

The renderer must implement:

| Helper | Purpose |
|---|---|
| `status_emoji(status)` | Maps `pass` → ✅, `warn` → ⚠️, `fail` → ❌, `skip` → ⏭️ |
| `sign_pad(delta)` | Right-aligned signed number, e.g., `+100`, ` -12`, ` -2`, `  0` |
| `pad(width)` | Left-pad string for column alignment |
| `format_si(num)` | `1200000` → `1.2×10⁶`, `1500000000` → `1.5×10⁹` |
| `format_iso(datetime)` | `2026-09-15 14:23 UTC` |
| `relative_time(datetime)` | `3 minutes ago`, `2 hours ago` |
| `action_url(action_id)` | Build the GitHub-app callback URL for an action |
| `pluralize(count, word)` | English-style pluralization |
| `join: ", "` | Liquid-style array join |

---

## CLI verification (companion to the PR comment)

Customers can also run the verifier locally with `signalpilot test`. The CLI output mirrors the PR comment but rendered for terminal:

```
$ signalpilot test --policy production-strict
🔴 SignalPilot Receipt — Score 64/100 — production-strict v1.2

VERIFICATION (5/7 — 2 BLOCKERS)
  ✅ models exist
  ❌ column schema misaligned           BLOCK
       3 dashboards reference customer_id (now user_id)
       affected: apps/exec_dashboard, apps/ops_health, embedded/customer_portal
  ⚠️ row count varies                  ±3.2%
  ✅ no fan-out detected
  ❌ blast radius exceeds policy        BLOCK
       14 models affected; production-strict caps at 8

SUGGESTED FIXES
  [1] Tier 1 auto-fix: add backfill alias column for customer_id → user_id
  [2] Tier 2 delegate: open in Claude Code with full receipt context
  [3] Tier 3 override: approve with rollback playbook (requires data-eng-lead)

Receipt: rcpt_01J5MQK2X3...   Audit log: 47 entries

Run `signalpilot apply 1` to apply auto-fix #1.
Run `signalpilot delegate 2` to open in Claude Code.
```

The CLI MUST emit the same JSON receipt to `.signalpilot/receipts/{receipt_id}.json` so it's bit-for-bit identical to what CI / GitHub App would post. **Same artifact, two surfaces.**

---

## A/B testing notes (per Pitch Ladder Experiment E11)

The PR comment UX is the most-tested artifact in our funnel. Things to A/B in early design-partner conversations:

| Variable | Variant A | Variant B | Hypothesis |
|---|---|---|---|
| Score factors visibility | always shown (current) | collapsed under details | A is more transparent; B reduces visual noise |
| Suggested fixes ordering | by tier (1→2→3) | by impact (highest first) | tier-ordering teaches the system; impact-ordering is faster to act on |
| Override link prominence | last in list | first in list | last = friction discourages override; first = honors urgency |
| Audit log link | bottom of comment | inline next to each check | bottom = clean comment; inline = traceability per check |

Don't ship A/B test infra in MLP — track manually via design-partner feedback. After 3 design partners, lock the version that converts best.
