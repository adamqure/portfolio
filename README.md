# adamure.com

Portfolio site for Adam Ure, Software Engineer for Connected Devices.

- `build.py` generates every page in `site/` from one shared header/footer, plus `site/resume.pdf` (rendered with headless Chrome from `resume/resume.html`).
- Edit content in `build.py`, run `python3 build.py`, then commit and push. GitHub Actions publishes `site/` to GitHub Pages.
- `profile.md` has the profile description to keep in sync with LinkedIn and Upwork.
- The previous Astro site is preserved at the `astro-site-v1` tag.
