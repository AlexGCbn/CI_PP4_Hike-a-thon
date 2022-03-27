# CI_PP4_Hike-a-thon
Hike-a-thon is a hiking trips website, which permits users to register for trips that the administrator has posted. It was developed as the Portfolio Project 4 for the Code Institute Diploma in Software Development (Full Stack - E-commerce Applications).

- There are two types of users, for which test accounts are provided:
    - An administrator with the username/password of admin/admin
    - Regular users with the username/passwords:
        - alexT/testpassword1
        - georgeC/testpassword1
        - Mike.F/testpassword1
<br>

** View the live website [here](https://hike-a-thon.herokuapp.com/)**
<br><br>
** Website image **

- [Project Overview](#project-overview)
- [UX](#ux)
    * [Strategy](#strategy)
        + [Primary Goals](#primary-goal)
    * [Structure](#structure)
        + [Website pages](#website-pages)
        + [Code Structure](#code-structure)
        + [Database](#database)
            - [Database diagram](#database-diagram)
            - [Models](#models)
    * [Scope](#scope)
        + [User Stories]
    * [Design](#design)
        + [Wireframes](#wireframes)
        + [Colours](#colours)
        + [Fonts](#fonts)
- [Features](#features)
    * [Feature 1 - Navigation Bar and Homepage](#feature-1)
    * [Feature 2 - Welcome text](#feature-2)
    * [Feature 3 - Upcoming Trips](#feature-3)
    * [Feature 4 - Footer](#feature-4)
    * [Feature 5 - Trip Details](#feature-5)
    * [Feature 6 - Trip Registration](#feature-6)
    * [Feature 7 - Past Trips](#feature-7)
    * [Feature 8 - Trip Review](#feature-8)
    * [Feature 9 - Delete Review](#feature-9)
    * [Feature 10 - Edit Review](#feature-10)
    * [Feature 11 - Register](#feature-11)
    * [Feature 12 - Login](#feature-12)
    * [Feature 13 - Logout](#feature-13)
    * [Feature 14 - Admin page](#feature-14)
- [Technologies Used](#technologies-used)
    * [Languages](#languages)
    * [Libraries and other resources](#libraries-and-other-resources)
- [Testing](#testing)
- [Deployment](#deployment)
  * [Local Deployment](#local-deployment)
  * [Heroku and Postgres Database](#heroku-and-postgres-database)
- [Credits](#credits)

# Project Overview
- This project is a website for the Portfolio Project 4, part of the Code Institute Diploma in Software Development (E-commerce Applications)
- The website is deployed using Heroku at the following URL: [Hike-a-Thon](https://hike-a-thon.herokuapp.com/)
- The GitHub repository contains all the source code, Issues, Project (kanban board) and assets. It can be found here[here.](https://github.com/AlexGCbn/CI_PP4_Hike-a-thon)
- The website is fully responsive for all media sizes

# UX
## Strategy
### Primary Goals

The primary goals of the website admins are:
- To add, edit and delete trips with all the relevant information, per the model.
- To be able to see user requests for trips.
- To be able to see and manage user reviews.

The primary goals of the website users are: 
- To register for an account on the website. 
- To sign in and sign out of the website. 
- To View a list of all trips.
- To view a list of all past trips
- To view details of future and past trips.
- To register for trips.
- To review past trips they have been to, and be able to edit it.
- To make trip requests.
- To see their trip history.

## Structure
### Website pages
- The website is structured into 10 pages.
- All pages extend the same base, so they have the same look.
- Pages are described below.

Page            |Description
:-------------         |:------------- 
Home     |The homepage consists of a welcome message and a list of upcoming trips
Trip Detail     |Each trip detail provides the details of the specific trip, with options for users
Past trips     |Provides a list of all past trips
Past trip details     |Each past trip detail provides the details of the specific trip, with options for users      
About     |Provides information about page and contact details
Register     |Users can sign up for an account
Login     |Users can sign in with their accounts
Logout     |Users can sign out of their accounts
Dashboard     |Users see their past trips
Request     |Users can make a trip request

### Code Structure
- The project contains one app.
- The project's app is the "trips" app, which handles all the trips data.
- The project is accompanied by:
    * templates
    * README (This file)
    * TESTING (Documentation about testing)
    * Procfile (To run the deployed application)
    * Requirements.txt (Contains all necesary libraries required)
- The project was built with the help of the Django Blog app.

### Database
- The project uses a relational database (PostgreSQL)
- Data is handled by the application with Django

#### Database diagram
The database diagram can be seen below:
![Database diagram image](/static/docs/database_diagram.png)



User stories:  
  
First time visitor:
As a *first time visitor* I can *see a landing page* so that *I get information about the website's purpose*
- Navigate to home page
As a *first time visitor* I can *sign up* so that *I have an account for the website*
- Press "Register" > Complete form correctly > Press Sign Up
As a *first time visitor* I can *find an about page* so that *I can get information about the owner*
- Navigate to "About" page
As a *first time visitor* I can *find the navigation bar* so that *I can navigate the page*
- Navigate to any page and look to top
As a *first time visitor* I can *get to my dashboard* so that *I see my account details*
- Sign in > Navigate to "Dashboard"
As a *first time visitor* I can *find the trips section* so that *I see upcoming and completed trips*
- Navigate to home page for trips > Navigate to "Past Trips" for completed trips.

Recurring visitor:
As a *recurring visitor* I can *sign in* so that *I get access to my account*
- Press "Login" > Complete form > Press "Sign in"
As a *recurring visitor* I can *find the trip sign up* so that *I can sign up for an upcoming trip*
- Press "Details" on wanted trip > Press "Register"
As a *recurring visitor* I can *view all my trips* so that *I have a full history of them*
- Sign in > Press "Dashboard" > See trips
As a *recurring visitor* I can *comment on trips I have been to* so that *I can rate them and provide information*
- Sign in > Find completed trip that user was registered to > Complete review form > Press submit
As a *recurring visitor* I can *complete a request form* so that *I can request a trip idea*
- Sign in > Press "Dashboard" > Press "Request trip"
As a *recurring visitor* I can *find contact information* so that *I can contact the owner*
- Navigate to "About" page > See contact information

Admin/Owner:
As an *admin/owner* I can *add a trip* so that *I can post new trips*
- On Admin panel > Navigate to Trips > Press "Add Trip" > Complete form
As an *admin/owner* I can *view trip requests* so that *I can get ideas about future trips*
- On Admin panel > Navigate to Requests > View Requests (approve if needed)
As an *admin/owner* I can *view a list of attendees* so that *I know who is joining each trip*
- On Admin panel > Navigate to Trips > Choose trip > Look at "Chosen registered users"

### Colour palette:
https://colorhunt.co/palette/6fb2d285c88aebd671eeeeee