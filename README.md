# Brawlable

| Field                          | Detail                                                                                 |
| ------------------------------ | -------------------------------------------------------------------------------------- |
| **Website Title**              | Brawlable                                                                              |
| **Student Name(s)**            | Callen Lin                                                                             |
| **Class / Course**             | Year 9 Computer Technology                                                             |
| **Repository**                 | https://github.com/TempeHS/2027CT_myFlaskSite_Callen.L                                 |
| **Live Site / Codespaces URL** | v1.0.0 https://github.com/TempeHS/2027CT_myFlaskSite_Callen.L/releases/tag/v1.0.0 |
| **Date**                       | Last Edited on the 31st of July 2026 :D                                                |

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

| Field            | Detail                                                                          |
| ---------------- | ------------------------------------------------------------------------------- |
| **Link / Embed** | https://github.com/user-attachments/assets/bd304338-b4bb-4667-992f-d50daaf1ad87 |
| **Duration**     | 1 minute 50 seconds                                                             |

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

> [!IMPORTANT]
> The site has numerous href="#" or working in progress pages.  
> The reason is that I find it unfeasible to collect all assets and designs necessary to rebuild something towards a wiki platform.

> **Example of pages with content completed includes "brock" which you can search**

**My Primary Pages**
| Pages | Route | What it has delivered |
| ---------------- | ----------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| The Homepage | `/` | Homepage with a Bootstrap navbar and dropdown menu, 82vh hero video with mute/un-mute button using Bootstrap Icons and a call-to-action text, greetings section, three features topic cards (Brawlers, Gamemodes, Mechanics), six advanced strategy cards using Bootstrap Cards and Icons, two feature cards with game modes (Ranked or Trophy), and a footer. |
| The Contact Page | `/contact` | The Contact page featuring an embedded Google Map and a responsive Bootstrap contact form with fields for name, email address, and message. |
| The Brawler Page | `/brawlers` | The Brawler Page with six Bootstrap cards organised by rarity, each featuring a image, a gradient overlay, a description and a navigation button to each of the individual Brawler categories. |
| The Search Page | `/search` | The Search Page has a dynamic search results displaying titles and descriptions, and suggested navigation links when no matching results found. |
| The About Page | `/about` | About Us shows the website's missions, using Bootstrap card and grids, information explaining the purpose of the website, a call-to-action link to the onboarding page. |

**Other Significant Pages**

| Pages              | Route            | What it has delivered                                                                                                                                                                                                                                                                                                                                                       |
| ------------------ | ---------------- | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| The Attributions   | `/attribution`   | The Attribution page features quick id navigation shortcuts on the top, organised acknowledgement for Python Dependencies, third-party repos, content sources and project contributors. It also includes direct links to the external program and LICENSE files attached.                                                                                                   |
| The Privacy Policy | `/privacy`       | The Privacy Policy page outlines how the website collects data, cookies, third-party services, policy updates and contact page link for inquiries.                                                                                                                                                                                                                          |
| The Site Map       | `/sitemap`       | The Site Map page with categorised for main pages, resources, brawler content, gamemodes to improve site navigation experience.                                                                                                                                                                                                                                             |
| Page Not Found     | `/404`           | 404 error page with custom error message, navigation buttons back to homepage or site map, expandable technical details that has a copy report feature and a link to support page.                                                                                                                                                                                          |
| Rare Brawler Pages | `/brawlers/rare` | Includes a horizontal scrolling Brawler selector for quick visual navigation, followed by a responsive Bootstrap card grid displaying each Rare Brawler with their image, description and navigation link to their individual guide page.<br><br><b>There is also visible buttons on a mobile interface which is typically hidden on Desktop and Tablet sized displays.</b> |

**💻 Backend Functionalities of the Site**

| What is it            | What does it do?                                                                                                                                                                                                                                                                                                                                                                                                          |
| --------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| Search Configurations | A search_config.py file was made to store the searchable website pages in search.html which includes keywords, descriptions, and input sanitisation. This allows quick access to adding new search items into the search engine without modifying other components. <br><br> Related to: [Search Configurations](./routes/search/search_config.py), [Search Page](./templates/search.html) and [app.py File](./app.py)    |
| Search Services       | A search_service.py file was made to handle user input sanitisation based on what chars is allowed, finding the exact pages to immediately redirects, finding the keyword-based results and page routes for redirects. Using /search?q= to receive values to process. <br><br> Related to: [Search Services Route](./routes/search/search_service.py), [Search Page](./templates/search.html) and [app.py File](./app.py) |

