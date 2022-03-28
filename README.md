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
        + [User Stories](#user-stories)
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
The database diagram can be seen below:<br>
![Database diagram image](/static/docs/database_diagram.png)

#### Models
##### User
- The User model contains information about each user that registers
- It is part of the Django allauth library
- The following fields are used for this project: username, email, password

##### Trip
- The Trip model is the main model
- Only Admins can create Trip objects, but all users can interact with them
- The model contains the following fields: name, slug, destination, date_start, date_end, description, image, price, registered_users
- Has functions to count the registered users and show if the trip is completed
- Has a ManyToMany relationship, where all registered users are stored

##### Review
- Used by users to review Trip objects, thus has a ForeignKey relationship with both Trip and User
- Contains the following fields: trip, user, comment, rating, submitted_on
- Has function to return the rating as a list, so the app can count it

##### Request
- Used by users to request trips, thus has a ForeignKey relationship with User
- Contains the following fields: user, destination, description, submitted_on, approved
- Admins have the function to approve the request

## Scope
The User Stories are described below
### User Stories
First time visitor:
1) As a *first time visitor* I can *see a landing page* so that *I get information about the website's purpose*
2) As a *first time visitor* I can *sign up* so that *I have an account for the website*
3) As a *first time visitor* I can *find an about page* so that *I can get information about the owner*
4) As a *first time visitor* I can *find the navigation bar* so that *I can navigate the page*
5) As a *first time visitor* I can *get to my dashboard* so that *I see my account details*
6) As a *first time visitor* I can *find the trips section* so that *I see upcoming and completed trips*

Recurring visitor:
7) As a *recurring visitor* I can *sign in* so that *I get access to my account*
8) As a *recurring visitor* I can *find the trip sign up* so that *I can sign up for an upcoming trip*
9) As a *recurring visitor* I can *view all my trips* so that *I have a full history of them*
10) As a *recurring visitor* I can *comment on trips I have been to* so that *I can rate them and provide information*
11) As a *recurring visitor* I can *complete a request form* so that *I can request a trip idea*
12) As a *recurring visitor* I can *find contact information* so that *I can contact the owner*

Admin/Owner:
13) As an *admin/owner* I can *add a trip* so that *I can post new trips*
14) As an *admin/owner* I can *view trip requests* so that *I can get ideas about future trips*
15) As an *admin/owner* I can *view trip requests* so that *I can get ideas about future trips*
16) As an *admin/owner* I can *view a list of attendees* so that *I know who is joining each trip*

## Design
### Wireframes

![Home wireframes](/static/docs/wireframes/home.png)
![Trip details wireframes](/static/docs/wireframes/trip_details.png)
![Dashboard wireframes](/static/docs/wireframes/dashboard.png)
![Request wireframes](/static/docs/wireframes/request.png)

