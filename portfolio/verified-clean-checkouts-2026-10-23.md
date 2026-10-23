# Three flagship projects — clean checkout verification

Recorded **23 October 2026** on an authorized Kali Linux workstation (Intel Core i9-14900K, Linux 7.1.5+kali-amd64, Python 3.13.12). The runs were executed from **fresh shallow public clones** in disposable `/tmp` directories, not working trees modified for the tests.

This is **maintainer-operated reproduction**, not independent adoption, code review, or external security certification.

| Project | Actual command family | Observed result | What was not tested in this run |
| --- | --- | --- | --- |
| [LeaseLedger](https://github.com/harshitethic/LeaseLedger) | `python3 -m examples.recovery_walkthrough`; `python3 -m unittest discover -s tests -q`; `python3 -m compileall -q leaseledger` | 54 tests passed; deterministic demo verified stale-ACK refusal, lease reclamation, consistent online SQLite backup/restore | Exactly-once external effects, multi-host queueing, production traffic |
| [RepoPilot](https://github.com/harshitethic/RepoPilot) | In disposable Python virtualenv: install `backend/requirements-test.txt`; `PYTHONPATH=backend python -m unittest discover -s backend/tests -q`; compile backend | **100 backend tests passed**, Python 3.13 | Manual Windows/macOS onboarding, live LLM quality and an interactive browser walkthrough in this run |
| [PatchPilot](https://github.com/harshitethic/PatchPilot) | In disposable Python virtualenv: install `backend/requirements.txt`, `cd backend`, `python -m unittest discover -s tests -q`; compile app/tests | **116 backend tests passed**, Python 3.13 | Real Docker sandbox execution in this local run, macOS UI, independent pentest or multi-tenant isolation |

RepoPilot's suite printed `Resource admission configuration or lock unavailable` four times while testing failure paths; the exit code was 0 and all 100 tests passed. Do not turn this into an assertion that all runtime environments are warning-free.

## Separate GitHub CI evidence

- [LeaseLedger: CI matrix](https://github.com/harshitethic/LeaseLedger/actions/workflows/ci.yml), including [successful reviewer-guide PR #8 CI](https://github.com/harshitethic/LeaseLedger/actions/runs/39990942446) and [successful 12-trial benchmark PR #9 CI](https://github.com/harshitethic/LeaseLedger/actions/runs/39991870725).
- [RepoPilot: CI](https://github.com/harshitethic/RepoPilot/actions/runs/39990956693) and [CodeQL](https://github.com/harshitethic/RepoPilot/actions/runs/39990956527) passed on the review-guide PR.
- [PatchPilot: CodeQL](https://github.com/harshitethic/PatchPilot/actions/runs/39990951365) passed on its review-guide PR. Its backend tests and [Docker isolation CI](https://github.com/harshitethic/PatchPilot/actions/workflows/docker-isolation.yml) run on separate path triggers and are **not** represented by the documentation-only PR result.

The three test counts are from this fresh Kali run. Read each repository's README for supported versions and reproduction details; PatchPilot CI currently targets Python 3.11–3.12, so a passing Python 3.13 local suite is supplementary rather than a platform support commitment.

## Independent follow-up, not yet completed

The following requests invite real independent review with explicit test scope:

- [LeaseLedger correctness/benchmark review](https://github.com/harshitethic/LeaseLedger/issues/10)
- [PatchPilot Docker boundary review](https://github.com/harshitethic/PatchPilot/issues/40)
- [RepoPilot first-run/isolation review](https://github.com/harshitethic/RepoPilot/issues/40)

**Do not add external-review totals to the profile until genuine responses are received and verified.** For user/adoption evidence criteria, see [the independent evaluation guide](independent-evaluation.md).
