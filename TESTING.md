# Table of Contents

- [Unit Testing](#unit-testing)
- [Manual Testing](#manual-testing)
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
- [Validation](#validation)
    * [HTML](#html)
    * [CSS](#css)
    * [Wave / Accessibility](#wave)
    * [Lighthouse](#lighthouse)
    * [Python](#python)

# Unit Testing
- I have written a total of 27 tests using the Django framework.
- Those tests are structured based on the model/view/form structure, thus are named test_model/test_view/test_form
- Coverage was used to check the total coverage of my tests
- The core files (model, view, form) are covered 100% and most other files are fully covered, too

### Testing screenshots:
![Unit testing image](/static/docs/unittesting/test.png)
<br>![Unit testing coverage image](/static/docs/unittesting/coverage.png)


# Manual Testing
### Feature 1 - Navigation bar and Welcome text
#### User stories:
1) As a *first time visitor* I can *see a landing page* so that *I get information about the website's purpose*
4) As a *first time visitor* I can *find the navigation bar* so that *I can navigate the page*

| **Feature** | **Action** | **Expected Result** | **Actual Result** |
|-------------|------------|---------------------|-------------------|
| Welcome text | Open page | See welcome text | Works as expected |
| Navbar | Open page > Look at top | Find navigation bar with links | Works as expected |

<details><summary>Screenshots</summary>

![Home page image](/static/docs/features/welcome.png)
![Navigation bar image](/static/docs/features/navbar.png)

</details>

### Feature 2 - About & Contact
#### User stories:
3) As a *first time visitor* I can *find an about page* so that *I can get information about the owner*

| **Feature** | **Action** | **Expected Result** | **Actual Result** |
|-------------|------------|---------------------|-------------------|
| About page | Open page, press "About" on navbar | See about text | Works as expected |

<details><summary>Screenshots</summary>

![Home page image](/static/docs/features/about.png)

</details>

12) As a *recurring visitor* I can *find contact information* so that *I can contact the owner*

| **Feature** | **Action** | **Expected Result** | **Actual Result** |
|-------------|------------|---------------------|-------------------|
| Contact info | Open page, press "About" on navbar | See contact text | Works as expected |

<details><summary>Screenshots</summary>

![Navigation bar image](/static/docs/features/contact.png)

</details>

### Feature 3 - Upcoming trips
#### User stories:
6) As a *first time visitor* I can *find the trips section* so that *I see upcoming and completed trips*

| **Feature** | **Action** | **Expected Result** | **Actual Result** |
|-------------|------------|---------------------|-------------------|
| Upcoming trips | Open page | See upcoming trips | Works as expected |

<details><summary>Screenshots</summary>

![Upcoming trips image](/static/docs/features/upcoming_trips.png)

</details>

### Feature 4 - Past trips
#### User stories:
6) As a *first time visitor* I can *find the trips section* so that *I see upcoming and completed trips*

| **Feature** | **Action** | **Expected Result** | **Actual Result** |
|-------------|------------|---------------------|-------------------|
| Past Trips | Open page > Press "Past trips" on navbar | See past trips | Works as expected |

<details><summary>Screenshots</summary>

![Past trips image](/static/docs/features/past_trips.png)

</details>

### Feature 5 - Register account
#### User stories:
2) As a *first time visitor* I can *sign up* so that *I have an account for the website*

| **Feature** | **Action** | **Expected Result** | **Actual Result** |
|-------------|------------|---------------------|-------------------|
| Register account | Open page > Press "Register" on navbar > Complete form | Have an account | Works as expected |

<details><summary>Screenshots</summary>

![Sign up page image](/static/docs/features/signup.png)

</details>

### Feature 6 - Sign in account
#### User stories:
7) As a *recurring visitor* I can *sign in* so that *I get access to my account*

| **Feature** | **Action** | **Expected Result** | **Actual Result** |
|-------------|------------|---------------------|-------------------|
| Sign in account | Open page > Press "Login" on navbar > Input credentials | Sign in to account | Works as expected |

