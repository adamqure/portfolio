# adamure.com

Personal portfolio site, built with [Astro](https://astro.build) and deployed to
[GitHub Pages](https://pages.github.com) at the custom domain **adamure.com**.

## Local development

Requires Node 18+.

```bash
npm install      # install dependencies
npm run dev      # start dev server at http://localhost:4321
npm run build    # build static site to ./dist
npm run preview  # preview the production build locally
```

## Project structure

```
src/
  layouts/Layout.astro   # shared <head>, global styles
  pages/index.astro      # homepage (add more .astro/.md files here for new pages)
public/                  # static assets served as-is (favicon, images)
astro.config.mjs         # set `site` to your final URL
```

Add a new page by dropping a file in `src/pages/` — `about.astro` becomes
`/about`. Markdown files work too if you'd rather write posts in Markdown.

## Deploy to GitHub Pages

Deployment is automated by `.github/workflows/deploy.yml` (the official
`withastro/action`), which builds the site and publishes it on every push to
`main`.

One-time setup:

1. Create a repo under your account and push this directory to its `main` branch:

   ```bash
   git init
   git add .
   git commit -m "Initial adamure.com site"
   git remote add origin https://github.com/adamqure/portfolio.git
   git branch -M main
   git push -u origin main
   ```

2. In the repo on GitHub: **Settings → Pages → Build and deployment → Source**,
   choose **GitHub Actions**.

3. Push (or re-run the workflow from the **Actions** tab). The build runs and
   deploys automatically. Watch progress under **Actions**.

### Custom domain (adamure.com)

The `public/CNAME` file already pins the site to `adamure.com`, so the domain is
applied automatically on deploy. To make DNS resolve:

- At your domain registrar, create a **CNAME** record for `www` → `adamqure.github.io`,
  **or** for the apex `adamure.com` add the four GitHub Pages **A records**
  (`185.199.108.153`, `185.199.109.153`, `185.199.110.153`, `185.199.111.153`)
  and an `AAAA`/`ALIAS` if your registrar supports it.
- In **Settings → Pages → Custom domain**, confirm `adamure.com` and enable
  **Enforce HTTPS** once the certificate is issued.

See GitHub's guide: <https://docs.github.com/pages/configuring-a-custom-domain-for-your-github-pages-site>.

> Note: the repo name (e.g. `portfolio`) doesn't affect the URL while the
> `adamure.com` custom domain is in place — the site always serves at the domain
> root. Only if you removed the custom domain would a repo named `portfolio`
> serve at `https://adamqure.github.io/portfolio` and need `base: '/portfolio'`
> in `astro.config.mjs`. (A repo named `adamqure.github.io` serves at the root of
> `https://adamqure.github.io` with no extra config.)
