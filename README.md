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
Fitness Forge was developed using Agile methodologies, with two-week sprints followed by reviews and planning sessions. This allowed for continuous evaluation and incorporation of feedback into the development process.

### Wireframes
Wireframes for Fitness Forge were created using Adobe XD and are accessible [here](https://example.com/wireframes).

### Site Goals
The primary goal of Fitness Forge is to provide a platform where fitness enthusiasts can purchase fitness-related products, sign up for events, and access various fitness services. The site aims to enhance user engagement and streamline the shopping experience.

### 5 Planes of UX
- **Strategy:** Address the needs of fitness enthusiasts for quality gear and reliable fitness advice.
- **Scope:** Functional specifications include e-commerce capabilities, user profiles, and event registrations.
- **Structure:** Information is structured logically with an intuitive navigation system.
- **Skeleton:** Wireframes were used to layout the user interface elements efficiently.
- **Surface:** A modern, clean design with interactive elements enhances user experience.

### Visual Design Choices
The design uses a minimalistic approach with a color palette of blue, gray, and white to promote a sense of calm and professionalism. Fonts like 'Lato' for body text and 'Roboto' for headings are used to ensure readability and aesthetic appeal.

### SEO and Marketing
SEO strategies include the use of structured data, optimized meta tags, and keyword-rich content. Social media campaigns and regular blog posts are used for marketing.

## Features
### Existing Features
- **Product Listing:** Users can browse products categorized by type, price, and rating.
- **User Authentication:** Secure login and registration system for users.
- **Shopping Cart and Checkout:** Integrated with Stripe for payment processing.
- **User Profiles:** Users can view and edit their profiles, and access their order history.

### Future Features
- **Loyalty Program:** Implementation of a points system to reward frequent shoppers.
- **Live Chat Support:** Real-time assistance for customers navigating the site.

## Database Design
### Database Model
The application uses a PostgreSQL database with models for Users, Products, Orders, and Events.

### Custom Model
A custom model `ProductReview` allows users to post reviews on products they have purchased.

### CRUD
- **Create:** Users can register, add products to the cart, and place orders.
- **Read:** Products, reviews, and user profiles are displayed.
- **Update:** Users can update their profiles and modify their cart.
- **Delete:** Users can remove products from their cart or delete their accounts.

## Technologies Used
### Work Environments and Hosting
The site is hosted on Heroku, with separate staging and production environments to manage deployments.

### Python Libraries
- **Django:** Main framework for web development.
- **Pillow:** For image processing capabilities in Django.

### Django Libraries
- **Django Allauth:** For handling user authentication.
- **Django Crispy Forms:** To render forms based on Bootstrap.

### Payment processing
Stripe API is integrated for secure online payments.

### Emails/Newsletter
Utilizes SendGrid for transactional emails and Mailchimp for newsletter distribution.

### SEO/Marketing
Google Analytics for tracking visitor data and insights.

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