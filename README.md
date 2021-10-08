# Milestone Project 4 - Lotus Activewear</h1>

[Click here to view the live project :link:](https://lotus-activewear.herokuapp.com/)

Lotius Activewear is a fictional e-commerce website that sells Gym/Yoga clothes for woman. This was developed for my Code Institute Milestone 4 Project (Full Stack Frameworks with Django).

# Table Of Contents

1. [User Experience (UX)](#user-experience)
    - [User stories](#user-stories)
    - [Design](#design)
2. [Features](#features)
3. [Technologies Used](#technologies-used)
4.  [Languages Used](#languages-used)
5.  [Frameworks, Libraries & Programs Used](#frameworks-libraries-and-programs-used)
6.  [Database](#database)
7.  [Testing](#testing)
    - [Testing User Stories](#testing-user-stories)
    - [Additional Testing](#additional-testing)
    - [Bugs and Fixes](#bugs-and-fixes)
8. [Deployment](#deployment)
    - [Heroku](#heroku)
    - [Stripe and Database](#stripe-and-database)
    - [GitHub](#github-pages)
9. [Credits](#credits)
    - [Code](#code)
    - [Content](#content)
    - [Media](#media)
    - [Acknowledgements](#acknowledgements)

# User Experience

The main goal here is to provide a good shopping experience to potential customers either on mobile or desktop. All design elements inspire a delicate and sofisticate environment that goes with the whole wellness aspect.

-   ## User stories

    -   ### First Time Visitor Goals
        1. As a First Time user, I want to easily know what type of products are being offered.
        2. As a First Time user, I want to be able to register and access my account.
        3. As a First Time user, I want to check the different product categories.
        4. As a First Time user, I want to be informed of the minimum total to get free shipping.
        5. As a First Time user, I want to easily access my shopping bag to edit or remove any items.
        6. As a First Time user, I want to be able to view my shopping bag and proceed to checkout.

    -   ### Returning Visitor Goals
        1. As a Returning user, I want to use my account to log back in to manage my details.
        2. As a Returning user, I want to be able to checkout using my pre-defined delivery details.
        3. As a Returning user, I want check all my previous purchases in my account.

    -   ### Store Manager Goals
        1. As the store manager, I want to be able to login to my administrator account with super privileges.
        2. As the store manager, I want to be able to create new products through an intuitive interface.
        3. As the store manager, I want to be able to edit already created products through an intuitive interface.
        4. As the store manager, I want to be able to delete any products on the spot.

-   ## Design
 - Design for this project was inspired by a Local brand from my hometown. [Magia Do Mar](https://www.magiadomar.com.br/)(means, Sea Magic in Portuguese) features a clean and delicate design, with soft pastel colors and tones of gray. I attempted to follow the same patterns they did as I believe this website provides good user experience.

    -   ### Color Scheme
        - Following Magia do Mar's palette, I opted for bright pastel tones through the website with the main colors being shades of grey or pink.
        - Pastel shades of pink and ivory also match with the Lotus flower color palette.
        
    -   ### Typography
        - For the main logo and header fonts I chose "Comfortaa" from [Google Fonts](https://fonts.google.com/). This is a rounded geometric sans-serif type design that also compliments the delicate nature of the website.
        
    - ### Logo Icon
        - The Icon next to the logo is a simplistic representation of a Lotus Flower. The image itself comes from [Flaticon](https://www.flaticon.com/free-icon/lotus-flower_1308565?term=lotus&page=1&position=44&page=1&position=44&related_id=1308565&origin=search). In the website it was inserted using an SVG to preserve its carachteristics.

    - ### Effects and Feedback:
        - In order to provide a pleasant and intuitive experience, CSS effects were used in the main elements where interaction is possible.
        - These include:
            - Links and buttons and input fields changing color to let the user know they are being hovered or clicked.
            - Products that change colors along with a small border shadow when hovered.

    - ### Images:
        - When managers add a new product but do not provide an image URL, a personalised placeholder image will be inserted instead.
        - This placeholder image was edited on [Canva](https://www.canva.com/) using the free elements offered there, and features a camera with the "no product image" alert.

        - To aid in user navigation and provide feedback, I used free icons offered by [Fontawesome](https://fontawesome.com/) and [Bootstrap Icons](https://icons.getbootstrap.com/?).
            - Both were imported and used as fonts that can be manipulated using CSS.
            - I believe this is superior to regular Images as they won't lose quality when zoomed-in.

# Main Features
- **Navigation Resources** - Here users can access their account dashboard, see shopping bag total and click to access the bag, as well as search for products or navigate via categories.
- **Responsive Nav Bar** - When on a mobile device or in a small desktop window, the responsive website will collapse the navbar and make it easier for users to navigate clutter-free.
- **Product Quantity Updates** - While shopping or in their shopping bag, users can adjust the quantity of products they wish to purchase through an intuitive interface.
- **Persistent Bag Contents** - While navigating and shopping on Lotus, users will have a persistent shopping experience being able to leave their bag for a few hours or days and then come back to manage the contents and proceed to the checkout.
- **Profile Management** - Through their profile dashboard, users can update their delivery details as well as review their order history.
- **Product Management** - Super users/admins are can create, update and delete products through a easy to use interface..

# Technologies Used

### Languages
- [HTML5](https://whatwg.org/) - To create the main page's content structure.
- [CSS 3](https://www.w3.org/TR/CSS/#css) - Used with HTML to style this website's content.
- [JavaScript](https://www.javascript.com/) - Along with jQuery, used to create dynamically updating content.
- [Python](https://www.python.org/) - Used to run the main website functionalities including pushing and retrieving content from the DB and controling user session.

### Libraries/Frameworks
- [Django](https://www.djangoproject.com/) - Django is a high-level Python web framework that encourages rapid development and clean, pragmatic design.
- [Django Allauth](https://django-allauth.readthedocs.io/en/latest/installation.html) - Integrated set of Django applications addressing authentication, registration, account management as well as 3rd party (social) account authentication.
- [Django Countries](https://pypi.org/project/django-countries/) - Django application that provides country choices for use with forms, flag icons static files, and a country field for models.
- [Guicorn](https://gunicorn.org/) - The Gunicorn "Green Unicorn" is a Python Web Server Gateway Interface HTTP server. broadly compatible with a number of web frameworks, simply implemented, light on server resources and fairly fast.
- [Bootstrap 5](https://getbootstrap.com/) - CSS framework directed used to create this responsive, mobile-first website.
- [JQuery](https://jquery.com/) - The project uses JQuery for easier DOM manipulation.
- [FontAwesome](https://fontawesome.com/)/[Flaticon](https://www.flaticon.com/) -  Font and Icon toolkits based on CSS and Less.
- [Jinja2](https://www.palletsprojects.com/p/jinja/) - Used with Django, this is a full-featured template engine for Python.
- [Boto3](https://boto3.amazonaws.com/v1/documentation/api/latest/index.html) - Used to create, configure, and manage AWS services
- [Crispy Forms](https://django-crispy-forms.readthedocs.io/en/latest/) - Lets you control the rendering behavior of your Django forms in a very elegant and DRY way.


### Other
- [Github](https://github.com/) - Used version control using Git.
- [Stripe](https://stripe.com/en-ie) - Online payment processing for internet businesses.
- [Heroku](https://www.heroku.com/) - Cloud platform used for hosting the deployed website.
- [AWS](https://aws.amazon.com/) - Amazon Web Services offers reliable, scalable, and inexpensive cloud computing services.
- [SQLite3](https://www.sqlite.org/index.html/) - SQLite is a relational database management system pre-built into Django.
- [Gitpod](https://www.gitpod.io/) - Online IDE used to developed the project.
- [Favicon.io](https://favicon.io/favicon-converter/) - Used to convert image to Favicon.
- [Am I Responsive](http://ami.responsivedesign.is/?url=http%3A%2F%2Fms3-keto-recipes.herokuapp.com%2Frecipes%2F60c3445a59caadfa8d633b29) - To generate the demo image for this project.

# Testing
## Validators 
- [W3 HTML](https://validator.w3.org/) - Used to Validate HTML.
    - After fixing the most proeminent issues, a few were left unresolved on purpose such as "Duplicate ID" or multiple "Autofocus" warnings.
    - These were likely caused by the validator having trouble reading through Jinja/Django code.
- [W3 CSS](https://jigsaw.w3.org/css-validator/) - Used to Validate CSS.
    - No errors or warnings found.
- [JS Hint](https://jshint.com/) - Used to Validate Javascript Code.
    - No errors or warnings found.
- [Flake8](https://flake8.pycqa.org/en/latest/user/index.html) - Used to Validate Python code according to PEP8 Guidelines.
    - Encountered a several "Line too long" errors that were mostly fixed, except when it would impact code functionality.
    - Some errors left unresolved as they belong to imported files, editing those could impact functionality.
    - After that, no further errors or warnings found.

## Manual Testing 
- The deployed website was manually tested by myself.
- Testing consisted of general website usage, such as navigating through the navbar, clicking links and buttons, searching for products, creating accounts, editing profile details, completing orders, creating, editing and deleting products as an admin.

    - Desktop: Chrome, Firefox, Opera, Edge and Internet Explorer.
        - Only Internet Explorer presented issues: Though functionality was preserved, the layout was broken and design was heavily impacted, giving the aspect of an unfinished website.
        - I decided to leave this as is given that IE users represent only around 1% of all internet users as of May 2021. 
        - Source: [Statcounter](https://gs.statcounter.com/browser-market-share/desktop/worldwide).

    - Mobile: Android(Chrome) and iOS(Chrome and Safari) devices were used for testing.
        - For Android testing, a Galaxy A90 (6.7 inches, 1080x2400 pixels) was used.
        - For iOS testing, an iPhone 12 Mini (5.4-inch, 2340x1080 pixels) was used.
        - No issues found.

    - Mobile simulations were also made using Chrome DevTools.
        - Several screen sizes were used, for phones and tablets.
        - The "Responsive" option was also used and confirmed that the website is fully responsible and adaptable.

## Testing User Stories

-   ### First Time Visitor Goals
        1. As a First Time user, by looking at the background image and menu items, I become aware that Lotus sells activewear.
        2. As a First Time user, by clicking on Account > Register I can easily create an account.
        3. As a First Time user, by looking at the navigation bar at the top of the screen I can navigate to the different product categories.
        4. As a First Time user, by looking at the top of the screen I know how much I need to add to my bag. On the bag page I'm also informed of the amount remaining to get free shipping.
        5. As a First Time user, I can easily click on the bag icon to manage quantity added or remove a product altogether.
        6. As a First Time user, once I open my bag, it becomes clear that I only need to click a button to proceed to checkout.

    -   ### Returning Visitor Goals
        1. As a Returning user, if not already logged in, I can click on Account > Login to easily access my account.
        2. As a Returning user, by updating my profile details, I'm now able to checkout with pre-inserted details in my profile.
        3. As a Returning user, I can easily see my previous orders and even check its details by clicking on the order ID.

    -   ### Store Manager Goals
        1. As the store manager, I can follow the same steps as a regular user to log into my manager account.
        2. As the store manager, by hovering on the account menu, I can click on Manage Products to create a new one.
        3. As the store manager, by browsing the store or checking a product detail, I see buttons that allow me to easily edit said product.
        4. As the store manager, by browsing the store or checking a product detail, I see buttons that allow me to delete the products.

# Backend

- During development SQLite that comes built-in with Django was used for development mode and Heroku Postgre is used for production mode. 
- AWS (Amazon Web Services) was used to store static and media folders while in production.

Below is the chart of the database to show the data relationships.

![DB Structure](/readme/db.jpg)

## Bugs and Fixes
Throughout development, multiple minor issues were encountered, too many to list them all here. Most of these were due to commented code, typos or incorrect indentation.
They were investigated and quickly fixed during development.

Below are the most proeminent ones.

1. While having a test product added to my bag, I removed this item from the website through the admin panel, this caused the website to stop working.
    - I investigated the issue and concluded that this was caused by the deleted product being saved to my bag in the session cookie.
    - This was resolved by going to Chrome Dev Tools(F12) > Application > Cookies > Deleting 'session' entry.

2. While trying to setup webhooks I kept getting 400 errors upon sending test events via the Stripe Website.
    - I searched on Code Institute Slack and found out that this was caused by an issue with the ports on Gitpod.
    - Even though my ports were set to public it was not working.
    - I fixed this by closing all ports and setting them to 'public' again and concluded this was a visual glitch with Gitpod.
    - This issue kept happening whenever I restarted the project and the fix was the same every time, closing and opening ports.

    - With webhooks I also had an issue where they would fail despite ports being set to Public and I fixed this by exporting my credentials again through Gitpod Terminal. 

3. While testing the account creation and deletion functionality, I got a "IntegrityError at /admin/login/" which caused logins to stop working.
    - After hours of investigation and online searches, I thought this was caused by creating more than one account with the same 'test' name.
    - I was not able to delete said account as the admin panel was also not accessible.
    - After further review and with the help of Scott from the Tutor team I found out that this was caused due to a commented-out line of code in the models file for that app.
    - God bless Scott.

# Deployment

## Heroku

The project was deployed to [Heroku](https://www.heroku.com/). As described on their website, "Heroku is a platform as a service (PaaS) that enables developers to build, run, and operate applications entirely in the cloud".
The site was deployed from the Master branch of this GitHub repository using Heroku's "auto deployment" feature. This ensures that the website is always up-to-date with the master branch of the repository.

### Deploying to Heroku
- Before deploying this application, you must create a requiriments file by typing `pip freeze --local > requirements.txt` in your console.
- After that, the Procfile must be created. You can create this manually using your code editor UI or through the console by typing `echo web: gunicorn fun_fit.wsgi:application > Procfile`.
    - Make sure that the file name is "Procfile" with a capital "P" and no file extension.
    - Open the file to confirm if all the content is in a single line, with no blank lines at the bottom.

To deploy this project to Heroku, first you must create a Heroku account, as well as a new App by following the website intuitive UI and instructions.
Once your project is created, go to the "Deploy" tab and connect your Heroku App to your GitHub account, making sure to select the corresponding repository.

1. Created a requirements.txt file by typing: `pip3 freeze --local > requirements.txt` in the terminal.
2. Created a Procfile by typing: `echo web: gunicorn fun_fit.wsgi:application > Procfile` in the terminal.
3. Logged in to Heroku.
4. Pressed the button "new" and then "create new app".
5. Chose an app name and a region and clicked on "create app".
6. Went to deployment section.
7. Under deployment method clicked on "Github".
8. Selected my repository in the list and clicked "connect".
9. Clicked on "enable automatic deploys" under "automatic deploys".
10. Clicked on the "find more addons" button.
11. Clicked on the "Heroku Postgres" button.
12. Clicked on install "Heroku Postgres".
13. Went to "settings".
14. Added all the config vars needed for the project.
    - Head to the "Settings" tab on your Heroku dashboard and click on "Reveal Config Vars" halfway through the page and insert the following:
    1. `AWS_ACCESS_KEY_ID` → `Your AWS Access Key ID` (found on AWS)
    2. `AWS_SECRET_ACCESS_KEY` → `Your AWS Access Key ID` (found on AWS)
    3. `EMAIL_HOST_PASS` → `Your Email Host Pass` (Mine was Generated by Google Gmail > App Passwords)
    4. `EMAIL_HOST_USER` → `Your Email Host User` (Mine was Generated by Google Gmail > App Passwords)
    5. `SECRET_KEY` → `Your Django Secret key` (Mine was generated [here](https://miniwebtool.com/django-secret-key-generator/))
    6. `STRIPE_PUBLIC_KEY` → `Your Stripe Publick Key` (found on Stripe > Dashboard)
    7. `STRIPE_SECRET_KEY` → `Your Stripe Webhook Secret Key` (found on Stripe > Dashboard(click to reveal))
    8. `STRIPE_WH_SECRET` → `Your Stripe Webhook Secret Key` (found Stripe > Webhooks(click to reveal))
    9. `USE_AWS` → `True`
    10. `MONGO_DBNAME` → `Name of your Database`
    11. `MONGO_URI` → `Your Mongo URI`
    12. `SECRET_KEY` → `Your Secure Key`
15. Click "Open App" to see the deployed website.

## Stripe and Database

The first step after forking or cloning the project would be to install all dependencies needed by the system.
If the project is opened in GitPod the command in the terminal would be: `pip3 install -r requirements.txt`.
If working locally setting up a virtual environment first and after that running the `pip3 install -r requirements.txt` command.

In order for the project to work in a product environment a PostgreSQL database would need to be set up, this process might differ depending upon how you choose to deploy the site but on Heroku you would:
1. Log in to Heroku.
2. From the dashboard click the link to the app.
3. Go to resources.
4. Click on the find more addons button.
5. Click on the Heroku Postgres button.
6. Click on install Heroku Postgres.
7. Choose the Hobby dev free plan and choose your app in the list.
8. Press submit form.

If your using another way of hosting the project include an environment variable called "DATABASE_URL" which only exists in the production environment and create the connection to the database in this section in the settings.py file: if DATABASE_URL:
    DATABASES = {
        'default': dj_database_url.parse(DATABASE_URL)
    }

In order for the payment and order system to work a Stripe account needs to be created, with these steps:

1. Go to https://dashboard.stripe.com/register.
2. Enter all details and press create account.
3. Confirm your email address by following the link.
4. Create an account by pressing the top left account button.
5. Write name and press create account.
6. Navigate to developers/webhooks.
7. Click on add endpoint.
8. Enter the base URL of your website plus "/payments/confirmation/" in the URL field.
9. Choose checkout.session.completed in events to send and press add endpoint.
10. Go to developers/webhooks and click on the webhook.
11. Get the webhook signing secret by clicking click to reveal.
12. Get your Stripe API keys from developers/Stripe API
13 Store your webhook signing secret in the variable STRIPE_ENDPOINT_SECRET in settings.py.
14. Store your Stripe API secret_key in the variable STRIPE_TEST_SECRET_KEY in settings.py.
15. Add your publishable key as a string argument to the const stripe = Stripe() object in payments.js

Preferably hide your STRIPE_ENDPOINT_SECRET and STRIPE_TEST_SECRET_KEY values in environment variables if the project is to be publicly displayed.
The same goes for the rest of the settings that needs to be added to setting.py: 

SECRET_KEY : a secret key used to hash passwords etc.
EMAIL_HOST_USER : Gmail account you want to send mails from..
EMAIL_HOST_PASSWORD = App password which can be acquired by setting up two step verification and creating an app password for your Google account
DEFAULT_FROM_EMAIL = same Gmail account.

In development add an environment variable called DEVELOPMENT to use the development database.

### Running Localy
- This is just a brief explanation. Full instructions can be found on  [GitHub Docs - Cloning a repository](https://docs.github.com/en/github/creating-cloning-and-archiving-repositories/cloning-a-repository).

<br>

- To run this locally, navigate to Lotus Activewear [repository](https://github.com/mariogusman/Funfit).
- Click on "↓ Code" button.
    - Select from the options available, either downloading the [ZIP](https://github.com/mariogusman/Funfit/archive/refs/heads/main.zip) file, opening with [GitHub Desktop](https://desktop.github.com/) or by copying the HTTPS address.
    - If you opted for GitHub Desktop, after clicking the "Open with GitHub Desktop" button, all you need to do is click "Clone" and the enviroment will be created and files downloaded.
    - If you downloaded the ZIP files, you must manually extract them locally to then open it using your code editor of choice.
    - If you copied the HTTPS address:
        - Open the terminal in your IDE
        - Type `git clone` followed by the URL, E.g. `git clone https://github.com/mariogusman/Funfit.git`
- With the files in place, you must install the packages listed in the "requirements" file, E.g. `pip install -r requirements.txt`

### Contributing
- Though this project is for educational purposes, pull requests are welcome and will be reviewed once the project is graded. 
- For major changes, please open an issue so we can discuss the proposed changes.

# Credits

- [Code Institute Course](https://codeinstitute.net/) for providing all the knowledge used in this project through the Boutique Ado mini-project.
- [Font Awesome](https://fontawesome.com/icons) & [Bootstrap Icons](https://icons.getbootstrap.com/?) for the free icons offered.
- [Google Fonts:](https://fonts.google.com/) for the free fonts offered.
- [Bootstrap](https://getbootstrap.com) for the large and free libraries and examples.
- [Pexels](https://www.pexels.com/) for the background image used in this project.
- [Magia Do Mar](https://www.magiadomar.com.br/) for all the product images and design inspiration.

## Acknowledgements
- Thanks to Code Institute and all team members for the excellent content offered - Special mention to the Tutor team!
- Thanks to Chris Zielinski for all the answers in Slack and the excellent Boutique Ado videos/explanations.   
- Thank to my mentor, Gerry McBride.
- Thank you to two Code Institute colleagues, Mateus and Toto for the advice given.
- A big thank you to my wife for the patience, support, and for helping me test the website.