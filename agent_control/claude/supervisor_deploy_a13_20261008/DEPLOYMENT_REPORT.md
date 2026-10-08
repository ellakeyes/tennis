# CLAUDE HOST OPERATOR — SUPERVISOR DEPLOYMENT + A13 — DEPLOYMENT REPORT

TASK_ID = TENNIS-CLAUDE-HOST-SUPERVISOR-DEPLOY-A13-20261008
STATUS = BLOCKED_HOST_ACCESS
ROLE = HOST_OPERATOR
AGENT = CLAUDE
GENERATED_UTC = 2026-10-08T21:07:11Z
SOURCE_COMMIT = 4b93bb0ece81e4933b7e1649d9651e4fdd722fb5
INDEPENDENT_VERIFIER_COMMIT = 1d80923196b06c31dd21d054df89c48d7ab6ae1e
FROZEN_DEPLOYMENT_CONTRACT_COMMIT = 0c46e8b0bfd2568470d9a82ab726b741893bfa94
VERIFIED_EXACT_BYTES = YES (remote source commit only; NOT installed on host)
BOTH_LANES_PRESERVED = NO
QUEUE_AGENT_MIGRATION = NOT_RUN
CLEAN_ZERO_RELAY_CHAIN = NOT_RUN
FAILURE_RECOVERY_ZERO_RELAY_CHAIN = NOT_RUN
CONTROL_PLANE_ACCEPTANCE_RECOMMENDATION = NO
STATUS_MIRROR_ACTIVE = NO
BLOCKER = BLOCKED_HOST_ACCESS: this session executes in an ephemeral Linux cloud container, not on the macOS host. launchctl, the LaunchAgent plist, ~/.config/tennisauto-supervisor, ~/.local/share/tennisauto-supervisor (runtime, control checkout, Codex lane, Claude lane), the Codex CLI, the host SSH git credential and any running supervisor process are all absent. Steps A-F were NOT executed.
REPORT_PATH = agent_control/claude/supervisor_deploy_a13_20261008/DEPLOYMENT_REPORT.md
PRODUCTION_TENNIS_RUNTIME_TOUCHED = NO
ORDERS_ENABLED = NO
C04_UNTOUCHED = YES
NO_PROVIDER_SPEND = YES
GITHUB_OUTPUT_REPOSITORY = ellakeyes/tennis
GITHUB_OUTPUT_BRANCH = claude/a13-host-operator-deploy-kpfpe3
GITHUB_OUTPUT_COMMIT = 8aa7172c3be789be76f2580154a03249bd04e67e (receipt commit; recorded by follow-up commit on the same branch)
DISPATCH_OUTPUT_BRANCH_NOT_WRITTEN = agent/claude/supervisor-deploy-a13-20261008 (ellakeyes/tennisauto)

## 1. What was done (honest scope)

Preconditions 1 and 2 of the dispatch were executed in full. Preconditions 3 to 5 and execution steps A to G hit the STOP check "host access/permissions are missing", so this is a BLOCKED receipt and no host work is claimed.

| Dispatch step | Result |
|---|---|
| Pre 1: read full frozen contract, verifier result, A13 contract, runbook | DONE |
| Pre 2: independent identity check (source SHA, verifier SHA, ten file hashes) | DONE — MATCH |
| Pre 3: inspect launch agent, lanes, installed hash, queue, dirty files | HOST NOT REACHABLE |
| Pre 4: preserve unpublished Stage 01 / liveness evidence | NOTHING TOUCHED |
| A: stop old supervisor | NOT_RUN |
| B: preserve both lanes | NOT_RUN |
| C: queue AGENT migration | NOT_RUN (read-only pre-audit done) |
| D: install exact bytes, one restart, three polls | NOT_RUN |
| E: A13 clean chain | NOT_RUN |
| F: A13 failure chain | NOT_RUN |
| G: publish receipts | DONE (this directory) |

## 2. Identity verification (Precondition 2) — PASS