<details><summary>Screenshots</summary>

![Sign in page image](/static/docs/features/login.png)
![Signed in text image](/static/docs/features/signed_in.png)

</details>

### Feature 7 - Sign out of account
#### User stories:
7) As a *recurring visitor* I can *sign in* so that *I get access to my account*

| **Feature** | **Action** | **Expected Result** | **Actual Result** |
|-------------|------------|---------------------|-------------------|
| Sign in account | Open page > Press "Login" on navbar > Input credentials | Sign in to account | Works as expected |

<details><summary>Screenshots</summary>

![Sign out page image](/static/docs/features/logout.png)

</details>

### Feature 8 - Register for trip
#### User stories:
8) As a *recurring visitor* I can *find the trip sign up* so that *I can sign up for an upcoming trip*

| **Feature** | **Action** | **Expected Result** | **Actual Result** |
|-------------|------------|---------------------|-------------------|
| Register for trip | Open home page > Press "Details" on desired trip > Press "Register" (Must be signed in) | Count as registered for trip / Have option to deregister | Works as expected |

<details><summary>Screenshots</summary>

![Details button image](/static/docs/features/trip_register_1.png)
![Trip Register image](/static/docs/features/trip_register_2.png)
![Details button image](/static/docs/features/trip_register_3.png)
![Trip Deregister image](/static/docs/features/trip_deregister.png)

</details>

### Feature 9 - Review trip
#### User stories:
10) As a *recurring visitor* I can *comment on trips I have been to* so that *I can rate them and provide information*

| **Feature** | **Action** | **Expected Result** | **Actual Result** |
|-------------|------------|---------------------|-------------------|
| Review trip | Open "Past trips" page > Press "Details" on desired trip > Complete review form (Only appears if user was registered for trip) | Comment and rating appear in reviews / Score counts towards average | Works as expected |
| Edit review | Open "Past trips" page > Press "Details" on desired trip > Press "Edit" on self user review > Complete form | Comment and rating appear updated in reviews | Works as expected |
| Delete review | Open "Past trips" page > Press "Details" on desired trip > Press "Delete" on self user review | Comment and rating are deleted | Works as expected |

<details><summary>Screenshots</summary>

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

</details>

### Feature 10 - Registered trips (Dashboard)
#### User stories:
5) As a *first time visitor* I can *get to my dashboard* so that *I see my account details*
9) As a *recurring visitor* I can *view all my trips* so that *I have a full history of them*

| **Feature** | **Action** | **Expected Result** | **Actual Result** |
|-------------|------------|---------------------|-------------------|
| Registered trips (Dashboard) | Press "Dashboard" on navbar | See user details (Currently only user past trips are displayed) | Works as expected |

<details><summary>Screenshots</summary>

![Trip history image](/static/docs/features/registered_trips_1.png)
![Trip Deregister image](/static/docs/features/trip_deregister.png)
![Trip history image](/static/docs/features/registered_trips_2.png)

</details>

### Feature 11 - Request trip
#### User stories:
11) As a *recurring visitor* I can *complete a request form* so that *I can request a trip idea*

| **Feature** | **Action** | **Expected Result** | **Actual Result** |
|-------------|------------|---------------------|-------------------|
| Request trip | Press "Dashboard" on navbar > Press "Request trip" on Options > Complete form | Request is created and sent to admin | Works as expected |

<details><summary>Screenshots</summary>

![Trip request image](/static/docs/features/request_1.png)
![Trip request image](/static/docs/features/request_2.png)

</details>

### Feature 12 - Admin panel Request page
#### User stories:
14) As an *admin/owner* I can *view trip requests* so that *I can get ideas about future trips*

