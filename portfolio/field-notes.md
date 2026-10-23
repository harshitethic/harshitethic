# Three engineering case studies — short edition

These summaries link to source and repeatable validation. For detailed threat models, metrics and experiments see the [full case-study archive](engineering-case-studies.md).

## 1. LeaseLedger — a worker wakes up after losing its lease

**Problem.** Background work must survive process crashes, but an old worker can resume and incorrectly mark reclaimed work complete.

**Approach.** Store job state in SQLite WAL, atomically claim leases, increment fencing tokens and require a valid lease token for completion. Track retries, dead letters and audit events.

**Reproduce.** Run `python3 -m examples.recovery_walkthrough` from the checkout and compare against [the recorded output](https://github.com/harshitethic/LeaseLedger/blob/main/docs/recovery-demo-output.json). Inspect [the test workflow](https://github.com/harshitethic/LeaseLedger/actions/workflows/ci.yml).

**Trade-off.** Single-host durability and at-least-once processing; external side effects need idempotency, and multi-host SQLite/NFS is outside scope.

**Source:** [Repository](https://github.com/harshitethic/LeaseLedger) · [Architecture](https://github.com/harshitethic/LeaseLedger/blob/main/docs/architecture.md) · [Recovery](https://github.com/harshitethic/LeaseLedger/blob/main/docs/backup-and-recovery.md)

## 2. PatchPilot — a coding agent should not execute arbitrary project scripts on the host

**Problem.** An automated patch workflow that runs tests against an unfamiliar repository can trigger unsafe commands.

**Approach.** Separate workspaces, keep model-generated edits reviewable, run detected test commands only through a fail-closed Docker isolation path, limit Git subprocess output and guard staged secrets.

**Verify.** Review [isolation CI](https://github.com/harshitethic/PatchPilot/actions/workflows/docker-isolation.yml), [security boundaries](https://github.com/harshitethic/PatchPilot/blob/main/docs/security-boundaries.md), and [browser verification](https://github.com/harshitethic/PatchPilot/blob/main/docs/browser-verification.md).

**Trade-off.** Docker test isolation does not sandbox every host Git operation or make the local API safe to expose to multiple untrusted tenants.

**Source:** [Repository](https://github.com/harshitethic/PatchPilot) · [Preview release](https://github.com/harshitethic/PatchPilot/releases/tag/v0.4.0)

## 3. ClonePeek — inspect a repo's hidden startup hooks before trusting it

**Problem.** Simply opening a project or running an install can execute code specified in editor tasks, package scripts, devcontainers and agent hooks.

**Approach.** Use bounded passive file reads; identify known hook surfaces, show source paths and remediation advice, and output machine-readable findings that can run in GitHub Actions.

**Verify.** Watch [the actual CLI replay](https://harshitethic.github.io/clonepeek/#video-demo), inspect [the fixture evaluation](https://github.com/harshitethic/clonepeek/blob/main/docs/EVALUATION.md), and check [the released Action](https://github.com/marketplace/actions/clonepeek-passive-repository-execution-audit).

**Trade-off.** Heuristics produce false positives and negatives. No passive scan proves that a repository is safe; unmodeled dynamic execution remains possible.

**Source:** [Repository](https://github.com/harshitethic/clonepeek) · [Threat model](https://github.com/harshitethic/clonepeek/blob/main/docs/THREAT_MODEL.md)
