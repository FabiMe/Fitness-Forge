# Fitness Forge

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
### Agile
The project follows Agile SCRUM methodology. Regular sprint planning, daily stand-ups, sprint reviews, and retrospectives were conducted. Each sprint lasted two weeks, focusing on delivering a potentially shippable product increment. Trello boards were utilized to manage backlogs and track sprint progress.

### Wireframes
https://www.figma.com/file/QoQR6UBFHRPp7QnKICRWo0/Low-fi-Wireframe-Template-(Community)?type=design&node-id=576%3A1879&mode=dev&t=7Yd8G1LpaSzCgQu2-1

### Site Goals
Fitness Forge aims to:
- Provide a seamless shopping experience for fitness adventures.
- Enable users to register for fitness events seamlessly.
- Offer a platform where users can access personalized fitness advice and community support.

### 5 Planes of UX
- **Strategy Plane:** Identified the need for a e-commerce platform targeting fitness enthusiasts.
- **Scope Plane:** Functional requirements included a dynamic product catalog, user accounts, an event registration system, and blog functionality.
- **Structure Plane:** Information architecture was designed to ensure ease of navigation and logical flow of content.
- **Skeleton Plane:** Interface elements were laid out to optimize the user experience and improve accessibility.
- **Surface Plane:** High-fidelity prototypes were designed to finalize the look and feel, emphasizing mobile-first design.

### Visual Design Choices
The UI uses a monochromatic theme with vibrant accents to invoke energy and action, suitable for a fitness brand. Typography involves a combination of Lato for readability and bold, motivational call-to-actions. Responsive design practices ensure usability across devices.

### SEO and Marketing
A comprehensive SEO strategy focusing on high-traffic keywords related to fitness products was implemented. Google AdWords and Facebook marketing campaigns were initiated to drive traffic and conversion. A monthly newsletter provides value through fitness tips and product updates to subscribed users.

## Features
### Existing Features
- **Product Browsing:** Users can filter products by categories such as "New Arrivals", "Most Popular", and "Sale Items".
- **User Reviews:** Users can submit reviews for products they have purchased.
- **Event Booking:** Users can sign up for upcoming fitness events directly through the site.
- **Admin Panel:** A Django admin panel customized for product and user management.

### Future Features
- **Virtual Try-On:** Integrate AR technology to allow users to visualize products.
- **Mobile App:** Develop a mobile app to enhance access and push notifications.

## Database Design
### Database Model
Uses Django's ORM with PostgreSQL. Models include:
- `User`: Stores user profiles.
- `Product`: Stores product details.
- `Order`: Manages sales transactions.
- `Event`: For managing event details.

### Custom Model
`UserProfile` extends Django's built-in User model to include additional fields like user bio and fitness preferences.

### CRUD
- **Create:** Users can create accounts, add products to their cart, and register for events.
- **Read:** Users can browse products and read other users' reviews.
- **Update:** Users can update their profiles and modify orders.
- **Delete:** Admins can remove outdated products or user accounts.

## Technologies Used
### Work Environments and Hosting
Developed using PyCharm, deployed on Heroku with Amazon S3 for static and media files.

### Python Libraries
- `Django`: The web framework for building the website.
- `Pillow`: For image processing in Django.

### Django Libraries
- `django-allauth`: For authentication, registration, and account management.
- `django-crispy-forms`: To render Django forms in Bootstrap layout.

### Payment processing
Integrated with Stripe and PayPal for handling secure credit card transactions.

### Emails/Newsletter
Configured Django to use SendGrid for transactional emails and newsletters through Mailchimp integration.

### SEO/Marketing
Implemented with Google Analytics for traffic analysis and Yoast for on-page SEO optimization.

## Testing
### Test Guide


### Validator Testing


### Browser Testing


### Fixed Bugs


### Unfixed Bugs

## Deployment
### Development
#### Fork
To fork the repository, click on the 'Fork' button on the repository page on GitHub.

#### Clone
To clone the repository, use the following command:
```bash


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