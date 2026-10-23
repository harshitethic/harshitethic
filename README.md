<div align="center">

<img src="assets/header.svg" width="100%" alt="Harshit Sharma — AI tools, backend systems and open-source software" />

# Harshit Sharma

**Software engineer | AI developer tools · backend reliability · developer security · cross-platform software**

I build and maintain practical developer software with reproducible tests, explicit security boundaries and reviewable changes.

[![Portfolio documentation links](https://github.com/harshitethic/harshitethic/actions/workflows/profile-docs.yml/badge.svg)](https://github.com/harshitethic/harshitethic/actions/workflows/profile-docs.yml)

[Website](https://harshitethic.com) · [LinkedIn](https://www.linkedin.com/in/harshitethic/) · [Email](mailto:contact@harshitethic.com) · [Engineering notes](portfolio/engineering-case-studies.md)

</div>

## Featured original work

| Project | Why it matters | Try it / verification |
| --- | --- | --- |
| **[LeaseLedger](https://github.com/harshitethic/LeaseLedger)** · Python / SQLite | Durable, single-host job queue: fenced worker leases, crash recovery, retries and consistent backups. | [One-command recovery demo](https://github.com/harshitethic/LeaseLedger/blob/main/docs/reproducible-demo.md) · [CI](https://github.com/harshitethic/LeaseLedger/actions/workflows/ci.yml) |
| **[PatchPilot](https://github.com/harshitethic/PatchPilot)** · Python / FastAPI | Local-first AI coding workflow with bounded execution, fail-closed Docker test isolation and reviewable Git diffs. | [Preview release](https://github.com/harshitethic/PatchPilot/releases/tag/v0.4.0) · [Isolation CI](https://github.com/harshitethic/PatchPilot/actions/workflows/docker-isolation.yml) |
| **[ClonePeek](https://github.com/harshitethic/clonepeek)** · Python / GitHub Actions | Passive scanner for known editor, package, devcontainer and AI-agent execution hooks in unfamiliar repositories. | [Real CLI replay](https://harshitethic.github.io/clonepeek/#video-demo) · [GitHub Action](https://github.com/marketplace/actions/clonepeek-passive-repository-execution-audit) |
| **[RepoPilot](https://github.com/harshitethic/RepoPilot)** · FastAPI / React | Browse and search repository source locally, with optional Ollama Q&A and guarded ZIP/Git imports. | [Real browser walkthrough](https://github.com/harshitethic/RepoPilot/blob/main/docs/RepoPilot-live-verified-walkthrough.gif) · [First-run guide](https://github.com/harshitethic/RepoPilot/blob/main/docs/first-run.md) |

**Hands-on evidence:** [Three short engineering case studies](portfolio/field-notes.md) · [Full technical portfolio](portfolio/engineering-case-studies.md) · [Watch/try real demos](portfolio/demo-gallery.md)

## Accepted contributions to other projects

My upstream fixes are reviewed and merged by other maintainers. Representative **merged** changes (verified 23 October 2026):

- **[Concord #1144](https://github.com/useconcord/concord/pull/1144)** — fix download URL lifetime and add regression tests.
- **[ChurchCRM #10814](https://github.com/ChurchCRM/CRM/pull/10814)** — immediately explain disabled calendar sharing when a token is generated.
- **[agent-trace #264](https://github.com/Siddhant-K-code/agent-trace/pull/264)** — implement a read-only Codex hook activation preflight.
- **[ntfy-ios-NextGen #13](https://github.com/new-usemame/ntfy-ios-NextGen/pull/13)** — support copying notification actions on iOS.
- **[Concord #1142](https://github.com/useconcord/concord/pull/1142)** — preserve integer precision and trailing zeros.
- **[ChurchCRM #10759](https://github.com/ChurchCRM/CRM/pull/10759)** — fix missing Slim routing in FrankenPHP.

[See merged upstream PRs](https://github.com/search?q=author%3Aharshitethic+is%3Apr+is%3Amerged&type=pullrequests) · [See open PRs](https://github.com/search?q=author%3Aharshitethic+is%3Apr+is%3Aopen&type=pullrequests). Open/draft work is not presented as accepted.

## Community-used projects

- **[chatgpt-bot-telegram](https://github.com/harshitethic/chatgpt-bot-telegram)** — maintained JavaScript/Telegram example, safer configuration and regression tests.
- **[ChatGPT-Telegram-Bot](https://github.com/harshitethic/ChatGPT-Telegram-Bot)** and **[whatsapp-chatgpt](https://github.com/harshitethic/whatsapp-chatgpt)** — popular *legacy* examples; the original API integrations are not presented as current production-ready software.
- **[FxSound Linux/macOS](https://github.com/harshitethic/fxsound-linux-macos)** — experimental native audio port with Linux/macOS build CI. **Alpha**, not a finished replacement.

**Clean checkout evidence:** [54 + 100 + 116 Python tests on Kali, commands and limitations](portfolio/verified-clean-checkouts-2026-10-23.md).

**Independent testers:** [Reproduce the flagship demos and report verified feedback](portfolio/independent-evaluation.md). The review checklist distinguishes real users from automated fixtures and lists security, benchmark and release boundaries.

## Working principles

**Reproduce → isolate the cause → write a regression → implement the fix → run CI → document limits → get review.**

Tooling: Python · TypeScript/JavaScript · C++ · SQLite · FastAPI · React · Linux/macOS · Docker · GitHub Actions.

Security claims are scoped to the demonstrated boundary. Tests, synthetic benchmarks and maintainer-run examples do **not** imply independent security certification or production adoption.

**Collaboration:** [Issues and discussions](https://github.com/harshitethic?tab=repositories) · [Technical writeups](portfolio/engineering-case-studies.md) · [contact@harshitethic.com](mailto:contact@harshitethic.com)

<sub>Want every architecture detail and source link? Read the [original extended profile](portfolio/profile-full-2026-10-23.md).</sub>