**🙋‍♂️ User Experience Additions**

| What is it                   | What does it do?                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                         |
| ---------------------------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| Accessibility Features       | The website includes accessibility considerations such as image alt text with detailed description on what is visible on the image, ARIA labels for interactive controls, and support for users who prefer reduced motion. These improvements make the website easier to use for those with assistive technologies. <br><br> Relates to: [Homepage](./templates/index.html), [Rare Brawlers](./templates/brawlers/rare.html), [Global Styles](./static/css/global-styles.css) and many more.                                                                                                                                                             |
| Back to Top Button           | A floating Back to Top button fades in from the bottom-right corner after the user scrolls more than 200 pixels. Selecting it smoothly scrolls the user back to the top of the page, after which the button ease out. <br><br> Related to: [base.js](./static/js/base.js) and [global-styles.css](./static/css/global-styles.css)                                                                                                                                                                                                                                                                                                                        |
| Brand and Logo to Homepage   | Clicking the Brawlable logo or brand name in the navigation bar or footer returns the user to the homepage, providing a familiar navigation shortcut. [Navigation Bar](./templates/partials/nav.html) and [Footer Bar](./templates/partials/footer.html)                                                                                                                                                                                                                                                                                                                                                                                                 |
| Card Hover Animation         | Cards provide a hover animation that slightly raises the card and adds a shadow effect, giving users visual feedback when interacting with different content. <br><br> Relates to: [Global-styles.css](./static/css/global-styles.css)                                                                                                                                                                                                                                                                                                                                                                                                                   |
| Hero Video Overlay           | The Hero video has a overlay of rgba(0, 0, 0, 0.35) which allows the text on the hero video to be easier to read. <br><br> Related to: [Hero Video in Homepage](./templates/index.html) and [Overlay CSS](./static/css/section-css/hero-section.css)                                                                                                                                                                                                                                                                                                                                                                                                     |
| Loading Text for Hero        | If the hero video takes more than 2 seconds to load, the website displays an animated loading message to inform the user that the video is still loading. If loading fails, an error message is displayed instead, preventing confusion caused by a blank hero section. <br><br> Related to: [Hero Video in Homepage](./templates/index.html) and [Loading Text JS](./static/js/section-js/hero-video.js)                                                                                                                                                                                                                                                |
| id Attribute Heading Spacing | There is a small 65px scroll-margin-top buffer to counteract the heading being covered by the fixed-top attribute on the navigation bar. It is specifically slightly larger than Bootstrap NavBar default size. <br><br> Relates to: [Global Styles CSS](./static/css/global-styles.css)                                                                                                                                                                                                                                                                                                                                                                 |
| Instant Search Redirect      | `find_exact_match_endpoint()`checks whether the sanitised search query exactly matches a configured page in`search_config.py`. If a match is found, the user is redirected directly to that page instead of first viewing the `search.html` page. <br><br> Related to: [Search Configurations](./routes/search/search_config.py), [Search Services](./routes/search/search_service.py) and [Search Page](./templates/search.html)                                                                                                                                                                                                                        |
| Navigation Bar Blur          | After the user scrolls 28 pixels, the navigation bar applies a blur effect to improve readability and visually separate the navigation bar from the page content. <br><br> [Navigation Bar Styles](./static/css/global-styles.css) and [Navigation Bar HTML](./templates/partials/nav.html)                                                                                                                                                                                                                                                                                                                                                              |
| Partial Searches             | `find_partial_matches()`searches page titles, descriptions and keywords for the user's query using partial text matching. For example, searching help returns pages such as Support and Contact because the keyword appears in their searchable content <br><br> Related to: [Search Configurations](./routes/search/search_config.py), [Search Services](./routes/search/search_service.py) and [Search Page](./templates/search.html)                                                                                                                                                                                                                  |
| Hero Video Performance       | The cold visit (1st visit) downloads the 20.2MB video and store it on a local cache using IndexedDB. Then on the second visit, the javascript checks if it has a cache of it and if there is a new one before playing. This further improves future visits the user may do. <br><br> <b># Real world performance values:</b> <br> <b>❄️ Cold Visit (1st visit):</b> <br> LCP: 1.22s // CLS: 0 // INP: 8ms <br> <br><b>🔥 Warm Visit (2nd visit):</b><br>LCP: 0.15s // CLS: 0 // INP: 8ms<br><br>Measured using Google Chrome DevTools 150 Throttling to Slow 4G. <br><br> Relates to: [Video IndexedDB Caching JS](./static/js/section-js/hero-video.js) |
| Theme Detection              | The website uses`prefers-color-scheme` to detect the user's system light or dark theme and automatically applies the matching appearance. This applies not only to the text and background but also some of the colour schemes used in the project. <br><br> Related to: [JavaScript Theme Detection](./static/js/site-theme.js) and [global-styles.css](./static/css/global-styles.css)                                                                                                                                                                                                                                                                 |
| Visible Fade in Effect       | Elements smoothly fade and move into position as the user scrolls through the website, creating a much more polished website. There are different triggers including `fade-in-fx` needing to be fully visible, `fade-in-fx-higher` needing 60% and `fade-in-fx-even-higher` needing 30% fully visible. <br><br> <b>⚠️ This only applies to user without reduce motion enabled!</b> <br><br> Relates to: [Fade in Effects JS](./static/js/fade-in-fx.js) and [Fade in Effect Styles](./static/css/site-fx.css)                                                                                                                                            |

