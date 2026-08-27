# GitHub Profile README — setup

Repository: `https://github.com/harshitethic/harshitethic`

## Upload structure

Upload the files/folders from this package so the repo looks like:

```text
harshitethic/
├── README.md
├── assets/
│   ├── header.svg
│   ├── github-telemetry.svg
│   ├── github-activity.svg
│   └── Harshit-Ethic-Cyber-Banner.png
└── .github/
    └── workflows/
        └── update-profile.yml
```

## One-time activation

After uploading, open:

**Actions → Update profile → Run workflow**

The workflow will immediately populate:

- your latest 6 repositories
- repository links
- descriptions
- star counts
- public repository count
- follower count
- total stars
- contribution activity graphic

Then it runs automatically once per day.

## Why the README uses raw.githubusercontent.com

The previous version depended on a relative SVG path that was rendering as a broken image in the profile view. This version uses the repository's raw GitHub URL for the visual assets, so the image resolves directly from the profile repository.

## No external stats widgets

The unreliable third-party GitHub Stats / Top Languages / Activity Graph images have been removed. The profile now generates its own SVG telemetry and activity graphics through GitHub Actions.

## Email

The email CTA uses:

`mailto:contact@harshitethic.com`

GitHub READMEs cannot execute arbitrary JavaScript, so a true clipboard-copy button isn't reliable inside the profile README.
