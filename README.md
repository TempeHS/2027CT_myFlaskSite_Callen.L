# Brawlable

| Field                          | Detail                                                                                 |
| ------------------------------ | -------------------------------------------------------------------------------------- |
| **Website Title**              | Brawlable                                                                              |
| **Student Name(s)**            | Callen Lin                                                                             |
| **Class / Course**             | Year 9 Computer Technology                                                             |
| **Repository**                 | https://github.com/TempeHS/2027CT_myFlaskSite_Callen.L                                 |
| **Live Site / Codespaces URL** | v0.2 Alpha: https://github.com/TempeHS/2027CT_myFlaskSite_Callen.L/releases/tag/v0.2-a |
| **Date**                       | Last Edited on the 23rd of July 2026 :D                                                |

> Your website is the main piece of work. This README is short on purpose — it
> points a reader to your **2-minute walkthrough** and gives an honest
> **evaluation of what you delivered**.

---

## 1. Overview

**Purpose:**
Brawlable is a beginner-friendly tutorial website for Brawl Stars players. Featuring a homepage with a comprehensive roadmap for beginners, a detailed article gallery on key game mechanics, and a "Quick Start" guide with easy-to-begin tutorials.

**Target audience:** Brawlable is for new and experienced Brawl Stars players ages 13-21 to sharpen and improve their skill.

**Technology stack:** Python Flask · Jinja2 templates · Bootstrap (CDN) · custom JS · custom CSS · pytest

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

<!--
**Your walkthrough should show:**

- A tour of each page (Home and Contact)
- Your key Bootstrap components working (navbar, carousel, cards, map, form)
- The layout responding when the window is resized (navbar collapsing to a hamburger)
-->

---

## 3. Evaluation — Did You Deliver Your Statement of Intent?

This is the most important written part of your documentation. Evaluate the
website you **delivered** against the **Statement of Intent** you wrote during
planning. Be honest and use evidence — point to a page, a feature or a test.

### 3.1 Your Statement of Intent

Brawlable is a beginner-friendly tutorial website for Brawl Stars players. Featuring a homepage with a comprehensive roadmap for beginners, a detailed article gallery on key game mechanics, and a "Quick Start" guide with easy-to-begin tutorials.

Currently, Brawl Stars continues to introduce new features and mechanics, resulting in becoming increasingly more complex, leaving beginners struggling to keep up. This often results in unnecessary confusion, poor gameplay experience, and a decline in player engagement.

By addressing this issue with a dedicated site that guides users through Brawl Stars mechanics and brawlers, beginners can find clear and concise descriptions of a range of features. This will help the community become more engaged, encourage player confidence, and support long-term player retention.

The primary audience is young Brawl Stars players aged 13-21 who are either new to Brawl Stars or want to improve their gameplay. These users are comfortable with technology and prefer quick, easily accessible information, but have limited time, so the site must offer both fast navigation and comprehensible content. The secondary audience includes more experienced players who may use the site to enhance their strategies or further deepen their game knowledge.

Brawlable will simplify the learning curve of new players, making it easier to quickly understand and enjoy the game Brawl Stars. With easy-to-follow tutorials, clear game mechanics and practical strategies, we aim to enhance player engagement, confidence and long-term retention.

### 3.2 What You Delivered

Primary Pages

<!-- Add later: Showing what you can learn, and a dedicated section for casual trophy players and ranked players. -->

| Page          | Route                     | What it delivers                                                                                                                                       |
| ------------- | ------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------ |
| Home Page     | `/`                       | Introduces Brawlable as a learning guide to Brawl Stars with a Hero Video. Followed by cards for Brawlers, Game Modes, Mechanics.                      |
| Contacts Page | `/contact` and `/support` | Offers a contact page with a embeded map from Google Maps, a responsive form for general equiries, support, feedback and bug reports.                  |
| Search Page   | `/search`                 | Allows users to search for pages using a URL. Matching results shows clickable links while unsuccessful searches shows a warning and suggested results |

.  
.  
.  
.  
.  
.  
.  
.  
.  
.  
.  
.  
.  
.  
.  
.  
.  
.  
.  
.  
.

Site Contents

| Contents   | Route                                              | How it is made and why it is made                                                                                              |
| ---------- | -------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------ |
| Hero Video | [↗ View Hero Video](./static/videos/hero.mp4)      | Collected game footage from gameplay and spectator mode and edited in Premiere Pro to create a unique engaging hero.           |
| Favicon    | [↗ View Site Favicon](./static/images/favicon.svg) | The favicon is made in Adobe Illustrator and is exported as a SVG (Scalable Vector Graphics) as it can be infinitely zoomed in |

| Contents     | Route                                                                                                                                                                                                                                                                                        | Where is it from, Why it is chosen, Additional Decisions made                                                                                                                                                     |
| ------------ | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| Index Images | [↗ View Image 1](./static/images/index-feature1.jpg) <br> [↗ View Image 1](./static/images/index-feature2.jpg) <br> [↗ View Image 1](./static/images/index-feature3.jpg) <br> [↗ View Image 1](./static/images/index-feature4.jpg) <br> [↗ View Image 1](./static/images/index-feature5.jpg) | From [Supercell Brawl Stars Fankit](https://fankit.supercell.com/d/YvtsWV4pUQVm/game-assets), and is used for it to feel distinct and relatable to users. The images are reduced to below 5250KB for performance. |

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
