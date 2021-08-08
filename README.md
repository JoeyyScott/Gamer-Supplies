<h1 align="center">Gamer Supplies</h1>

[View a live version of the site here.]()

I have created this project (Milestone project 4) as part of my Full Stack Web Development course with [Code Institute](https://codeinstitute.net/).

It is an E-Commerce site for a fictional company 'Gamer Supplies' which offers a variety of snacks for sale.

___

##  Contents

+ [**User Experience Design (UXD)**](<#user-experience-design>)

  + [Project Goals](<#project-goals>)
  + [Content Requirements](<#content-requirements>)
  + [Importance and Feasibility chart](<#importance-and-feasibility-chart>)
  + [User Stories](<#user-stories>)
  + [Website Structure](<#website-structure>)
  + [Design Decisions from UXD](<#design-decisions-from-uxd>)
    + Colour Scheme
    + Images
    + Typography
  + [Wireframes](<#wireframes>)
  + [Design Changes](<#design-changes>)

+ [**Database Schema**](<#database-schema>)

+ [**Features**](#features)

+ [**Technologies**](#technologies)

+ [**Testing**](#testing)

+ [**Deployment**](#deployment)

+ [**Credits**](#credits)
  
___

## User Experience Design

### Project Goals

The goal of this project is to create an MVP (mininum viable product) of an E-Commerce store for a fictional company called 'Gamer Supplies'. The brand motto is ' We provide quality service of Gamer Snacks seamlessly to you'. The site is aimed at gamers looking to stock up on their favourite snacks.

### Content Requirements

+ To provide users with an E-Commerce store that is designed in an user-tailored way to make the process intuitive and seamless.
+ To demonstrate my skills as a full stack web developer using HTML, CSS, JavaScript and Python.
+ To showcase my skills using the Django framework, the modules within it and use of the MVC paradigm.
+ To combine all my previous knowledge on the course into creating an application that looks and runs efficiently.

### Importance and Feasibility chart

Opportunity/Problem | Importance | Viability/Feasibility
:-------- |:--------:|:--------:
A. Users able to register an account and login  | 5 | 5
B. Users can add/edit and remove items from their crate | 5 | 5
C. Users are notified of their actions | 5 | 4
D. Users can re-purchase a past order | 3 | 3
E. Users can search for snacks | 4 | 4

### User stories

#### User goals

+ As a **User**, I want to easily understand the site upon loading it.
+ As a **User**, I want to be able to intuitively navigate the entire site with ease.
+ As a **User**, I want to be able to receive full site functionality on my mobile and tablet.
+ As a **User**, I want to be able to see what supplies are available for purchase on the site.
+ As a **User**, I want to know the prices.
+ As a **User**, I want to be able to seamlessly sign up for an account and receive a confirmation email.
+ As a **User**, I want to be able to access the company's associated social media profiles.
+ As a **User**, I want to be able to contact the company with any relevant questions.

#### Registered User goals

+ As a **Registered User**, I want to be able to easily login and logout of my account.
+ As a **Registered User**, I want to be able to easily add and remove items from my supply crate.
+ As a **Registered User**, I want to be able to easily purchase my crate.
+ As a **Registered User**, I want to receive a purchase confirmation email.
+ As a **Registered User**, I want to be able to easily update my contact and delivery information.
+ As a **Registered User**, I want to be able to view my previous orders.

#### Site Owner/Superuser goals

+ As a **Site Owner/Superuser**, I want to be able to add new supplies.
+ As a **Site Owner/Superuser**, I want to be able to edit and delete supplies.
+ As a **Site Owner/Superuser**, I want to be able to delete reviews.
+ As a **Site Owner/Superuser**, I want to be able to access the admin section of the site to view orders made, the items they contain and the delivery information.

### Website Structure

The structure of the site is very simple to provide an easy-to-use experience. The header/footer/nav links will remain in the same places across the site but will differ from mobile to other devices as the screen real estate is limited. The header will always contain a link to the supplies page and different links based on whether a user is logged in or a super-user.

| Other links shown |
|:-----------------:|
+ Not logged in: 
    + Register
    + Login

+ Logged in:
    + **Only as superuser** 
        + Add Supply
        + Manage Reviews
    + My Profile
    + My Crate
    + Logout

###  Design Decisions from UXD

#### Colour Scheme

![Colour Scheme](docs/images/colourscheme.png)

Using a combination of [coolors.co](https://coolors.co/) and [Accessible Color Generator Tool](https://learnui.design/tools/accessible-color-generator.html) I was able to create a colour scheme that uses contrasting blues and yellows  to convey the majority of the content as it matches the colours used in the brand's logo. The colour scheme will remain consistent throughout the buttons, the overall design of the site and where information is presented back to the user based on their actions. The off-white/off-black will be used for text and information popups.

- ![#4169e1](https://via.placeholder.com/15/4169e1/000000?text=+) `#4169e1`: Royal Blue
- ![#ffd700](https://via.placeholder.com/15/ffd700/000000?text=+) `#ffd700`: Gold Web Golden
- ![#eee6e6](https://via.placeholder.com/15/eee6e6/000000?text=+) `#eee6e6`: Isabaline
- ![#141414](https://via.placeholder.com/15/141414/000000?text=+) `#141414`: Eerie Black

I tested my colour contrasts against the AA guidelines using [this tool](https://learnui.design/tools/accessible-color-generator.html) as mentioned in my technologies section. I have included a picture below as proof:

![Accessible Colours](docs/images/aaproof.png)

#### Images

**Logo image** - This is a modified version of a cartoon crate clipart which is licensed for personal use ([source](http://clipart-library.com/clipart/22001.htm)).

![Logo](docs/images/logodesign.png)

#### Typography

Throughout the site two main fonts will be used. 

Headers and titles will use [Saira Stencil One](https://fonts.google.com/specimen/Saira+Stencil+One) and associated text will use [Salsa](https://fonts.google.com/specimen/Salsa).

The Saira Stencil One font was chosen as it resembles stencil lettering such as is used on shipping crates. I felt it an appropriate fit for the purpose of the site as the user fills a Gamer Supply crate. Salsa was chosen as a complimentary font as Google suggested it as a popular pairing with Saira Stencil One and it provides a non obtrusive font to display information across the site.

### Wireframes

| Page | Mobile | Tablet |  PC  |
| :----: |:-----: | :--: | :--: |
| Home | [View](docs/wireframes/mobile-home.png) | [View](docs/wireframes/tablet-home.png) | [View](docs/wireframes/pc-home.png) |
| Register | [View](docs/wireframes/mobile-register.png) | [View](docs/wireframes/tablet-register.png) | [View](docs/wireframes/pc-register.png) |
| Login | [View](docs/wireframes/mobile-login.png) | [View](docs/wireframes/tablet-login.png) | [View](docs/wireframes/pc-login.png) |
| Logout | [View](docs/wireframes/mobile-logout.png) | [View](docs/wireframes/tablet-logout.png) | [View](docs/wireframes/pc-logout.png) |
| Supplies User | [View](docs/wireframes/mobile-suppliesuser.png) | [View](docs/wireframes/tablet-suppliesuser.png) | [View](docs/wireframes/pc-suppliesuser.png) |
| Supplies Admin | [View](docs/wireframes/mobile-suppliesadmin.png) | [View](docs/wireframes/tablet-suppliesadmin.png) | [View](docs/wireframes/pc-suppliesadmin.png) |
| Crate | [View](docs/wireframes/mobile-crate.png) | [View](docs/wireframes/tablet-crate.png) | [View](docs/wireframes/pc-crate.png) |
| Reviews | [View](docs/wireframes/mobile-reviews.png) | [View](docs/wireframes/tablet-reviews.png) | [View](docs/wireframes/pc-reviews.png) |

### Design Changes

**Coupon missing from wireframes**
+ I have added a coupon feature on ```supplies.html``` which is not reflected in the wireframes as this was added into the project later.
    + The reason being I was unsure what to include for my second custom model to satisfy the project requirement. I am aiming for a distinction and as such have included a disclaimer here.

**Sort missing from wireframes**
+ I have added a sort feature on ```supplies.html``` which is not reflected in the wireframes as this was added into the project later.
    + It appears below the category links and expands to a dropdown sorting by Price, Name, Category and Brand (with options for ascending/descending).


**Reviews page without a wireframe**
+ When creating the wireframes I was unsure where I wanted to include reviews that had been posted.
    + I have opted to display them on the homepage and have used templating logic in both the homepage and manage reviews to handle there being no current reviews.


## Database Schema 

SQLite3 was used in the development of this project as part of the Django framework. Upon deploying, I used Heroku PostGres to handle the database for the production version of the site. The models used to construct the site are outlined below:

![Database Diagram](docs/images/dbdiagram.png)

I used [dbdiagram.io](https://dbdiagram.io) to create this rendering of the database model and the associated relationships between data sets.

**Supplies App:**

Category Model

| Field | Field Type | Field Options |
| --- | --- | --- |
| name | CharField | max_length=254 |

Supply Model

| Field | Field Type | Field Options |
| --- | --- | --- |
| name | CharField | max_length=254, null=True |
| category | ForeignKey | 'Category', null=True, blank=True, on_delete=models.SET_NULL |
| price | DecimalField | max_digits=6, deciaml_places=2
| description | TextField | null=True, blank=True |
| brand | CharField | max_length=254, null=True, blank=True |
| size | CharField | max_length=25, null=True, blank=True |
| image | ImageField | null=True, blank=True |

Coupon model

| Field | Field Type | Field Options |
| --- | --- | --- |
| code | CharField | max_length=10, unique=True |
| amount | IntegerField | validators=[MinValueValidator(1),MaxValueValidator(5)] |

**Checkout App:**

Order Model

| Field | Field Type | Field Options |
| --- | --- | ---|
| order_number | CharField | max_length=32, null=False, editable=False |
| user_profile | ForeignKey | UserProfile, on_delete=models.SET_NULL, null=True, blank=False, related_name='orders' |
| full_name | CharField | max_length=80, null=False, blank=False |
| email | EmailField | max_length=254, null=False, blank=False |
| contact_number | CharField | max_length=20, null=True, blank=True |
| address_line_1 | CharField | max_length=50, null=False, blank=False |
| address_line_2 | CharField | max_length=50, null=False, blank=False |
| town_or_city | CharField | max_length=50, null=False, blank=False |
| county | CharField | max_length=50, null=True, blank=True |
| postcode | CharField | max_length=20, null=True, blank=True |
| country | CountryField | blank_label="Country *", null=False, blank=False |
| date | DateTimeField | auto_now_add=True |
| order_total | DecimalField | max_digits=10, decimal_places=2, null=False, default=0 |
| original_crate | TextField | null=False, blank=False, default='' |
| stripe_pid | CharField | max_length=254, null=False, blank=False, default='' |

Crate Items Model

| Field | Field Type | Field Options |
| --- | :--- | ---|
| order | ForeignKey | Order, null=False, blank=False, on_delete=models.CASCADE, related_name="crateitems" |
| supply | ForeignKey | Supply, null=False, blank=False, on_delete=models.CASCADE |
| quantity | IntegerField | null=False, blank=False, default=0
| crateitem_total | DecimalField | max_digits=6, decimal_places=2, null=False, blank=False, editable=False

**Reviews App:**

Review Model

| Field | Field Type | Field Options |
| --- | --- | --- |
| review | TextField | null=True, blank=False |
| added_by | ForeignKey | User, on_delete=models.CASCADE |
| rating | IntegerField | default=0, validators=[MinValueValidator(1),MaxValueValidator(5)] |

#### [Back to top](#contents)

---

## Features

### Existing Features

## Included in the **header** is:

+ **Intuitive navigation**: The navigation bar is located in the same place throughout the site, is easy to use and collapses into a toggle button in mobile view which expands its content.
    + **Brand Icon and Name**: Provides a link to the homepage to allow the user to view it at any point.
    + **Nav Links**: Provides a way for the user to view the other pages on the site.
        + If the user is not logged in they will see Supplies, Register and Login.
        + If the user is logged in they will see Supplies, My Profile, My Crate and Logout.
        + If the user is logged in as a superuser they will see an additional 2 links below Supplies which are: Add Supply and Manage Reviews.

## Included in the **footer** is:

+ **Social media links**: These will take you to the various social media connnections for the company. (Currently the links will point to the homepage for the associated social media site as the brand's socials do not exist at this point in time).

## Included in **index.html** is:

**Website intro**:
+ Intro section loads at the top of the page.
    + Contains a tagline with a button to view the snacks in the store.
    + Contains an incentive to create an account as non logged in users do not have access to a crate.

**Reviews**:
+ I used an adapted Bootstrap 5 carousel to display reviews posted to the data store.
    + Carousel will not autoplay and displays reviews using a for loop.
    + If the user is logged in they will see an add review button.
    + If the user is logged in as an Admin they will have a manage reviews button below the add review button.

## Included in **supplies.html** is:

**Supplies**
+ A rendered list of cards which contain all the relevant information about the supply from the data store.
    + Image, Name, Description, Size, Brand and Price.

**Supply buttons**
+ Within each card there are multiple buttons based on who is accessing the site.
    + If the user is not logged in they will see Register and Login buttons.
    + If the user is logged in they will see an Add to Crate and quantity adjust buttons.
    + If the user is logged in as a superuser they will see an Add to Crate, quantity adjust and Edit/Delete buttons (denoted by relevant icons).

**Supply navigation**
+ A navigation bar which filters the list of supplies based on category filters and sort options which are contained in a dropdown.
+ A search box which allows users to search which can match the supply name, description and brand.


## Included in both **crate.html** and **checkout.html** is:

**Quantity adjust buttons**:
+ These buttons are validated using an external file ```quantity_input.html``` in the ```includes``` folder within supplies which allows them to be used across the site.
    + Buttons are set to the correct state on page load and when the input is changed.
    + Buttons are disabled outside of the range 1-99.
    + Buttons adjust the amount of the supply in:
        + ```supplies.html``` before clicking the add to crate button.
        + ```crate.html``` before clicking the update button.


## Included in **crate.html** is:

**Crate total with Coupon field**:
+ A price summary of their crate that updates when a valid coupon is entered.
    + Apply coupon form input where users can enter a 10 character max string.
        + This will then be checked against coupons in the data store when the apply coupon button is clicked and provide the correct result.
            + If the coupon exists, a section containing information of the current coupon and the savings/discount it provides to the user.
            + If the coupon does not exist, the user is returned to the crate without any changes.

**Navigation buttons**:
+ There are two buttons which provide relevant links to the user at the top of the page below the coupon field. These links point to:
    + Browse more snacks - ```supplies.html```
    + Secure checkout - ```checkout.html```

**Crate contents**:
+ Logged in users will see a summary of their crate; if it is empty they will see a button to the supplies page.
    + Included in the crate summary is the amount of supplies in the crate and a list of each item within the crate.
    + On each item within the crate they will see:
        + A summary of the item with an image, name, individual price and a subtotal based on the item quantity.
        + Update/delete and quantity adjust buttons.
        + If the quantity is set to 0 the item is removed from the crate.

## Included in **checkout.html** is:

**Checkout summary and contents**:
+ If the crate is empty they will be redirected to ```supplies.html``` with a message displaying that their crate is empty.
+ Included in the checkout summary is the amount of supplies in the crate and a list of each item within the crate.
+ On each item within the crate they will see:
    + A summary of the item with an image, name, individual price and a subtotal based on the item quantity.
+ The order total is displayed after the list.

**Delivery Information**:
+ A form which allows the user to fill out the relevant fields:
    + Full name, Email, Contact Number, Address Line 1, Address Line 2, Town or City, County, Postcode and Country.
+ A checkbox which allows the user to save their delivery information to their profile which will be preloaded on both the checkout and profile pages thereafter.

**Payment Information**:
+ A form which allows the user to fill out their card information which is verified through Stripe payments and handled using webhooks.

**Form buttons**:
+ There are two buttons which submit the form and provide a relevant link to the user below payment information. These buttons function as follows:
    + Adjust Crate - ```crate.html```
    + Secure checkout - Submits the form and verifies it through Stripe:
        + If successful the user will be redirected to ```checkout_success.html```
            + This page is very similar to the checkout summary page except that there will be an order number and only a singular button is present.
            + If the user is coming from their profile they will see
                + Back to profile - ```profile.html```
                + Got room for more? - ```supplies.html```
        + If unsuccessful the user will be redirected to ```checkout.html``` with an error message displayed, their crate and information intact.

## Included in **profile.html** is:

**Delivery Information**:
+ A form which allows the user to fill out the relevant fields:
    + Full name, Email, Contact Number, Address Line 1, Address Line 2, Town or City, County, Postcode and Country.
+ A button which allows the user to update their delivery information which will be preloaded on both the checkout and profile pages thereafter.

**Order history**:
+ A rendered list from orders linked to the users profile in the data store which contains a summary of each order. Included in this summary is:
    + Order Number and Date - Auto generated when the order is completed.
    + Order Items - Contains supply name and quantity pertaining to each item on the order.
    + Order Total - Contains the total price of the order.

## These features are included throughout the site and thus do not fall into a specific page

**Bootstrap Toasts**:
+ Bootstrap toasts are prebuilt notifications that are customized to suit the theme of the site, the action that has occured and display relevant messages based on this.
+ These notifications are used throughout the entire site in too many cases to list for each one so I have included the different templates used.
    + For all successful actions ```toast_success.html``` will be used.
    + For all unsuccessful actions ```toast_error.html``` will be used.
    + For all actions that do not fall into either of the previous categories ```toast_info.html``` will be used.


**Account system**:
+ I used [django-allauth](https://django-allauth.readthedocs.io/en/latest/installation.html) to create my account system within the project as it provided prebuilt templates I could style as desired.
    + Users can register with email confirmation, login and logout.

**CRUD Functionality for admins**:
+ Admins are able to create, read, update and delete records in the database for the project through various pages and functionality. Included in this is:
    + Supplies - ```supply_add.html```, ```supplies.html``` and ```supply_edit.html``` with the delete functionality activating when the associated button is pressed.
    + Reviews - ```review_add.html```, ```index.html``` and ```review_manage.html``` with the delete functionality activating when the associated button is pressed.
        + I did not include an edit feature as I felt it would devalue the integrity of the reviews and opted to only include create, read and delete for this feature.

### Features to be added

**Subscription**:
+ I would like the user to be able to order the same crate at a user defined interval (within reason) which would allow for more user options and incentives.
    + Example: If a user orders the same crate 10 times over a certain value they get a 50% discount on their next crate of those items.
+ This would also allow users to receive their favourite snacks whenever they wanted with only having to checkout once.

#### [Back to top](#contents)

---

## Technologies

### Languages
+ [HTML](https://en.wikipedia.org/wiki/HTML) - Used as the main language for structuring the website.
+ [CSS](https://en.wikipedia.org/wiki/CSS) - Used as the main language for styling the website.
+ [JavaScript](https://www.javascript.com/) - Used to import and initialize certain functions for use throughout the project.
+ [Python](https://www.python.org) - Used as the main coding language to generate the site, handle the database and user login system.

### Frameworks, libraries and programs
+ [AWS Amazon S3](https://aws.amazon.com/s3/) - Amazon Simple Storage Service (Amazon S3) was used to store media and static files used throughout the project.
+ [Bootstrap](https://getbootstrap.com/docs/5.0/getting-started/introduction/) - A CSS framework that allows for responsive design, prebuilt styling classes and other utlities/components to be applied throughout the entire site.
+ [Django](https://www.djangoproject.com/) - The project was built using Django's web framework.
+ [Djecrety](https://djecrety.ir/) - I used this tool to generate a secret key for Django.
+ [FavIcon](https://favicon.io/) - I used this tool to convert an image I made into icon form and provide the code (stated in HTML comments) to link this icon to base.html.
+ [Font Awesome](https://fontawesome.com/) - I used the Font Awesome icon library to provide icons throughout the site, mainly used for buttons. 
+ [Google Fonts](https://fonts.google.com/) - I used two fonts from the Google fonts library - "Saira Stencil One" and "Salsa".
+ [Git](https://git-scm.com) - Git is an open source version control system where you can commit and push changes to the associated Github repository.
+ [GitHub](https://github.com/) - GitHub was used to store the project code pushed from GitPod using Git.
+ [GitPod](https://gitpod.io) - GitPod was the online IDE (Integrated Development Engine) I used to develop this site.
+ [Heroku](https://dashboard.heroku.com/) - A cloud platform that was used to deploy and run the code pushed to the associated GitHub repository.
+ [jQuery](https://jquery.com/) - I used the jQuery library to provide access to a multitude of functions/methods throughout the site.
+ [Stripe](https://stripe.com/docs) - Stripe was used to integrate an online payment authentication and processing system.

### Docs
+ [Accessible Color Generator](https://learnui.design/tools/accessible-color-generator.html) - I used this tool in conjunction with coolors.co to provide a better colour contrast for accessibility.
+ [Am I Responsive?](http://ami.responsivedesign.is/) - I used this tool to easily display the responsiveness of my site for my README.md introduction.
+ [coolors.co](https://coolors.co) - I used this tool to generate a colour scheme based on the Gamer Supplies logo.
+ [GIMP](https://www.gimp.org) - I used this program to design the logo/favicon image and wireframes.
+ [Placeholder](https://placeholder.com) was used to generate colour boxes to display in the colour scheme section of my README.md file.

### Dependencies
+ [boto3](https://boto3.amazonaws.com/v1/documentation/api/latest/index.html) - Create, configure, and manage AWS services, such as Amazon Elastic Compute Cloud (Amazon EC2) and Amazon Simple Storage Service (Amazon S3) using the AWS SDK for Python (Boto3).
+ [django-allauth](https://django-allauth.readthedocs.io/en/latest/overview.html)  - Prebuilt Django applications that handle registration, user authentication, account management as well as support for third party accounts.
+ [Django Countries](https://pypi.org/project/django-countries/) - Provides country choices for use with forms and a prebuilt country field for models.
+ [Django Crispy Forms](https://django-crispy-forms.readthedocs.io/en/latest/) - Django tool to program customizable reusable layouts out of components used within forms.
+ [django-storages](https://django-storages.readthedocs.io/en/latest/) - A collection of Django custom storage backends. 
+ [dj_database_url](https://pypi.org/project/dj-database-url/) - Django utility allows you to configure your Django application to simply utilize the 12factor inspired ```DATABASE_URL``` environment variable.
+ [gunicorn](https://pypi.org/project/gunicorn/) - Python WSGI HTTP Server for UNIX.
+ [Pillow](https://pillow.readthedocs.io/en/stable/) - Imaging library for Python.
+ [psycopg2-binary](https://pypi.org/project/psycopg2-binary/) - PostgreSQL database adapter for Python.
+ [Stripe](https://stripe.com/docs) - Stripe’s API library for Python.

#### [Back to top](#contents)

---

## Testing

I created a separate file for the testing process which can be located [here](TESTING.md).

#### [Back to top](#contents)

---

## Deployment

### Project Inception

### Deployment to Heroku

Before creating a Heroku app make sure your project has these two files:
+ **requirements.txt** - You can create one by using ```pip3 freeze --local > requirements.txt```
+ **Procfile** - You can create one by using ```echo web: python run.py > Procfile```

### Creating a local clone

#### [Back to top](#contents)

---

## Credits

### Content

This section includes areas/sections of code and properties I was unaware of. I have also included sources from where I have adapted/changed code used in the projects throughout my course as I figured it was better practice to state as such to avoid any penalizations or copyright violations.

**Sending HTML through django messages and templates**:
+ I wanted to customize my Django messages and tried various solutions from searching myself.
    + The one that worked for me was [this post](https://stackoverflow.com/questions/58415186/how-to-make-a-new-line-in-django-messages-error) which uses "mark safe" from Django's built in utilities.

**TypedChoiceField**:
+ I was looking around for how to display the ratings on my reviews and after looking on [here](https://docs.djangoproject.com/en/3.2/ref/forms/fields/) I decided to use either TypedChoiceField or ChoiceField and when looking for how to set it up I found [this post](https://stackoverflow.com/questions/3673833/typedchoicefield-or-choicefield-in-django) which provided a basic structure which I adapted for my reviews ```forms.py``` file.

**Inner carousel for loop**:
+ When developing this project I encountered a bug in my Bootstrap carousel (details in [TESTING.md](TESTING.md))
+ I found [this post](https://stackoverflow.com/questions/35836879/how-to-use-for-loop-with-bootstrap-carousel) which solved my issue using the following code:
    + ```{% if forloop.counter == 1 %}active{% endif %}```

**Inner carousel scrollbar**:
+ I wanted my review carousel to be a fixed height and set ```overflow: scroll``` on the element.
    + This caused a scrollbar to appear and after searching around I found [this post](https://www.w3schools.com/howto/howto_css_hide_scrollbars.asp) which provided me with the CSS rules to hide the scrollbar but keep the functionality.
    + Hiding scrollbar for:
        + Chrome, Safari and Opera
        
            ```.example::-webkit-scrollbar {```
            
            ```display: none;```
            
            ```}```

        + IE, Edge and Firefox
        
            ```.example {```
            
            ```-ms-overflow-style: none;``` IE and Edge
            
            ```scrollbar-width: none;``` Firefox
            
            ```}```

**Redirecting after adding to crate**:
+ Originally I had this feature using:

    ```request.POST.get('redirect_url')```

    but when using the site in development I noticed when adding items to your crate it would clear your previous search/category filter/sorting whereas I wanted to return users to the page before pressing the button.
    + After searching around I found [this post](https://stackoverflow.com/questions/44151339/python-django-how-to-get-the-page-url-before-navigating-to-a-new-view) which utilized the following code:
    
        ```request.META.get('HTTP_REFERER')```
     
    + I set ```redirect_url``` to this value and the view functioned as intended.

**Scroll to top button**:
+ In searching how to find out detect if a user was scrolling and returning the amount I found [this post](https://css-tricks.com/how-to-make-an-unobtrusive-scroll-to-top-button/) which utilized the following code.

    ```javascript
    var rootElement = document.documentElement

    function handleScroll() {
        // Do something on scroll
        var scrollTotal = rootElement.scrollHeight - rootElement.clientHeight
        if ((rootElement.scrollTop / scrollTotal ) > 0.80 ) {
            // Show button
            scrollToTopBtn.classList.add("showBtn")
        } else {
            // Hide button
            scrollToTopBtn.classList.remove("showBtn")
        }
    }

    document.addEventListener("scroll", handleScroll)
    ```
+ I was able to utilize, ```document.documentElement```, ```scrollTop``` and the event listener and created a script to detect if the user had scrolled past a point (found using console logs) to take the relevant action with the back to top button.

    ```javascript
    document.addEventListener("scroll", function () { 
        var btt = document.getElementById('trigger-btt')
        if (page.scrollTop > 290) { btt.classList.remove('hidden'); } else { btt.classList.add('hidden'); }
    })

**Ordering a queryset in Django**:
+ After deploying my application to Heroku when editing supplies the order showed on "All Supplies" would default to the most recently edited being the last in the list.
    + I realized I had to sort them by the primary key attached to the Supplies in the data store.
    + After searching around I found [this post](https://books.agiliq.com/projects/django-orm-cookbook/en/latest/asc_or_desc.html) which utilized the ```order_by``` function within Django objects and showed how to set parameters.
    + Using this function ensured the Supplies were loaded in the correct order and were unaffected by being edited.

### Media

#### Images

### Acknowledgements

#### [Back to top](#contents)

---