- `git ls-remote` on ellakeyes/tennisauto: `refs/heads/codex/tennisauto-supervisor-hardening-v1` = 4b93bb0ece81e4933b7e1649d9651e4fdd722fb5 (matches SOURCE_COMMIT).
- `refs/heads/agent/claude/supervisor-hardening-verify-20261008` = 1d80923196b06c31dd21d054df89c48d7ab6ae1e (matches INDEPENDENT_VERIFIER_COMMIT).
- Commit 0c46e8b0bfd2568470d9a82ab726b741893bfa94 exists and introduces SUPERVISOR_DEPLOYMENT_WINDOW_CONTRACT.md.
- SHA256 of each of the ten `agent_control/supervisor/*.py` files at 4b93bb0, computed in this session, equals the verifier's CANDIDATE_IDENTITY_4b93bb0.json and the candidate's SUPERVISOR_HARDENING_R4_SOURCE_EVIDENCE_SHA256.json (10/10). Values in HOST_PRECHECK.json.
- Verifier VERIFICATION_RESULT_4b93bb0.json read in full: VERDICT = VERIFIED, failed_gates = [], READY_FOR_LIVE_SUPERVISOR_DEPLOYMENT = YES, DEPLOYED = NO.
- Informational only: the candidate's own suite at 4b93bb0 ran in this container, 32 tests OK. This is not deployment evidence.

## 3. Host preflight (Precondition 3) — BLOCKED

Observed platform: Linux vm 6.18.44-fc-v80 x86_64, user root, HOME=/root. This is a cloud session container, not the Mac.

| Required host item | Observed |
|---|---|
| `launchctl` | MISSING |
| `~/Library/LaunchAgents/com.ellakeyes.tennisauto-supervisor.plist` | ABSENT |
| `~/.config/tennisauto-supervisor/config.json` | ABSENT |
| `~/.local/share/tennisauto-supervisor` (runtime, lanes, logs) | ABSENT |
| `/Applications/ChatGPT.app/Contents/Resources/codex` | ABSENT |
| host SSH git credential | ABSENT |
| supervisor / agent_runner process | NONE |
| previous installed supervisor identity | UNKNOWN (not readable) |

Because the lanes are unreachable, no statement is made about live workers, dirty files, or unpublished Stage 01 / liveness evidence. Nothing was stopped, moved, reset, cleaned, or launched.

## 4. Queue read-only pre-audit (informational, no mutation)

`agent_control/TASK_QUEUE.md` at tennisauto main 90916c7f680ab5a475727a630aa9d4e532223ee1, sha256 4f825e8b43b53bc425c658a5048c4971017eaad47dc4f7d3def89b93a1467532, unchanged before and after.

Parsed with the candidate's `parse_ready_tasks_with_errors` (supervisor.py at 4b93bb0):

| Section | Mode | Section hash | Candidate decision today | Required migration |
|---|---|---|---|---|
| TENNIS-CLAUDE-STATUS-006 | READY | 4527230870…fdce0 | TASK_PARSE_BLOCKED MISSING_AGENT | `AGENT: CLAUDE` |
| TENNIS-CODEX-STAGE01-R2-ACK-REPAIR-001 | READY | f62c0ed4c6…62bd4 | TASK_PARSE_BLOCKED MISSING_AGENT | `AGENT: CODEX` |
| TENNIS-CODEX-STAGE01-R2-ACK-REVERIFY-001 | AUTO_READY_AFTER=…ACK-REPAIR-001 | 425dbfe003…d736eb | TASK_PARSE_BLOCKED MISSING_AGENT | `AGENT: CODEX` |

No other READY / READY_PUBLIC_NETWORK / AUTO_READY_AFTER sections exist. Six PAUSED and three COMPLETE sections are non-dispatchable. Under the candidate parser there is zero stale accidental-launch risk until migration. The old supervisor's actual behaviour on these sections could not be observed. No A13 task section exists in the queue, so step E would in any case be WAITING_PM_A13_TASK.

## 5. Output branch discrepancy

The dispatch names OUTPUT_BRANCH `agent/claude/supervisor-deploy-a13-20261008` in ellakeyes/tennisauto. This session was attached to tennisauto read-only and is bound to branch `claude/a13-host-operator-deploy-kpfpe3` in ellakeyes/tennis. The receipts are published there under the dispatch's ALLOWED_GITHUB_OUTPUT_SCOPE path. A PM or host relay must mirror this directory to the tennisauto OUTPUT_BRANCH or re-point the dispatch, otherwise an hourly PM audit of tennisauto alone will classify this task as HANDOFF_GAP.

## 6. Exact safe next action

1. Re-run this exact dispatch from a session on the macOS host with: launchctl, the LaunchAgent, `~/.config/tennisauto-supervisor`, `~/.local/share/tennisauto-supervisor`, the Codex CLI, the host SSH git credential, and push access to ellakeyes/tennisauto.
2. Reuse the identity verification and queue pre-audit here; they need no re-derivation unless the remote refs move.
3. Before step E, the PM must author a bounded harmless A13 task in the queue (WAITING_PM_A13_TASK).

Until then: CONTROL_PLANE_ACCEPTED must remain NO. Nothing on the host changed as a result of this task.
