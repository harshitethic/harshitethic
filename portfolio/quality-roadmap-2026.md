# Engineering portfolio mission — 15 October 2026

This is an evidence-linked, **finite portfolio work checklist**, not a hiring
score or a promise of follower growth. Each item counts only with a public
repository, test result or profile state supporting it. Scope: 20 defined
milestones across profile, engineering, community and evaluation.

## Completed (16 / 20)

- [x] Audit public repositories, profile, follower baseline and six pinned projects
- [x] Record GitHub CodeQL and dependency risk before modifying flagship code
- [x] Publish a professional engineering bio and evidence-first README
- [x] Reorganize six pins to emphasize technical breadth and genuine adoption
- [x] Publish technical case studies linked to source, PRs and CI
- [x] Link reproducible demos and a reachable real-world full-stack website
- [x] Isolate PatchPilot repository tests in fail-closed Docker containers ([PR #24](https://github.com/harshitethic/PatchPilot/pull/24))
- [x] Restrict PatchPilot host execution to Git and keep test logs private ([PR #25](https://github.com/harshitethic/PatchPilot/pull/25))
- [x] Prove RepoPilot HTTP import/search lifecycle with 30 automated tests ([PR #20](https://github.com/harshitethic/RepoPilot/pull/20))
- [x] Replace PsychologyOS known admin defaults; verify full production build ([PR #12](https://github.com/harshitethic/PsychologyOS/pull/12))
- [x] Verify FxSound portability on independent Linux and macOS CI ([PR #2](https://github.com/harshitethic/fxsound-linux-macos/pull/2))
- [x] Develop original LeaseLedger durable queue with fenced concurrent workers ([source](https://github.com/harshitethic/LeaseLedger))
- [x] Publish LeaseLedger tests, architecture docs, v0.1.2 fault-injection and queue-progress fix, online recovery improvements and verified release ([CI](https://github.com/harshitethic/LeaseLedger/actions))
- [x] Link genuine accepted third-party open-source work, rather than opened PR counts
- [x] Establish a weekly quantitative follower/star progress review against the baseline
- [x] Respond to a concrete maintainer review on an issue-linked external PR: fixed [ChurchCRM #10484](https://github.com/ChurchCRM/CRM/pull/10484), verified i18next extraction and lint, and passed independent CodeQL/Semgrep checks. Merged on 14 October 2026 after the requested fixes and verification.

**Finite milestone progress: 80% complete (16/20).** This is not a claim
that the overall mission or the follower target is 80% complete.

## Outstanding (4 / 20)

- [ ] Independently review PatchPilot production/multi-user security despite zero
      open CodeQL findings after [PR #26](https://github.com/harshitethic/PatchPilot/pull/26).
      PsychologyOS dependency remediation is complete in [PR #13](https://github.com/harshitethic/PsychologyOS/pull/13); the broader independent review remains open.
- [ ] Produce a locally verifiable end-to-end screen recording for the
      newly pinned developer tools; avoid polished mock-ups misrepresented as working apps
- [ ] Add independent multi-user/production threat review and deployment proof
      before presenting any local-only tool as production secure
- [ ] Obtain independent experienced-engineer feedback and iterate on
      architectural trade-offs, performance evidence, and hiring clarity

## Community growth — separate ongoing goal

**Verified baseline:** 150 followers on 15 Oct 2026; 48 public repositories and four visible native achievement types (Pull Shark, Quickdraw, YOLO, Starstruck).
**Target:** 500 genuine followers (+350). Growth requires other people to
choose to follow and is not guaranteed.

Useful non-spam activities:
1. Publish practical engineering writeups with reproduction commands.
2. Keep tests, releases, changelogs and contribution guidance current.
3. Respond to maintainers' code review feedback and help new contributors.
4. Share case studies where developers voluntarily seek this technical topic.
5. Measure followers, releases and traffic weekly; adjust topic focus from
   genuine engagement instead of mass-follow or artificial stars.

**Achievement check:** The live profile still shows four types. The genuine
co-author trailer remains in the merged WhatsApp PR #40 commit, but Pair
Extraordinaire has not appeared. No badge award or processing date is promised.
Further opportunities require accepted community answers, genuine collaboration,
or voluntary adoption; sponsorship would require a separately agreed budget.

**Active external follow-through:** [Poetry #11135](https://github.com/python-poetry/poetry/pull/11135)
received a tested fix for the reviewer's executable-alias/source-directory
collision. Local environment suites: 97 passed, four platform skips; real CLI
checks passed for plain/custom aliases. [Upstream CI passed](https://github.com/python-poetry/poetry/actions/runs/38736327430); the PR remains open for
maintainer review.

No follower purchasing, fake engagement, bulk unsolicited DMs or vanity PRs.

## Latest verified engineering milestone — 15 October 2026

- [PatchPilot PR #30](https://github.com/harshitethic/PatchPilot/pull/30) merged as
  [`d05bd36`](https://github.com/harshitethic/PatchPilot/commit/d05bd36f7c10c8a5fb5f49caaa17fe6778f99e64).
  Reproduced provider failures; added bounded transfers, an overall deadline,
  sanitized errors, cancellation cleanup and real TCP/Git integration tests.
- **107 backend tests** passed locally and in independent Python 3.11/3.12 CI;
  Docker isolation and CodeQL also passed on the exact PR head before merge.
- Live GitHub search reports **25 merged external PRs across 9 repositories**,
  including the now-merged ChurchCRM translation-extraction contribution.
- [PatchPilot #23](https://github.com/harshitethic/PatchPilot/issues/23) stays open:
  worker privilege separation, cloning/aggregate quotas and independent
  multi-user deployment review remain incomplete. Per-call provider limits
  do not establish public hosting safety.
- [PsychologyOS PR #13](https://github.com/harshitethic/PsychologyOS/pull/13) resolved
  the remaining audit findings: zero npm audit vulnerabilities at verification.
  Three regression tests verify cyclic merges and the real Prisma config loader.
- [PsychologyOS PR #14](https://github.com/harshitethic/PsychologyOS/pull/14) prevents
  reseeding from erasing student learning history. Four real SQLite scenarios
  verify identity preservation, changed content, rollback and retry; CI now also
  runs the production build. CI and CodeQL passed on the PR and merged main.
- [PsychologyOS PR #15](https://github.com/harshitethic/PsychologyOS/pull/15) fixed
  malformed admin signatures and session survival after password rotation or
  account deletion. [PR #16](https://github.com/harshitethic/PsychologyOS/pull/16)
  makes learning attempts atomic and rejects malformed submissions. Thirteen
  production-handler HTTP scenarios verify access boundaries, rollback and
  concurrent XP accounting against disposable SQLite. CI and CodeQL passed on
  both PR heads and merged main. Initial CI contention was fixed, not suppressed.
- [PsychologyOS #10](https://github.com/harshitethic/PsychologyOS/issues/10) now
  tracks a separate Prisma major migration. The established HTTP suite must be
  repeated during that migration; the scoped override also needs reassessment.
- [PatchPilot PR #31](https://github.com/harshitethic/PatchPilot/pull/31) closes
  reproduced repair-prompt leaks through raw Git diffs and test output. All
  **112 backend tests**, Docker isolation and CodeQL passed before merge and
  on main [`59f3828`](https://github.com/harshitethic/PatchPilot/commit/59f38282dbb1df2278c97645cc11323e8fa36867).
- [LeaseLedger PR #5](https://github.com/harshitethic/LeaseLedger/pull/5) fixes
  expired-lease acceptance during SQLite writer contention. Six real-lock
  regressions fail before the fix and pass after it. **40 tests** and the
  existing four-process benchmark smoke passed on Kali and macOS. Python
  3.11–3.13 CI, packaging, lint and CodeQL passed before merge and on main
  [`f0a6d71`](https://github.com/harshitethic/LeaseLedger/commit/f0a6d713c7143ab3cce1ee58cc573a60d01456da).
- [LeaseLedger PR #6](https://github.com/harshitethic/LeaseLedger/pull/6) adds
  immutable publication after the complete CI/CodeQL gate. Eight release tests
  bring the suite to **48**. The actual main workflow successfully published
  [v0.1.3](https://github.com/harshitethic/LeaseLedger/releases/tag/v0.1.3), targeting
  [`783ad67`](https://github.com/harshitethic/LeaseLedger/commit/783ad67c57277c0095316d51dd9063d669b360da).
  [Run 38745249190](https://github.com/harshitethic/LeaseLedger/actions/runs/38745249190)
  verifies the publication step after all required jobs succeeded.
- RepoPilot main already includes PRs #22–24 beyond the older #21 handoff;
  review current source before repeating work. RepoPilot was not modified in
  this milestone. LeaseLedger now includes the lock-contention fix above.
- ClonePeek was excluded from this work. No repository deletion, visibility
  change, production deployment or existing user-data migration was performed.

These results strengthen existing milestones; the finite checklist remains
**16/20**, and neither follower growth nor an independent security review is
claimed as completed.