**Small and Major Codebase Architectural Change!**

| What is it               | What changed?                                                                                                                                                                                                                                                                                                                                                                                                                                                          |
| ------------------------ | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| Flask Blueprints         | The original app.py was refactored into multiple separate Flask Blueprints, organised into modules for main pages, brawlers, gamemodes, guides, search and error handling. This allows the code to be much more maintainable, and reduces the code size of app.py. <br> <br> Related Pages: [Routes Folder](./routes) and [app.py File](./app.py)                                                                                                                      |
| Static Code Organisation | The static assets were restructured into organised categories each for CSS, JavaScript, images, videos and licenses. Site wide styling and code were separated from page-specific resources, while images and media were placed into relevant folders to improve maintainability. <br> <br> Related Pages: [Static Folder](./static/), [Static CSS](./static/css/), [Static JS](./static/js/), [Static Video](./static/videos/), [Static Licenses](./static/licenses/) |

> [!NOTE]
> There are much more other features in the website that I didn't have enough time to fully document here!

### 3.3 Evaluation Against Your Intent (2–3 paragraphs)

> Take each aim in your Statement of Intent and evaluate **how well the
> delivered site meets it**. Where did you meet your intent? Where did you fall
> short, and why? Support every judgement with evidence from your site.

Brawlable has achieved its main aim of simplifying the learning curve of the game Brawl Stars for beginners and experienced players sharpening their skills. I have made my guides into short and concise descriptions with clear headings in defined sections that makes information easier to read and understand. For example, the Brock Brawler guide page shows a simple quick overview of his offence, defence and his class followed by his different attacks and his stats at max level. It also provide strategies and builds people can use that helps reduce decision fatigue and start developing their skills. The homepage, brawler category page and search makes it easy for people to find where they want to begin and navigate content that matches their interests!

The site has also achieved its second goal of providing quick, digestible and accessible information for its audience. Featuring a responsive Bootstrap layouts, a search system, breadcrumb navigation, and consistent design in guides makes it easy for users to find information on the go or at their desk. The website is built around the idea that players want a quick explanation or strategy that they can use while playing, so features like back-to-top button and dark mode improves their experience especially on mobile devices.

However, Brawlable unfortunately was not above to achieve the full scope originally planned in the Statement of Intent. The original goal has included covering a large range of Brawlers, Gamemodes and Mechanics, but the amount of content required was significantly larger than expected. Because of this, many pages remain incompleted or use placeholder text. Instead of lowering the quality to complete all the pages, I’ve decided to focus on creating consistency, accessibility and responsiveness throughout the website that allows the site to have future guides and content added much easily.

