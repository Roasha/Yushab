# YÚSHAB storefront preview

Complete static website, ready to upload to GitHub and test with GitHub Pages. No npm install, build step, database, API key or paid domain is needed for this preview.

## Included

- 152 beauty, skincare and wellness listings, with individual product pages and local images.
- 14 size variants across seven products.
- Category, brand and price filters, search, sorting and pagination.
- Shopping bag, quantity controls, saved bag and checkout preview.
- About, contact, shipping, payment, return/refund, privacy, terms, FAQs, social and tracking pages.
- GitHub Pages deployment workflow and a local-link validation script.

The website is in `docs/`. GitHub deploys the contents of that folder, so its URL opens the actual home page. Do not upload the ZIP itself as the website.

## Upload and test online using GitHub Desktop

1. Extract this ZIP.
2. In GitHub Desktop, sign in and choose **File > New repository**. Name it `yushab`, choose a local folder, and create it.
3. Open that new repository folder. Copy the contents of the extracted `yushab-github` folder into it. Include `docs`, `scripts`, `.github`, `.gitignore` and this README. Do not nest the entire `yushab-github` folder inside the repository.
4. In GitHub Desktop, commit the changes with a message such as `Add Yushab store preview`.
5. Click **Publish repository**. A public repository works with GitHub Free. Keep the default branch named `main` because the included workflow targets it.
6. On GitHub.com, open the repository, then **Settings > Pages**. Under **Build and deployment**, set **Source** to **GitHub Actions**.
7. Open **Actions > Deploy YUSHAB preview > Run workflow**, select `main` and run it. The first automatic run may fail if Pages was not enabled yet. Run it again after step 6.
8. Wait for the workflow to finish successfully. Open **Settings > Pages > Visit site** or the URL shown on the deployment.

Your project URL will have the form `https://YOUR-USERNAME.github.io/yushab/`. This is an example, not an already deployed URL.

The package has more than 300 site files. GitHub Desktop avoids browser upload batch limits and preserves the required folder paths. Ensure `.github/workflows/deploy-pages.yml` appears in the repository.

Future commits pushed to `main` redeploy the preview automatically.

## Alternative: publish from a branch

If you prefer not to use a custom workflow, delete `.github/workflows/deploy-pages.yml` before uploading. In **Settings > Pages**, choose **Deploy from a branch**, then branch `main`, folder `/docs`, and save. Do not use both publishing methods at once.

## Local preview

Open `docs/index.html` directly, or run this from the repository root if Python is installed:

```sh
python -m http.server 8000 --directory docs
```

Then visit `http://localhost:8000/`. No installation is required for direct file opening.

## What to test

1. Open Home and every main navigation link.
2. Search for Golden Pearl, filter Face Wash, change the brand and sort by price.
3. Open a variable face wash and select a size before adding it to the bag.
4. Add another product, change quantities, remove an item and reload. The bag should remain in the same browser.
5. Confirm shipping is free and the total reflects the selected sizes and quantities.
6. Open the checkout preview and download a selection using dummy details.
7. Open all footer pages and check the mobile layout.
8. Test one direct product URL and refresh it.

## Preview scope

A visible design-preview banner identifies this as a non-transactional test. Payments, real orders, inventory, messages and shipment tracking are not connected. Forms download local drafts and do not send them to the business. Use dummy details for testing.

GitHub Pages is for this design demonstration, not a live commerce deployment. GitHub's usage rules prohibit using Pages to run an online business or e-commerce service. Connect production hosting and a commerce backend before accepting orders.

No domain has been purchased or connected. This package intentionally has no CNAME file. Uploading to GitHub does not register YÚSHAB.com.

The 3 October 2026 competitor catalog snapshot supplies the listed products and prices. It is not a live price feed. Product images are included from the reference catalog. The store still needs confirmed inventory, manufacturer information, business contacts, official social URLs, approved returns terms and a payment provider.

## Editing

- `docs/index.html`: home page.
- `docs/style.css`: appearance and mobile layout.
- `docs/app.js`: navigation, filtering, bag and preview forms.
- `docs/catalog.js`: catalog used by search and shopping interactions.
- `docs/product/`: individual product pages.
- `docs/assets/`: product images.

Product names and prices also appear in individual product-page HTML and some homepage cards. Keep those pages consistent with `catalog.js` when editing the catalog.

## Validation

Run `python scripts/validate.py`, `node --check docs/app.js` and `node --check docs/catalog.js` if Python and Node are available. The workflow runs these checks automatically.

Local references and JavaScript syntax were checked before delivery. The package has not been pushed to your GitHub account, and the GitHub deployment has not yet been run. Browser rendering and real payment processing have not been tested.

## Official references

- https://docs.github.com/en/pages/getting-started-with-github-pages/creating-a-github-pages-site
- https://docs.github.com/en/pages/getting-started-with-github-pages/using-custom-workflows-with-github-pages
- https://docs.github.com/en/pages/getting-started-with-github-pages/github-pages-limits
- https://github.com/actions/starter-workflows/blob/main/pages/static.yml
