# Fitness Forge
Developer: Fabian Meister

Deployed Site: https://fitness-forge-a4f5eb7ec202.herokuapp.com/ 

This Django based fictional e-commerce application is the result of the last of five portfolio projects required for Code Institute.

FitnessForge is an online store dedicated to adventure seekers and fitness enthusiasts. Offering a unique selection of adventures, fitness try-outs, and tournaments. FitnessForge sells these experiences as vouchers, perfect for gifting or personal use. A standout feature is the 'Mystery Box,' which evaluates the total value of your purchase and adds complimentary mystery boxes to your order, enhancing the excitement and value. The website includes a user-friendly comment section on each product and a comprehensive FAQ section to assist shoppers. Registered users can log in to save their data, manage orders, access a personalized wishlist, and subscribe to a newsletter for the latest updates and offers. FitnessForge is designed to cater to both the seasoned athlete and the casual adventurer, providing an engaging and interactive shopping experience.

## Table of Contents
- [UI/UX](#uiux)
  - [Agile](#agile)
  - [Wireframes](#wireframes)
  - [Site Goals](#site-goals)
  - [5 Planes of UX](#5-planes-of-ux)
  - [Visual Design Choices](#visual-design-choices)
  - [SEO and Marketing](#seo-and-marketing)
- [Features](#features)
  - [Existing Features](#existing-features)
  - [Future Features](#future-features)
- [Database Design](#database-design)
  - [Database Model](#database-model)
  - [Custom Model](#custom-model)
  - [CRUD](#crud)
- [Technologies Used](#technologies-used)
  - [Work Environments and Hosting](#work-environments-and-hosting)
  - [Python Libraries](#python-libraries)
  - [Django Libraries](#django-libraries)
  - [Payment processing](#payment-processing)
  - [Emails/Newsletter](#emailsnewsletter)
  - [SEO/Marketing](#seomarketing)
- [Testing](#testing)
  - [Test Guide](#test-guide)
  - [Validator Testing](#validator-testing)
  - [Browser Testing](#browser-testing)
  - [Fixed Bugs](#fixed-bugs)
  - [Unfixed Bugs](#unfixed-bugs)
- [Deployment](#deployment)
  - [Development](#development)
    - [Fork](#fork)
    - [Clone](#clone)
    - [Download ZIP](#download-zip)
- [Source Credits](#source-credits)
  - [References/Documentation/Tutorials](#referencesdocumentationtutorials)
  - [Media and Styling](#media-and-styling)
  - [Content/Data](#contentdata)

## UI/UX
### Agile Methodology - User Stories
The realization of this project has been accomplished with the use of agile methodology. In order to visualize user stories and tasks as well as overall project progress, GitHub Projects has been used. GitHub Projects sees itself as “an adaptable, flexible tool for planning and tracking work on GitHub”.

The user stories were created including a speaking title, acceptance criteria and required tasks. They were also prioritized in order to give a visual indication on which user stories to focus on first, with P0 being a “Must Have”, P1 being a “Should Have” and P2 being a “Nice to Have”.

During the project the most commonly used views have been the “Backlog”, the “Priority board” and “My items”. Those have been adjusted to suit the need of a clear visibility of tasks and a good overview on the overall project progress. All others template views have been removed.

#### Backlog View
![image-20240504-152337](https://github.com/FabiMe/Fitness-Forge/assets/136444209/99a0196b-fb6f-458a-a0b8-7bdf4d7a7533)

#### Priority board
![image-20240504-152545](https://github.com/FabiMe/Fitness-Forge/assets/136444209/ce9f3d84-3dd4-427f-8ad7-6ec314088606)

#### My items View
![image-20240504-152704](https://github.com/FabiMe/Fitness-Forge/assets/136444209/a9dc86c2-eee2-4619-b8e4-8ec3bf906411)


Generally speaking the realization of the project was a continuous process of planning, prioritizing implementing and testing functionalities covered in the user stories.
The GitHub Projects can be accessed via: https://github.com/users/FabiMe/projects/6 

### Wireframes
Wireframes are simplified, rough sketches of the basic structure of the website. Wireframes are created in an early state and should but might not cover all crucial functionalities and structures of the websites pages.  To create the wireframes of this project Figma has been used: 
https://www.figma.com/file/QoQR6UBFHRPp7QnKICRWo0/Low-fi-Wireframe-Template-(Community)?type=design&node-id=576%3A1879&mode=dev&t=7Yd8G1LpaSzCgQu2-1

* Home
* Products Page
* Product Details Page
* Shopping Bag
* Checkout
* Order History
* Account/Profile
* Login/Register
* FAQ

### Site Goals
The Fitness Forge Website aims to provide a seamless shopping experience for fitness adventures. It enables users to register for fitness events easily and offers a platform where users can plan future fitness adventures for themselves and others. Fitness Forge aims to maintain and improve general health and physical fitness and to elevate the customers skills.

Users can select adventures and events from the categories CATEGORIES

Once the user selects a specific adventure or event, he/she can adjust the quantity and personalize each adventure's attendees individually. The possibility to purchase adventures for multiple attendees makes the website to an ideal place to search for gifts and presents.

### 5 Planes of UX
- **Strategy Plane:** The project identified a clear need to create an e-commerce platform specifically for fitness enthusiasts. This insight guided the development process, ensuring the platform would attract and meet the demands of its target demographic.
- **Scope Plane:** The project’s functional requirements were clearly defined to include a dynamic product catalog that allows for regular updates and additions, comprehensive user account functionalities, a robust event registration system to handle various fitness activities, and interactive comment features enabling community engagement.
- **Structure Plane:** The design of the information architecture was a critical step, carefully planned to provide intuitive navigation and a logical flow of information. This framework supports users in finding and interacting with the content they need without unnecessary complexity or confusion.
- **Skeleton Plane:**  In designing the interface, attention was paid to the arrangement of interface elements to optimize the overall user experience. This included thoughtful placement of navigation bars, product listings, and interactive elements to ensure high usability and easy access for all users, particularly considering diverse accessibility needs.
- **Surface Plane:**  To finalize the platform's design, high-fidelity prototypes were crafted, focusing on a sleek, user-friendly interface that appeals to the modern consumer. These prototypes were instrumental in refining both the visual appeal and the functional layout, with a particular emphasis on ensuring a responsive, mobile-first design that performs well across various devices and screen sizes.

### Visual Design Choices
Based on the nature of the products and the target group, the overall design and the color scheme aim to reflect a modern and clean approach. The imposing, high quality product images are used to attract the target audience over visual input rather than an information overload.

The color scheme uses a monochromatic theme (different shades of grey) with vibrant accents (green, light blue) to invoke energy and action. It relates to the “outdoor nature” of the product and the target group. For action components, green, blue and light blue accents pick up on a modern approach and additionally attract a young and active target group.

The UI uses a monochromatic theme with vibrant accents to invoke energy and action, suitable for a fitness brand.Responsive design practices ensure usability across devices.

Typography involves a combination of Lato - the main font used - for readability and bold, motivational call-to-actions and thus supports the idea of a minimalistic, clean look and feel.

Responsive design practices ensure usability across devices.

### SEO and Marketing

Initial Brainstorming of General Categories and short-termed and long-termed Keywords

| Sport                  | Adventures               | Health                |
|------------------------|--------------------------|-----------------------|
| Special sports         | sport centric            | Food                  |
| Tennis                 | outdoor adventure        | Recipe                |
| Judo                   | Survival adventure       | Food and health classes |
| Martial Arts Experience| Skateboard trip          | Fitness retreat       |
| lace up your sneakers  | push your limits         | Fitness bootcamp      |
| Table Tennis           | Embark on a journey      | Workshop              |
| Amateur Tournaments    | rush of adrenaline       | Thrills, Skills & Nature |
| Rock Climbing          | breathtaking             |                       |
| Dive into Excellence   | unforgettable adventure  |                       |
| Try-out                | Hike the Majestic Trails |                       |
| Climbing               | Panoramic Overlooks      |                       |
| Basketball             | Fly and Stay Packages    |                       |
| Soccer                 | water adventures         |                       |
|                        | Ride the wind            |                       |
|                        | Elevate Your Performance |                       |
|                        | Discover sport           |                       |
|                        | Forge your path with us  |                       |

## Research of initial keyword collection in Google Search
- After an extensive research using Google Search’s built-in functionalities such as autocomplete proposals, the “People also ask” and the “Related Searches” section, the following keywords have been identified to be most relevant and promising in terms of SEO:

| Sport                  | Adventures               | Health                   |
|------------------------|--------------------------|--------------------------|
| Boost your Skills      | Outdoor Adventure        | Food and Health Classes  |
| Martial Arts Experience| Survival Adventure       | Fitness Retreat          |
| Amateur Tournaments    | Breathtaking             | Fitness Bootcamp         |
| Rock Climbing          | Unforgettable Adventure  | Thrills, Skills & Nature |
| Discover Sport         | Panoramic Overlooks      |                          |
| Elevate your Performance| Adrenaline Rush         |                          |
|                        | Ride the Wind            |                          |

## Determination of keyword volume and competition
- Using www.wordtracker.com keyword volume and competition have been determined for some of the refined keyword ideas:
![image-20240504-181130](https://github.com/FabiMe/Fitness-Forge/assets/136444209/005e9cff-5a88-4968-a4f0-d6896d8356ba)
![image-20240504-181632](https://github.com/FabiMe/Fitness-Forge/assets/136444209/5e18e49b-7442-4cd1-9bad-d5474e965759)
![image-20240504-181849](https://github.com/FabiMe/Fitness-Forge/assets/136444209/89dfef34-2aa3-459a-9967-536c710fa2db)
![image-20240504-181456](https://github.com/FabiMe/Fitness-Forge/assets/136444209/1f547870-f001-4d98-b1a3-93eca333b2fc)

## SEO Implementations in HTML

Effective Search Engine Optimization (SEO) is critical for improving visibility and ensuring that your content reaches its intended audience. Below are the key SEO strategies implemented within the HTML structure of the website.

### Use of Semantic HTML Elements
- On both the homepage and product detail pages, we've strategically placed relevant keywords within headings and emphasized them using `<strong>` or `<em>` tags, carefully avoiding the practice of "keyword-stuffing."

### Images
- Image SEO has been enhanced by enriching the `alt` attributes of `<img>` tags with relevant keywords, which are crucial for search engines. Additionally, image file names have been renamed to include these keywords to further optimize searchability.

### Descriptive Meta Tags
- Within the `<head>` section of `base.html`, descriptive meta tags including `<meta name="description">` and `<meta name="keywords">` have been added. These tags provide search engines with a concise summary of the page's content and associated keywords.

### XML Sitemap
- An XML sitemap has been created to list important URLs within the website, aiding search engines in understanding the site's structure. This sitemap ensures that all relevant pages are crawled and content is easily discovered. It was generated using an online sitemap generator and is located at the root level of the project.

### Robots.txt
- The `robots.txt` file at the root of the project directory plays a vital role in managing search engine access. It allows search engines to crawl the website freely while specifying directories or files that should not be indexed. This not only helps in managing crawl traffic but also signals the website's quality, potentially improving search rankings.

Implementing these SEO practices is part of our ongoing effort to enhance the accessibility and visibility of our website, ensuring that our content reaches its target audience efficiently.

## Features
### Existing Features


### Future Features
- **Virtual Try-On:** Integrate AR technology to allow users to visualize products.
- **Mobile App:** Develop a mobile app to enhance access and push notifications.

## Database Design
### Database Model

![fitness_forge_models (1)](https://github.com/FabiMe/Fitness-Forge/assets/136444209/8fe31ed1-c421-4e26-b61f-7b4939f8ba3d)

- to create a Automatically Generated ERD Model are following steps crucial.

- Uses Django's ORM with PostgreSQL. Models include:
![image](https://github.com/FabiMe/Fitness-Forge/assets/136444209/722508d2-8890-47cf-91c3-ca3d77275d05)

- This will create the bellow files and directories.

![image](https://github.com/FabiMe/Fitness-Forge/assets/136444209/1f2af177-121c-45f0-93da-7ca0dacf2b32)

- Create a blog application

![image](https://github.com/FabiMe/Fitness-Forge/assets/136444209/e4a67d91-5ef6-4cbd-b449-4a478b81a0bf)

- install Django

![image](https://github.com/FabiMe/Fitness-Forge/assets/136444209/6822922e-6758-40b7-a0c3-de2383178b84)

- in blog/models.py 

![image](https://github.com/FabiMe/Fitness-Forge/assets/136444209/9eced74b-9261-4679-a4c5-6da9f4775541)

- in mysite/settings.py

![image](https://github.com/FabiMe/Fitness-Forge/assets/136444209/1d81af87-8c66-4e4d-a954-0f7e83e071db)

- Run the project and migrate the models

![image](https://github.com/FabiMe/Fitness-Forge/assets/136444209/b61c960f-f4e6-49dd-ad18-d445d32b06e4)

- install django-extensions 

![image](https://github.com/FabiMe/Fitness-Forge/assets/136444209/28514a57-5779-4805-85df-042cbdd95753)

- Setup the package

![image](https://github.com/FabiMe/Fitness-Forge/assets/136444209/c575987d-5557-4187-ba43-c6a8c64a3920)

- Generate ERD Model

![image](https://github.com/FabiMe/Fitness-Forge/assets/136444209/fefc1cc8-80c8-4355-bb55-a4050780b991)


## Custom Models

This section describes the three custom models implemented in the platform, each designed to enhance user interactivity and provide essential features to both users and admins. The models are segmented into individual apps with their own URLs and views to maintain clarity and modularity.

### 1. Comment Model

- **Purpose:** Allows users to leave comments on product detail pages, fostering a community-driven environment where users can share opinions and feedback.
- **Functionality:** Users can submit comments directly on a product’s detail page. Each comment is stored and displayed after submission, pending visibility settings or moderation if needed.

### 2. FAQ Model

- **Purpose:** Provides a section for frequently asked questions where users can seek answers and submit their own questions.
- **Functionality:** Users can submit questions to the FAQ section. Submitted questions are not immediately visible; they require admin approval before being displayed publicly. This ensures that all information in the FAQ is accurate and relevant.

### 3. Wishlist Model

- **Purpose:** Enables users to add products to a wishlist, allowing them to save their favorite items for later purchase or review.
- **Functionality:** Users can add products to their wishlist from the product details page. This wishlist is accessible via the user’s profile, where they can view, edit, or remove items as desired.

### Architecture

Each of these models is housed in its own dedicated app within the Django project structure, including separate `models.py`, `views.py`, and `urls.py` files. This design approach:

- **Enhances Maintainability:** Isolating functionality into separate apps makes the codebase easier to manage and debug.
- **Improves Scalability:** As the platform grows, each app can be scaled or modified independently without affecting others.
- **Simplifies Testing:** Individual apps can be tested in isolation, ensuring that each component functions correctly before integration.

By using this modular architecture, the platform ensures that it remains both flexible and robust, catering to the evolving needs of its users while maintaining a clear organizational structure.

## CRUD Operations

This section outlines the Create, Read, Update, and Delete (CRUD) capabilities for both regular users and administrators within the platform.

### Create

- **Users:**
  - Can create accounts to personalize their experience.
  - Can add products to their shopping cart.
  - Can register for events to participate in various activities.

- **Admins:**
  - Have the ability to create new products to keep the catalogue up-to-date.

### Read

- **Users:**
  - Can browse all available products.
  - Can read comments from other users on products, gaining insights and feedback.

- **Admins:**
  - Can view all existing products, overseeing the complete range of offerings.

### Update

- **Users:**
  - Can update their profile information to keep their personal data current.
  - Can modify their orders, making changes to their purchases as needed.

- **Admins:**
  - Can update product details to reflect changes such as pricing adjustments, descriptions, or stock levels.

### Delete

- **Admins:**
  - Can remove outdated products to maintain a fresh and relevant product line.
  - Can delete FAQs that are no longer applicable or update them to reflect current information.
  - Can remove inappropriate or obsolete user comments to maintain a positive and useful community discourse.

Each of these operations supports the platform's functionality and enhances the user experience, ensuring both usability and administrative control.

## Technologies Used

This section categorizes the major dependencies of the project to provide a clear understanding of each component's role within the application.

### Web Framework and Extensions
- **Django==3.2.25** - The core web framework.
- **django-extensions==3.2.3** - Custom extensions for Django.
- **django-storages==1.14.2** - A collection of custom storage backends for Django.
- **django-crispy-forms==1.14.0** - Controls the rendering behavior of Django forms.
- **django-allauth==0.41.0** - Integrated set of Django applications for authentication.
- **django-countries==7.6.1** - Provides a country field for models.

### Database and Data Processing
- **dj-database-url==0.5.0** - Utility to configure the Django database using a URL.
- **psycopg2-binary==2.9.9** - PostgreSQL adapter for Python.
- **sqlparse==0.4.4** - A non-validating SQL parser for Python.

### Authentication and Security
- **oauthlib==3.2.2** - A generic, spec-compliant library for OAuth.
- **python3-openid==3.2.0** - Python 3 library for OpenID.
- **defusedxml==0.7.1** - XML library for preventing XML attacks.

### Network and HTTP Utilities
- **gunicorn==22.0.0** - WSGI HTTP server for UNIX.
- **requests==2.31.0** - Elegant and simple HTTP library for Python.
- **requests-oauthlib==2.0.0** - OAuthlib authentication support for Requests.
- **urllib3==2.2.1** - HTTP client for Python.
- **idna==3.7** - Supports the Internationalized Domain Names in Applications (IDNA) protocol.

### AWS and File Handling
- **boto3==1.34.98** - Framework for AWS API interactions including S3 storage.
- **botocore==1.34.98** - Low-level interface to a growing number of Amazon Web Services.
- **s3transfer==0.10.1** - Amazon S3 Transfer Manager for Python.

### Image and Data Visualization
- **pillow==10.3.0** - The Python Imaging Library adds image processing capabilities.
- **pydotplus==2.0.2** - Python interface to Graphviz's Dot language.

### Utilities and Miscellaneous
- **asgiref==3.8.1** - ASGI toolkit for Django.
- **certifi==2024.2.2** - Required for SSL certificate validation.
- **charset-normalizer==3.3.2** - Helps in character encoding normalization.
- **packaging==24.0** - Core utilities for Python packages.
- **python-dateutil==2.9.0.post0** - Provides powerful extensions to the datetime module.
- **pytz==2024.1** - World timezone definitions for Python.
- **stripe==9.2.0** - Library for Stripe API interactions.
- **typing_extensions==4.11.0** - Backported and experimental type hints for Python.

## Emails & Newsletter Management

- **Gmail**: Utilized for email dispatching, handling direct communications and customer service interactions.
- **Mailchimp**: Manages newsletter subscriptions, allowing us to effectively distribute marketing materials and updates to subscribers.

## SEO, Marketing & Content Creation Tools

- **XML Sitemaps**: Generates sitemaps to help search engines better crawl and index our website.
- **Privacy Policy Generator**: Used to create a compliant privacy policy that meets international standards.
- **Wortracker**: Assists in keyword volume and competition research to optimize our SEO strategies.
- **Chat-GPT**: Employs advanced AI for content creation, enhancing our blog posts, product descriptions, and marketing copy.

## Work Environments and Hosting

- **AWS (Amazon Web Services)**: Hosts static and media files using S3 storage, ensuring fast and secure access to our digital assets.
- **Figma**: Used for creating wireframes and designing the user interface, providing a blueprint for the website’s visual and functional elements.
- **Git**: Serves as our version control system, enabling efficient tracking of code changes and collaboration among developers.
- **GitHub**: Acts as the repository for storing, managing, and sharing the project’s codebase.
- **GitPod**: Provides an online VS Code editor for remote development. Optionally, VS Code was used for coding the website locally.
- **Heroku**: Hosts the main site, offering a platform for deploying and managing the live website.


## Testing
### Test Guide


### Validator Testing


### Browser Testing


### Fixed Bugs


### Unfixed Bugs

## Deployment and Configuration

### Deployment on Heroku
This project is deployed on Heroku, utilizing the following steps and tools:

1. **Installation of Necessary Libraries**:
   - Install psycopg2 and dj_database_url for PostgreSQL connectivity:
     ```bash
     pip3 install dj_database_url psycopg2
     ```
   - Install Gunicorn, the server for running Django on Heroku:
     ```bash
     pip3 install django gunicorn
     ```

2. **Requirements.txt**:
   - Generate the `requirements.txt` file to list all necessary dependencies:
     ```bash
     pip3 freeze > requirements.txt
     ```
   - Commit and push these changes to GitHub.

3. **Sensitive Information**:
   - Ensure all sensitive credentials are stored in an `env.py` file and excluded from Git tracking by including this file in `.gitignore`.
   - Set environment variables in `env.py`:
     ```python
     import os
     os.environ["DATABASE_URL"] = "<copied_database_url>"
     os.environ["SECRET_KEY"] = "your_secret_key"
     ```

4. **Creating Heroku App**:
   - Log into Heroku, navigate to the dashboard, create a new app with a suitable name and region.

5. **Stripe Setup**:
   - Configure Stripe keys in the `env.py` file and set up webhooks for transaction handling.

### AWS Setup
1. **S3 Bucket Configuration**:
   - Create an S3 bucket in the AWS Management Console with appropriate settings for public access and static website hosting.
   - Configure CORS to allow specific types of requests:
     ```json
     [
       {
         "AllowedHeaders": ["Authorization"],
         "AllowedMethods": ["GET"],
         "AllowedOrigins": ["*"],
         "ExposeHeaders": []
       }
     ]
     ```
   - Set up the bucket policy and ACL for public read access and list permissions.

2. **IAM Configuration**:
   - Create a user group and define permissions policies to grant the necessary access to the S3 bucket.
   - Create a user, attach the user to the group, and save the credentials for accessing AWS resources.

### Database Configuration
- **dbs.ci-dbs.net**:
  - Utilize dbs.ci-dbs.net for database hosting, connecting via the URL provided during setup.


## Repository Management

This section guides you through the processes of forking, cloning, and downloading the repository from GitHub.

### Forking a Repository
Forking a repository allows you to create a personal copy of another project on GitHub without affecting the original. Here’s how to fork a repository:

1. **Navigate** to the repository on GitHub.
2. **Locate** the “Fork” button in the top-right corner of the page and click it.
3. **Adjust** the name of the fork and add a description if necessary.
4. **Choose** which branches you want to copy (main branch or all branches).
5. **Click** "Create a Fork". The new repository will now appear in your GitHub account and can be cloned or modified as needed.

### Cloning a Repository
Cloning a repository creates a local copy on your machine, linked to the original repository. Changes pushed from this clone can affect the original repository if you have the necessary permissions.

1. **Navigate** to the repository on GitHub.
2. **Locate** the “Code” drop-down button above the file list.
3. **Select** your preferred method for copying the repository URL (HTTPS, SSH, or GitHub CLI).
4. **Open** Git Bash or your preferred terminal and navigate to the desired directory where you want the repository to be cloned.
5. **Type** `git clone`, followed by the copied URL.
6. **Press** “Enter” to create the local clone.

### Downloading a Repository as a ZIP
Downloading a repository as a ZIP file is useful for obtaining a snapshot of the project to run locally without git tracking.

1. **Navigate** to the repository on GitHub.
2. **Locate** the “Code” drop-down button above the file list.
3. **Select** “Download ZIP”.
4. **Extract** the ZIP file in your local environment to begin working with the files.

Each method serves different purposes—forking for personal modifications without affecting the original, cloning for direct contributions back to the original repository, and downloading for quick access or testing without version control.


Hero image : https://www.pexels.com/de-de/foto/mann-halt-braunes-seil-3253501/
Pine Ridge https://www.pexels.com/de-de/foto/weisser-schneeberg-nahe-grasfeld-733848/
Yosemite National Park https://www.pexels.com/de-de/foto/wald-in-der-nahe-von-gewassern-533881/
Blue Horizon Resort! https://www.pexels.com/de-de/foto/zwei-leute-die-einen-jet-ski-fahren-1430676/
AquaVista Resort https://www.pexels.com/de-de/foto/buckelwale-unter-wasser-4666753/
 Kitesurfing https://www.pexels.com/de-de/foto/man-kite-surfen-1604869/
 Wildwood heaven https://www.pexels.com/de-de/foto/landschaft-natur-sonnig-ferien-4268158/
 Aurora https://www.pexels.com/de-de/foto/person-auf-weissem-schneefeld-1693085/
 Basketball https://www.pexels.com/de-de/foto/mann-der-sprungschuss-tut-1905009/
 Rock climbing https://www.pexels.com/de-de/foto/person-klettern-3077882/
 Judo https://www.pexels.com/de-de/foto/stehen-sportler-kampfer-meister-6253307/
 Tennis https://www.pexels.com/de-de/foto/tennisball-auf-tennisschlager-auf-dem-boden-209977/
 Table tennis https://www.pexels.com/de-de/foto/selektives-fokusfoto-von-tischtennisball-und-tischtennisschlager-976873/
 mma https://www.pexels.com/de-de/foto/sport-stehen-ausbildung-boxen-8612504/
 bootcamp https://www.pexels.com/de-de/foto/manner-sport-fahrrader-gruppe-8766378/
 wellness https://www.pexels.com/de-de/foto/frau-meditiert-mit-kerzen-und-weihrauch-3822864/
 health and fitness https://www.pexels.com/de-de/foto/foto-des-gemusesalats-in-schalen-1640770/
 survival package https://www.pexels.com/de-de/foto/mann-der-lagerfeuer-am-wald-pruft-207324/
 deals https://www.pexels.com/de-de/foto/graustufenfotografie-von-verschiedenen-kleidungsstucken-auf-regalregal-1884581/
 Diving https://www.pexels.com/de-de/foto/mann-der-kurzes-tauchen-der-weissen-und-roten-tafel-von-der-felsformation-tragt-1378406/
 soccer https://www.pexels.com/de-de/foto/himmel-sonnenuntergang-feld-sonnenaufgang-114296/
 Tennis try out https://www.pexels.com/de-de/foto/gesund-mann-draussen-verwischen-5067813/
 healthy food https://www.pexels.com/de-de/foto/vielzahl-von-gerichten-1640771/
 summit& Surf https://www.pexels.com/de-de/foto/meer-natur-felsen-kuste-19074622/
skate trip https://www.pexels.com/de-de/foto/mann-der-einen-skateboard-trick-tut-1769553/

 banner für topnav https://www.pexels.com/de-de/foto/braune-holzplatte-139309/
 newsletter https://www.pexels.com/de-de/foto/foto-der-person-die-auf-schotterstrasse-lauft-1821694/
 sumit&surf https://www.pexels.com/de-de/foto/person-surfen-416676/