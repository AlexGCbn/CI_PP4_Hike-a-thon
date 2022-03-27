# CI_PP4_Hike-a-thon
Hike-a-thon is a hiking trips website, which permits users to register for trips that the administrator has posted. It was developed as the Portfolio Project 4 for the Code Institute diploma in Software Development (Full Stack - E-Commerce).

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
        + [Primary Goal](#primary-goal)
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

User stories:  
  
First time visitor:
As a *first time visitor* I can *see a landing page* so that *I get information about the website's purpose*
As a *first time visitor* I can *sign up* so that *I have an account for the website*
As a *first time visitor* I can *find an about page* so that *I can get information about the owner*
As a *first time visitor* I can *find the navigation bar* so that *I can navigate the page*
As a *first time visitor* I can *get to my dashboard* so that *I see my account details*
As a *first time visitor* I can *find the trips section* so that *I see upcoming and completed trips*

Recurring visitor:
As a *recurring visitor* I can *sign in* so that *I get access to my account*
As a *recurring visitor* I can *find the trip sign up* so that *I can sign up for an upcoming trip*
As a *recurring visitor* I can *view all my trips* so that *I have a full history of them*
As a *recurring visitor* I can *comment on trips I have been to* so that *I can rate them and provide information*
As a *recurring visitor* I can *complete a request form* so that *I can request a trip idea*
As a *recurring visitor* I can *complete a contact form* so that *I can contact the owner*

Admin/Owner:
As an *admin/owner* I can *add a trip* so that *I can post new trips*
As an *admin/owner* I can *view trip requests* so that *I can get ideas about future trips*
As an *admin/owner* I can *view a list of attendees* so that *I know who is joining each trip*
As an *admin/owner* I can *view contact forms* so that *I have messages from users*
As an *admin/owner* I can *reply to contact forms* so that *users get messages from me*

### Colour palette:
https://colorhunt.co/palette/6fb2d285c88aebd671eeeeee

### Users & Passwords:

Admin: admin - admin
Test users:
alexT - testpassword1
georgeC - testpassword1
Mike.F - testpassword1