# Brawlable

| Field                          | Detail                                                 |
| ------------------------------ | ------------------------------------------------------ |
| **Website Title**              | Brawlable                                              |
| **Student Name(s)**            | Callen Lin                                             |
| **Class / Course**             | Year 9 Computer Technology                             |
| **Repository**                 | https://github.com/TempeHS/2027CT_myFlaskSite_Callen.L |
| **Live Site / Codespaces URL** | N/A                                                    |
| **Date**                       | N/A                                                    |

> Your website is the main piece of work. This README is short on purpose — it
> points a reader to your **2-minute walkthrough** and gives an honest
> **evaluation of what you delivered**.

---

## 1. Overview

**Purpose:** <!-- One or two sentences: what the site is and why it exists (from your Statement of Intent). -->

**Target audience:** <!-- One sentence: who the site is for (from your personas). -->

**Technology stack:** Python Flask · Jinja2 templates · Bootstrap (CDN) · custom CSS · pytest

---

## 2. Walkthrough Video (2 minutes)

This is the most important part of your documentation — it shows your website running.

<!--
  Embed a ~2 minute walkthrough. Replace VIDEO_ID with your YouTube video ID:
  [![Website Walkthrough](https://img.youtube.com/vi/VIDEO_ID/0.jpg)](https://www.youtube.com/watch?v=VIDEO_ID)

  OR link a screen recording stored in the repository:
  [Watch the Walkthrough](./docs/walkthrough.mp4)
-->

| Field            | Detail |
| ---------------- | ------ |
| **Link / Embed** |        |
| **Duration**     |        |

**Your walkthrough should show:**

- A tour of each page (Home and Contact)
- Your key Bootstrap components working (navbar, carousel, cards, map, form)
- The layout responding when the window is resized (navbar collapsing to a hamburger)

---

## 3. Evaluation — Did You Deliver Your Statement of Intent?

This is the most important written part of your documentation. Evaluate the
website you **delivered** against the **Statement of Intent** you wrote during
planning. Be honest and use evidence — point to a page, a feature or a test.

### 3.1 Your Statement of Intent

<!-- Paste the Statement of Intent you wrote during planning so the reader can judge your site against it. -->

### 3.2 What You Delivered

#### Primary Pages of Brawlable

| Page           | Route          | What it delivers                                                                                                                                       |
| -------------- | -------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------ |
| Home           | `/`            |                                                                                                                                                        |
| Contact        | `/contact`     | Provides a page that allows you to provide feedback, receive assistance and report bugs.                                                               |
| Sitemap        | `/sitemap`     | A site map that shows all the pages across the site with categories for accessibility                                                                  |
| Privacy Policy | `/privacy`     | Provides information how the site handles data in the website                                                                                          |
| Attributions   | `/attribution` | Provides attribution to all the dependencies and repositories used in the project with a direct link and the LICENSE file accessible in a static link. |
| Search         | `/search`      | Offers a search that can be found on the header where it will show search results and instantly redirect you for exact matches.                        |

#### Backend Features of Brawlable

| Page                  | Route     | File Location                                      | What it delivers                                                                                                                                                                                                                                                |
| --------------------- | --------- | -------------------------------------------------- | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| 404 Page Not Found    | `/404`    | `templates/error_handler/404.html`, `test_app3.py` | When you visit a page that is not found by the website, it results in a 404 page, and provides options to go to the homepage or visit the sitemap. It also provides a detailed report that can be immediately copied into support with a hyperlink to the page. |
| Search Configurations | `/search` | `templates/search.html`, `search_config.py`        | The search configurations allows you search the exact names to get immediately redirected handled by search_services, and keywords show recommended results. This also filters disallowed text.                                                                 |
| Search Services       | `/search` | `templates/search.html`, `search_services.py`      | This sanitizes the input of the text being input into the search bar. Handling blank text, script injection, limiting the length of requests, and allows the requests to be handled and sent to the user as a query in the format of `/search?q=asd`            |
| Search No Results     | `/search` | `templates/search.html`, `~/search_services.py`    | When a query does not return any results for a query that includes a value, it provides a notice telling the user that no results were found for the content and shows suggested results the user can try.                                                      |

### 3.3 Evaluation Against Your Intent (2–3 paragraphs)

> Take each aim in your Statement of Intent and evaluate **how well the
> delivered site meets it**. Where did you meet your intent? Where did you fall
> short, and why? Support every judgement with evidence from your site.

<!-- Write 2–3 paragraphs. -->

### 3.4 Overall Effectiveness (1–2 paragraphs)

> Step back from the detail. Overall, **how effective** is the website at
> achieving its purpose for its target audience? Weigh what works against what
> falls short, and state what you would improve to better meet your intent.

<!-- Write 1–2 paragraphs. -->

---

## 4. Acknowledgements

> List anything you did not make yourself — tutorials, images, fonts, icons and
> libraries. Using content without acknowledgement may constitute academic
> misconduct.

| What you used | Source / Creator | Licence | What you used it for   |
| ------------- | ---------------- | ------- | ---------------------- |
| Bootstrap     | Bootstrap team   | MIT     | Layout and components  |
| Flask         | Pallets Projects | BSD     | Web server and routing |
|               |                  |         |                        |
|               |                  |         |                        |

---

> **Student Declaration:** All work submitted is my own except where explicitly acknowledged above.