| **Feature** | **Action** | **Expected Result** | **Actual Result** |
|-------------|------------|---------------------|-------------------|
| Admin panel Request page | On Admin panel > Press "Requests" | Can see all user requests | Works as expected |
| Admin panel Request approval | On Admin panel > Press "Requests" > Check desired request > Choose "Approve request" > Go | Request is approved | Works as expected |

<details><summary>Screenshots</summary>

![Admin trip request image](/static/docs/features/admin_approve_request_1.png)
![Admin trip request image](/static/docs/features/admin_approve_request_2.png)
![Admin trip request image](/static/docs/features/admin_approve_request_3.png)
![Admin trip request image](/static/docs/features/admin_approve_request_4.png)

</details>

### Feature 13 - Admin panel Trips page
#### User stories:
13) As an *admin/owner* I can *add a trip* so that *I can post new trips*
15) As an *admin/owner* I can *view a list of attendees* so that *I know who is joining each trip*

| **Feature** | **Action** | **Expected Result** | **Actual Result** |
|-------------|------------|---------------------|-------------------|
| Admin panel Trips page | On Admin panel > Press "Trips" | Can see all trips | Works as expected |
| Admin panel Trips page | On Admin panel > Press "Trips" > Press "Add Trip" > Complete form | New trip is added | Works as expected |
| Admin panel Trips page | On Admin panel > Press "Trips" > Choose trip | Can see all trip details, including registered users | Works as expected |

<details><summary>Screenshots</summary>

![Admin new trip image](/static/docs/features/admin_add_trip_1.png)
![Admin new trip image](/static/docs/features/admin_add_trip_2.png)
![Admin new trip image](/static/docs/features/admin_add_trip_3.png)
![Admin new trip image](/static/docs/features/admin_add_trip_4.png)
![Admin new trip image](/static/docs/features/admin_add_trip_5.png)

</details>

### Feature 14 - Footer
4) As a *first time visitor* I can *find the navigation bar* so that *I can navigate the page*

| **Feature** | **Action** | **Expected Result** | **Actual Result** |
|-------------|------------|---------------------|-------------------|
| Footer | Open page > Look at bottom | Find footer with details and links | Works as expected |

<details><summary>Screenshots</summary>

![Footer image](/static/docs/features/footer.png)

</details>

# Validation

