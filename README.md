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

<!--
  Here is a heavily refined version :D
  You can find the older version at the very bottom of this document since you are reading this comment :P
-->

> [!IMPORTANT] Notice
> The site has numerous href="#" or working in progress pages.  
> The reason is that I find it unfeasible to collect all assets and designs necessary to rebuild something towards a wiki platform.

**My Primary Pages**
| Pages | Route | What it has delivered |
| ---------------- | ----------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| The Homepage | `/` | Homepage with a Bootstrap navbar and dropdown menu, 82vh hero video with mute/un-mute button using Bootstrap Icons and a call-to-action text, greetings section, three features topic cards (Brawlers, Gamemodes, Mechanics), six advanced strategy cards using Bootstrap Cards and Icons, two feature cards with game modes (Ranked or Trophy), and a footer. |
| The Contact Page | `/contact` | The Contact page featuring an embedded Google Map and a responsive Bootstrap contact form with fields for name, email address, and message. |
| The Brawler Page | `/brawlers` | The Brawler Page with six Bootstrap cards organised by rarity, each featuring a image, a gradient overlay, a description and a navigation button to each of the individual Brawler categories. |
| The Search Page | `/search` | The Search Page has a dynamic search results displaying titles and descriptions, and suggested navigation links when no matching results found. |
| The About Page | `/about` | About Us shows the website's missions, using Bootstrap card and grids, information explaining the purpose of the website, a call-to-action link to the onboarding page. |

**Other Significant Pages**

| Pages              | Route          | What it has delivered                                                                                                                                                                                                                                                     |
| ------------------ | -------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| The Attributions   | `/attribution` | The Attribution page features quick id navigation shortcuts on the top, organised acknowledgement for Python Dependencies, third-party repos, content sources and project contributors. It also includes direct links to the external program and LICENSE files attached. |
| The Privacy Policy | `/privacy`     | The Privacy Policy page outlines how the website collects data, cookies, third-party services, policy updates and contact page link for inquiries.                                                                                                                        |
| The Site Map       | `/sitemap`     | The Site Map page with categorised for main pages, resources, brawler content, gamemodes to improve site navigation experience.                                                                                                                                           |
| Page Not Found     | `/404`         | 404 error page with custom error message, navigation buttons back to homepage or site map, expandable technical details that has a copy report feature and a link to support page.                                                                                        |

**Backend Functionalities of the Site**

| What is it            | What does it do?                                                                                                                                                                                                                                                                                                                                                                                                          |
| --------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| Search Configurations | A search_config.py file was made to store the searchable website pages in search.html which includes keywords, descriptions, and input sanitisation. This allows quick access to adding new search items into the search engine without modifying other components. <br><br> Related to: [Search Configurations](./routes/search/search_config.py), [Search Page](./templates/search.html) and [app.py File](./app.py)    |
| Search Services       | A search_service.py file was made to handle user input sanitisation based on what chars is allowed, finding the exact pages to immediately redirects, finding the keyword-based results and page routes for redirects. Using /search?q= to receive values to process. <br><br> Related to: [Search Services Route](./routes/search/search_service.py), [Search Page](./templates/search.html) and [app.py File](./app.py) |

**Small and Major Codebase Architectural Change!**

| What is it               | What changed?                                                                                                                                                                                                                                                                                                                                                                                                                                                          |
| ------------------------ | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| Flask Blueprints         | The original app.py was refactored into multiple separate Flask Blueprints, organised into modules for main pages, brawlers, gamemodes, guides, search and error handling. This allows the code to be much more maintainable, and reduces the code size of app.py. <br> <br> Related Pages: [Routes Folder](./routes) and [app.py File](./app.py)                                                                                                                      |
| Static Code Organisation | The static assets were restructured into organised categories each for CSS, JavaScript, images, videos and licenses. Site wide styling and code were separated from page-specific resources, while images and media were placed into relevant folders to improve maintainability. <br> <br> Related Pages: [Static Folder](./static/), [Static CSS](./static/css/), [Static JS](./static/js/), [Static Video](./static/videos/), [Static Licenses](./static/licenses/) |

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

<!--
This section was kept for personal archival purposes and as a cool previous archive of what it used to look like.

My Primary Pages

| Pages             | What it has delivered                                                                                                                                                                                                   |
| ----------------- | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| The Homepage      | The homepage comes with a hero video that greets the user, and as they scroll down, they see a small fade in effect, key pages in the site in cards, what else they can do on the website and a simplified options list |
| The Contacts Page | The contacts pages shows a Google Maps iframe, a email and location, a form the user can submit inquiries, bug reports, and more!                                                                                       |
| The Brawlers Page | The page shows the different rarities of brawlers with a anchor that redirects them to a category of brawlers in the rarity group with each having a image and a gradient overlay to make each more unique :D           |
| The Search Page   | The search page provides a list of values you have searched for, and when you search a page that doesn't exists, it provides you other follow up actions you can take.                                                  |
| The About Page    | The page shows what we are trying to do at Brawlable and a simplified design with a follow up action the user can take!                                                                                                 |


Other Significant Pages

| Pages            | What it has delivered                                                                                                                                                                                                          |
| ---------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
| The Attributions | The attribution pages lists all the python dependencies, content and assets used throughout the website. They also provide a hyperlink to the project and have a static licenses file to view all the licenses in the project  |
| The Privacy Page | This page tells how Brawlable handles user data and offers a redirect link on what the user can do if they have more questions.                                                                                                |
| The Sitemap Page | This page provides a universal link to all the pages across the website that are active and in use :)                                                                                                                          |
| The Support Page | This just does a 302 temporary redirect to the contacts page in short :P                                                                                                                                                       |
| The Not Found    | This page shows a 404 error when the user goes to a page that does not exist. It provides buttons to head back to home or the sitemap, an error code with a timestamp and page location that can be copied right into support. |

Small Codebase Architectural Changes

| What is it       | What changed?                                                                                                                                                                                                                                     |
| ---------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| Flask Blueprints | The app.py has been separated into different flask blueprints that you can find in the program                                                                                                                                                    |
| Search Configs   | The search configurations contains what type of text is allowed in the input to sanitize the input and searches in its list of files if there are matches to what the user wants from exact and keywords with the followup description and title. |
| Search Services  | The search_config.py file handles redirecting people immediately to the page if match exactly or sending the data to search.html if its general or not found.                                                                                     |
| Static Files     | The static file has been separated into files named css js videos and licenses with css and js having a additional section-css or section-js to indicate its not global and is section specific to a page. search                                 |
-->