### Colours
The colour palette was taken from [Color Hunt](https://colorhunt.co/palette/6fb2d285c88aebd671eeeeee)<br>
![Colour palette used](/static/docs/colours.png)

### Fonts
The fonts used are from the Google Fonts library, and are the following:
Josephin for the logo
Nunito for the website's text

# Features

### Feature 1 - Navigation bar and Welcome text
- The navigation bar has links to all pages, except the ones for each trip
- The logo brings the user back to the home page
- Navigation is consistent across all pages
- Welcome text is displayed when the user visits the page

![Navigation bar image](/static/docs/features/navbar.png)
![Home page image](/static/docs/features/welcome.png)

### Feature 2 - About & Contact
- Basic about information on the left (large screens)
- Contact information on the right (large screens)

![About us image](/static/docs/features/about.png)
![Contact image](/static/docs/features/contact.png)

### Feature 3 - Upcoming trips
- All upcoming trips are displayed
- Paginated by 3
- Each trip has a "Details" button, to go to the trip details

![Upcoming trips image](/static/docs/features/upcoming_trips.png)
![Details button image](/static/docs/features/trip_register_1.png)

### Feature 4 - Past trips
- All past trips are displayed
- Paginated by 3
- Each trip has a "Details" button, to go to the trip details

![Upcoming trips image](/static/docs/features/past_trips.png)
![Details button image](/static/docs/features/past_trip_detail_1.png)

### Feature 5 - Register account
- Users can create an account
- Template and functionality is provided by Django

![Sign up page image](/static/docs/features/signup.png)

### Feature 6 - Sign in account
- Users can sign in to their account
- Template and functionality is provided by Django
- Users will see that they are signed in on all pages

![Sign in page image](/static/docs/features/login.png)
![Signed in text image](/static/docs/features/signed_in.png)

### Feature 7 - Sign out of account
- Users can sign out of their account
- Template and functionality is provided by Django

![Sign out page image](/static/docs/features/logout.png)

### Feature 8 - Register for trip
- Users can register for upcoming trips
- They have the option to do so when they visit the trip details
- If they register, the button will turn to "Deregister" and they will be counted towards the registered users
- They can then deregister

![Details button image](/static/docs/features/trip_register_1.png)
![Trip Register image](/static/docs/features/trip_register_2.png)
![Details button image](/static/docs/features/trip_register_3.png)
![Trip Deregister image](/static/docs/features/trip_deregister.png)

### Feature 9 - Review trip
- Users can review trips they have registered for and are completed
- They need to complete the form with at least some data
- The score they provide is added to the total score average
- They can edit the review later or delete it

![Trip review guide image](/static/docs/features/new_review_1.png)
![Trip score image](/static/docs/features/score_before_review.png)
![Trip review guide image](/static/docs/features/new_review_2.png)
![Trip review guide image](/static/docs/features/new_review_3.png)
![Trip score image](/static/docs/features/score_after_review.png)
![Trip review edit guide image](/static/docs/features/edit_review_1.png)
![Trip review edit guide image](/static/docs/features/edit_review_2.png)
![Trip review edit guide image](/static/docs/features/edit_review_3.png)
![Trip delete review image](/static/docs/features/delete_review_1.png)
![Trip delete review image](/static/docs/features/delete_review_2.png)

### Feature 10 - Registered trips (Dashboard)
- Users can view all the trips they have registered for
- Completed trips have a checkmark
- All trip names are links to the trip details
- If the user deregisters from one trip, it is removed

![Trip history image](/static/docs/features/registered_trips_1.png)
![Trip Deregister image](/static/docs/features/trip_deregister.png)
![Trip history image](/static/docs/features/registered_trips_2.png)

### Feature 11 - Request trip
- Users can make a trip request
- The trip request will be added to their request history
- The admin can approve it and they will see an 'X' for not approved (default) or a checkmark if approved

![Trip request image](/static/docs/features/request_1.png)
![Trip request image](/static/docs/features/request_2.png)

### Feature 12 - Admin panel Request page
- Admin can see trip requests
- They have the option to approve any they want

![Admin trip request image](/static/docs/features/admin_approve_request_1.png)
![Admin trip request image](/static/docs/features/admin_approve_request_2.png)
![Admin trip request image](/static/docs/features/admin_approve_request_3.png)
![Admin trip request image](/static/docs/features/admin_approve_request_4.png)

### Feature 13 - Admin panel Trips page
- Admin can see trip objects and add new ones
- They need to add necessary data to trips
- They can choose which users to pre-populate 'registered_users' with

![Admin new trip image](/static/docs/features/admin_add_trip_1.png)
![Admin new trip image](/static/docs/features/admin_add_trip_2.png)
![Admin new trip image](/static/docs/features/admin_add_trip_3.png)
![Admin new trip image](/static/docs/features/admin_add_trip_4.png)
![Admin new trip image](/static/docs/features/admin_add_trip_5.png)

### Feature 14 - Footer
- Footer contains basic contact information
- Is always located at the bottom of the page and does not overlap with content

![Footer image](/static/docs/features/footer.png)

# Technologies used
## Languages
The languages used are:
- HTML
- CSS
- JavaScript (only what is created by Django - No personal code)
- Python

## Libraries and other resources
The project is based on Django, but contains the following resources, too:
- Bootstrap 5
- PostgreSQL
- Balsamiq
- Coverage
- HTML Markup Validation
- CSS Validation Service
- PEP8 Validation
- Quick Database Diagrams
- Crispy Forms
- FontAwesome
- Google Fonts
- Github
- Heroku

# Testing
All conducted testing can be found on the separate file, [TESTING.md](TESTING.md)

# Deployment
## Note
The project uses Cloudinary for static files hosting and it is needed for deployment and development.
## Local Deployment
You can clone this repository and run it locally with the following steps:
1. Login to GitHub (https://wwww.github.com)
2. Select the repository AlexGCbn/CI_PP4_Hike-a-thon
3. Click the Code button and copy the HTTPS url, for example: https://github.com/AlexGCbn/CI_PP4_Hike-a-thon.git
4. In your IDE, open a terminal and run the git clone command, for example:
    ```git clone https://github.com/AlexGCbn/CI_PP4_Hike-a-thon.git```
5. The repository will now be cloned in your workspace
6. Create an env.py file(This file should be included in .gitignore, so it will not be commited) in the root folder in your project, and add in the following code with the relevant key, value pairs, and ensure you enter the correct key values<br>
<br><code>import os</code>
<br>
<br><code>os.environ['SECRET_KEY'] = 'ADDED_BY_YOU'</code>
<br><code>os.environ['DATABASE_URL'] = 'ADDED_BY_YOU'</code>
<br><code>os.environ['CLOUDINARY_URL'] = 'ADDED_BY_YOU'</code>
<br>

7. Install the relevant packages as per the requirements.txt file
8. In the settings.py ensure the connection is set to either the Heroku postgres database or the local sqllite database
9. Ensure debug is set to true in the settings.py file for local development
10. Add localhost/127.0.0.1 to the ALLOWED_HOSTS variable in settings.py
11. Run "python3 manage.py showmigrations" to check the status of the migrations
12. Run "python3 manage.py migrate" to migrate the database
13. Run "python3 manage.py createsuperuser" to create a super/admin user
14. Start the application by running <code>python3 manage.py runserver</code>
15. Open the application in a web browser with the URL: http://127.0.0.1:8000/

## Heroku
This project can be deployed to Heroku with the following steps:
1. Create an account on [Heroku](https://www.heroku.com/)
2. Create an app, give it a name for example hike-a-thon, and select a region
3. Under resources search for postgres, and add a Postgres database to the app
4. Note the DATABASE_URL, this needs to be set as an environment variable in Heroku and your local environment variables
5. Create a Procfile with the text: web: gunicorn hike_a_thon.wsgi
6. Make sure you add your environment variables (env.py) to Heroku's Config Vars
7. In the settings.py ensure the connection is to the Heroku postgres database
8. Ensure debug is set to false in the settings.py file
9. Add 'localhost/127.0.0.1', and 'hike-a-thon.herokuapp.com' to the ALLOWED_HOSTS variable in settings.py
10. Run "python3 manage.py showmigrations" to check the status of the migrations
11. Run "python3 manage.py migrate" to migrate the database
12. Run "python3 manage.py createsuperuser" to create a super/admin user
13. Connect the app to GitHub, and enable automatic deploys from main
14. Click deploy to deploy your application to Heroku for the first time

# Credits
The app was created by relying on Code Institute's Django Blog walkthrough app, so a big thanks for that! 
I would also like to thank my mentor, Mo Shami, for his continued support and encouragement through my course! 


User stories:  
  
First time visitor:
As a *first time visitor* I can *see a landing page* so that *I get information about the website's purpose*
- Navigate to home page<br>
As a *first time visitor* I can *sign up* so that *I have an account for the website*
- Press "Register" > Complete form correctly > Press Sign Up<br>
As a *first time visitor* I can *find an about page* so that *I can get information about the owner*
- Navigate to "About" page<br>
As a *first time visitor* I can *find the navigation bar* so that *I can navigate the page*
- Navigate to any page and look to top<br>
As a *first time visitor* I can *get to my dashboard* so that *I see my account details*
- Sign in > Navigate to "Dashboard"<br>
As a *first time visitor* I can *find the trips section* so that *I see upcoming and completed trips*
- Navigate to home page for trips > Navigate to "Past Trips" for completed trips.<br>

Recurring visitor:
As a *recurring visitor* I can *sign in* so that *I get access to my account*
- Press "Login" > Complete form > Press "Sign in"<br>
As a *recurring visitor* I can *find the trip sign up* so that *I can sign up for an upcoming trip*
- Press "Details" on wanted trip > Press "Register"<br>
As a *recurring visitor* I can *view all my trips* so that *I have a full history of them*
- Sign in > Press "Dashboard" > See trips<br>
As a *recurring visitor* I can *comment on trips I have been to* so that *I can rate them and provide information*
- Sign in > Find completed trip that user was registered to > Complete review form > Press submit<br>
As a *recurring visitor* I can *complete a request form* so that *I can request a trip idea*
- Sign in > Press "Dashboard" > Press "Request trip"<br>
As a *recurring visitor* I can *find contact information* so that *I can contact the owner*
- Navigate to "About" page > See contact information<br>

Admin/Owner:
As an *admin/owner* I can *add a trip* so that *I can post new trips*
- On Admin panel > Navigate to Trips > Press "Add Trip" > Complete form<br>
As an *admin/owner* I can *view trip requests* so that *I can get ideas about future trips*
- On Admin panel > Navigate to Requests > View Requests (approve if needed)<br>
As an *admin/owner* I can *view trip requests* so that *I can get ideas about future trips*
- On Admin panel > Navigate to Requests > Tick request > Choose "Approve request" from options<br>
As an *admin/owner* I can *view a list of attendees* so that *I know who is joining each trip*
- On Admin panel > Navigate to Trips > Choose trip > Look at "Chosen registered users"<br>

### Colour palette:
https://colorhunt.co/palette/6fb2d285c88aebd671eeeeee