## HTML
- HTML was validated using the [Markup Validation Service](https://validator.w3.org/)
- The Validator unfortunately cannot validate pages that require signed in access
- There are errors on pages that display Summernote created code. They are documented and cannot be removed

<details><summary>Screenshots</summary>

#### Home
![HTML home page validation](/static/docs/html_validation/home.png)

#### About
![HTML about page validation](/static/docs/html_validation/about.png)

#### Past Trips
![HTML past trips page validation](/static/docs/html_validation/past_trips.png)

#### Dashboard
![HTML dashboard page validation](/static/docs/html_validation/dashboard.png)

#### Sign in/Login
![HTML login page validation](/static/docs/html_validation/login.png)

#### Sign up
![HTML sign up page validation](/static/docs/html_validation/signup.png)

#### Logout
![HTML logout page validation](/static/docs/html_validation/logout.png)

#### Trip Details
- There are errors here because the description was created with Summernote, which adds HTML to the content (seen in second image)
- Unable to remove errors without removing Summernote
- Those errors do not affect the functionality page
![HTML trip details page validation](/static/docs/html_validation/trip_detail.png)
![HTML trip details page validation](/static/docs/html_validation/trip_detail_proof.png)

#### Past Trip Details
- There are errors here because the description was created with Summernote, which adds HTML to the content (seen in second image)
- Unable to remove errors without removing Summernote
- Those errors do not affect the functionality page
![HTML past trip details page validation](/static/docs/html_validation/past_trip_detail.png)
![HTML past trip details page validation](/static/docs/html_validation/past_trip_detail_proof.png)

#### Request
![HTML request page validation](/static/docs/html_validation/request.png)

</details>

## CSS
- CSS was validated using the [CSS Validation Service](https://jigsaw.w3.org/css-validator/)
- No errors found

<details><summary>Screenshots</summary>

![CSS code validation](/static/docs/css_validation.png)

</details>

## Wave / Accessibility
- Accessibility was tested with [Web Accessibility Evaluation Tool](https://wave.webaim.org/)
- All pages pass with no errors
- Wave cannot access pages that require signed in access

<details><summary>Screenshots</summary>

#### Home
![WAVE home page validation](/static/docs/wave/home.png)

#### About
![WAVE about page validation](/static/docs/wave/about.png)

#### Past Trips
![WAVE past trips page validation](/static/docs/wave/past_trips.png)

#### Sign in/Login
![WAVE login page validation](/static/docs/wave/login.png)
- When trying to sign in:
![WAVE login page validation](/static/docs/wave/sign_in_error.png)

#### Sign up
![WAVE sign up page validation](/static/docs/wave/register.png)

#### Trip Details
![WAVE trip details page validation](/static/docs/wave/trip_detail.png)

#### Past Trip Details
![WAVE past trip details page validation](/static/docs/wave/past_trip_detail.png)

</details>

## Lighthouse
- Chrome Lighthouse was used to test page performance
- All pages pass with a great mark
- Most warnings are about Bootstrap, or the time it takes to load the stylesheet due to Heroku/Cloudinary

<details><summary>Screenshots</summary>

#### Home
![Lighthouse home page validation](/static/docs/lighthouse/home.png)

#### About
![Lighthouse about page validation](/static/docs/lighthouse/about.png)

#### Past Trips
![Lighthouse past trips page validation](/static/docs/lighthouse/past_trips.png)

#### Sign in/Login
![Lighthouse login page validation](/static/docs/lighthouse/login.png)

#### Logout
![Lighthouse logout page validation](/static/docs/lighthouse/logout.png)

#### Sign up
![Lighthouse sign up page validation](/static/docs/lighthouse/register.png)

#### Trip Details
![Lighthouse trip details page validation](/static/docs/lighthouse/trip_detail.png)

#### Past Trip Details
![Lighthouse past trip details page validation](/static/docs/lighthouse/past_trip_detail.png)

#### Dashboard
![Lighthouse dashboard page validation](/static/docs/lighthouse/dashboard.png)

#### Request
![Lighthouse request page validation](/static/docs/lighthouse/request.png)

</details>

## Python
- For Python validation I used [PEP8 Online](http://pep8online.com/)
- I tested only files that I made changes to, not files that Django creates on its own and there was no input from me
- All files pass with no errors, except of settings.py
- For settings.py, the only errors are about length for code that should not be changed

<details><summary>Screenshots</summary>

#### admin.py
![PEP8 admin.py validation](/static/docs/pep8/admin.png)

#### apps.py
![PEP8 apps.py validation](/static/docs/pep8/apps.png)

#### forms.py
![PEP8 form.py validation](/static/docs/pep8/forms.png)

#### models.py
![PEP8 models.py validation](/static/docs/pep8/models.png)

#### settings.py
- Errors are from code that Django creates and I did not modify, so nothing will break
- Last error is about cloudinary url, which is large in its own
![PEP8 settings.py validation](/static/docs/pep8/settings.png)

#### test_forms.py
![PEP8 test_forms.py validation](/static/docs/pep8/test_forms.png)

#### test_models.py
![PEP8 test_models.py validation](/static/docs/pep8/test_models.png)

#### test_views.py
![PEP8 test_views.py validation](/static/docs/pep8/test_views.png)

#### trips.py
![PEP8 trips.py validation](/static/docs/pep8/trips.png)

#### urls.py (trips)
![PEP8 urls.py for trips validation](/static/docs/pep8/urls_app.png)

#### urls.py (hike-a-thon)
![PEP8 urls.py for project validation](/static/docs/pep8/urls_project.png)

#### validators.py
![PEP8 validators.py validation](/static/docs/pep8/validators.png)

</details>