### 3.4 Overall Effectiveness (1–2 paragraphs)

> Step back from the detail. Overall, **how effective** is the website at
> achieving its purpose for its target audience? Weigh what works against what
> falls short, and state what you would improve to better meet your intent.

Brawlable is a Brawl Stars tutorial website designed for new and experienced players to learn new stuff. The frustrations people experience including me find many existing wikis are not designed for mobile interfaces and the descriptions are often too descriptive and too lengthy for a quick read. This website helps solve that problem with pages such as Brock’s brawler page with content simplified to the key ideas and actionable steps that people can take immediately in a clean interface. The scroll back-to-top button and dark mode makes it great for a quick read and while also reducing eye strain from bright backgrounds in dark places.

Some of the visual features I am most proud of in this project includes the colourful design language, the semi-transparent navigation bar and fade-in-effects the site has around making it feel more alive and not static. Some features I did find is limited is the onboarding where I have not exactly figured out what questions to ask prior to giving a suggestion. If I had more time, I would improve it so it is more personalised depending on your current skill level and what play style you enjoy.

Overall, I think Brawlable has indeed made a tutorial site that both new and experienced players could use on the go, and find it easy to learn new stuff that a typical wiki page may have in different blocks of text. Making Brawl Stars enjoyable just like how it was intended to be!

---

## 4. Acknowledgements

> List anything you did not make yourself — tutorials, images, fonts, icons and
> libraries. Using content without acknowledgement may constitute academic
> misconduct.

> [!IMPORTANT]
> The content below are derived from templates/pages/attribution.html and summarised here.

> You can find each of the individual licenses in static/licenses

| What you used                       | Source / Creator | Licence                          | What you used it for                                  |
| ----------------------------------- | ---------------- | -------------------------------- | ----------------------------------------------------- |
| Bootstrap                           | Bootstrap Team   | MIT                              | Website layout and JavaScript components              |
| Bootstrap Icons                     | Bootstrap Team   | MIT                              | Icons used throughout the website                     |
| Flask                               | Pallets Projects | BSD-3-Clause                     | Web application framework, routing and HTTP requests  |
| Blinker                             | Pallets Projects | MIT                              | Signal broadcasting                                   |
| Click                               | Pallets Projects | BSD-3-Clause                     | Flask command-line utilities                          |
| ItsDangerous                        | Pallets Projects | BSD-3-Clause                     | Secure data signing (Flask dependency)                |
| Jinja                               | Pallets Projects | BSD-3-Clause                     | HTML templating engine                                |
| MarkupSafe                          | Pallets Projects | BSD-3-Clause                     | Safe HTML and XML escaping                            |
| Werkzeug                            | Pallets Projects | BSD-3-Clause                     | WSGI utilities, request/response handling and routing |
| Packaging                           | PyPA             | Apache-2.0                       | Python package management utilities                   |
| Pluggy                              | pytest-dev       | MIT                              | Plugin management for pytest                          |
| Psycopg                             | Psycopg Team     | LGPL-3.0-only                    | PostgreSQL database connectivity                      |
| Pygments                            | Pygments Team    | BSD-2-Clause                     | Syntax highlighting                                   |
| Pytest                              | pytest-dev       | MIT                              | Testing framework                                     |
| CallenLin Python Flask DevContainer | CallenLin        | MIT                              | GitHub Codespaces DevContainer configuration          |
| CallenLin Website Task Project      | CallenLin        | Apache-2.0                       | Footer adapted from previous project                  |
| TempeHS Python Flask DevContainer   | TempeHS          | GPL-3.0                          | Base GitHub Codespaces DevContainer                   |
| Supercell FanKit Assets             | Supercell        | Proprietary (Fan Content Policy) | Images, graphics and other game assets                |
| Brawl Stars Gameplay                | Supercell        | Proprietary (Fan Content Policy) | Gameplay videos and related media                     |
| Brawl Stars Wiki                    | Fandom Community | CC BY-SA                         | Game information and descriptions                     |

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
