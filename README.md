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
- [Bootstrap 5](https://getbootstrap.com/) - CSS framework directed used to create this responsive, mobile-first website.
- [JQuery](https://jquery.com/) - The project uses JQuery for easier DOM manipulation.
- [FontAwesome](https://fontawesome.com/)/[Flaticon](https://www.flaticon.com/) -  Font and Icon toolkits based on CSS and Less.
- [Jinja2](https://www.palletsprojects.com/p/jinja/) - Used with Django, this is a full-featured template engine for Python.

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
### Validators 
- [W3 HTML](https://validator.w3.org/) - Used to Validate HTML.
    - After fixing the most proeminent issues, a few were left unresolved on purpose such as "Duplicate ID" or multiple Autofocus.
    - These were likely caused by the validator having trouble reading through Jinja/Django code.
- [W3 CSS](https://jigsaw.w3.org/css-validator/) - Used to Validate CSS.
    - No errors or warnings found.
- [JS Hint](https://jshint.com/) - Used to Validate Javascript Code.
    - No errors or warnings found.
- [Flake8](https://flake8.pycqa.org/en/latest/user/index.html) - Used to Validate Python code according to PEP8 Guidelines.
    - Encountered a several "Line too long" errors that were mostly fixed, except when it would impact code functionality.
    - Some errors left unresolved as they belong to imported files, editing those could impact functionality.
    - After that, no further errors or warnings found.

### Manual Testing 
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

# Backend

- During development SQLite that comes built-in with Django was used for development mode and Heroku Postgre is used for production mode. 
- AWS (Amazon Web Services) was used to store static and media folders while in production.

Below is the chart of the database to show the data relationships.

![image](https://github.com/mariogusman/funfit/blob/master/readme/db.jpg)




## Testing User Stories

-   ### First Time Visitor Goals
    1. As a first time user, entering the site I know by the landing page and by vieweing the "All Products" section that the website sells Aircraft Models.
    2. As a first time user, I can navigate via the top navigation menu to view and filter the products and to also register my account.
    3. As a first time user, I can see the all the products in the website by going to the "All products" section via the top nav bar.
    4. As a first time user, I can filter all the products by their categories or Aircraft types via the top navigation bar to check the products I am most interested in.
    5. As a first time user, I can check my current cart by clicking on the Cart icon on the top menu and check the products I have added with the quantity and price.
    6. As a first time user, I can quickly and easily update my cart information by decreasing/increasing the products quantity and then clicking update or by removing a product I don't want it anymore.

-   ### Returning Visitor Goals
    1. As a returning user, I can check and sort the Aircraft Models by their price by using the Sort Field and selecting the Price sorting options.
    2. As a returning user, I can login back with my registered account from previous sessions.
    3. As a returning user, I can go through the checkout process with my previous information saved there.
    4. As a returning user, I can check my favorite Aircraft Models types by filtering the types I like the most via the top navigation menu.

-   ### Frequent Visitor Goals
    1. As a frequent user, I can login back to my account with all my previous information from past purchases added there and also with the order history.
    2. As a frequent user, I can quickly view all the products by going to "All Products" on the top navigation menu and seeing all the Aircraft Models current in the store.
    3. As a frequent user, I can see a banner message informing if I will have to pay the shipping price with the current cart and products I have added in the cart.
    4. As a frequent user, I can quickly add the products to my cart and return to the store using the "Back to the store" button to view and add any more products to the cart.
    5. As a frequent user, I can leave the website and when I return my session is saved and I can return to vieweing the website and the products without having to login back again and without having to re-add my products to the cart.

## Additional Testing

    All testing performed via the app deployed to Heroku (on the-Lotus.herokuapp.com)

-   ### Testing index.html page:

    1. When clicking "Click here to Access" I am succesfully redirected to the webstore page.

    2. Tested that the hero image of the Lotus is responsive to the screen size.

-   ### Testing the Products App:

    #### products.html page:
    1. On the /products/ page tested the Sort by option with: Price Ascending, Price Descending, Category Ascending, Category Descending, Name (A-Z), Name (Z-A) and made sure the sorting is working correctly for each sorte option.
    
    2. Tested the "Back to top" Button to make sure it is working.
    
    3. Tested the "Edit" and "Delete" buttons under the products to make sure they are working correctly.

    4. Tested the redirect to the product details page when we click on the product image.

    5. When clicking on the products tags we then filter the products to show all the same tags.

    6. Made sure that the success toast alert appears when a product is added to the cart.

    7. Made sure that all information being picked up from the database is showing correctly on the page.

    8. Made sure that only admins can view the edit and delete button and no unintended user can modify the product by modifying the page URL.

    #### product_detail.html page:

    1. Tested the "Edit" and "Delete" buttons to make sure they are working correctly.

    2. Tested the Increase and Decrease buttons to make sure they were working properly and that the quantity was updating accordingly.

    3. Tested both buttons "Keep Shopping" (Redirects back to /products/ page) and "Add to Cart"(add product to cart) to make sure they are working properly.

    4. Made sure that only admins can view the edit and delete button and no unintended user can modify the product by modifying the page URL.

    #### add_product.html page:

    1. Made sure that while on the adding product management page users can choose the correct selectors for Caregoty, Type and Manufacturer from the database.

    2. Tested both buttons "Cancel" (returns to products page) and "Add product" (to add the product to the database)

    3. Tested adding a test product and made sure the image and all the fiels were created correctly on the database.

    4. Tested the "noimage.jpg" to make sure if a product is added without an image the noimage.jpg appears.

    #### edit_product.html page:

    1. Tested that while clicking on the "Edit" button the user is redirected to the /product/edit/# page and the product information populates the forms.

    2. Tested both buttons "Cancel" (returns to products page) and "Update product" to certify they are working properly and updating the product information.

    3. Tested the toasts alert to make sure they appear to indicate that you are editing a product and also a toast success appears when you have succesfully updated the product.

-   ### Testing the Cart App and also cart.html page :

    1. Tested the Increase/Decrease button and then the "Update" button to make sure the product quantity is changing accordingly as well as the total price.

    2. While Increasing/Decreasing the product quantity and clicking "Update" the Success toast should appear to inform the product quantity was updated accordinly.

    3. Tested the "Remove" button and to confirm the product is removed from the cart.

    4. Tested both the "Keep Shopping" and "Proceed to Checkout" buttons to make sure they are working.

    5. While adding a product under €100 made sure that the yellow banner informing about the free delivery is appearing.

    6. Made sure that all the information is showing correctly like product name, price, quantity, subtotal and grand total.

    6. Made sure that the session cookie is working and that it keeps saved the products inside the cart even if you close and re-open the page.

-   ### Testing checkout app and also checkout.html and checkout_success.html page:

    1. Made sure when clicking on the "Modify Cart" you get back to your cart.

    2. Tested that when you are logged in the form is populated with the User information correctly.

    3. Made sure the order summary displays correctly all the information (product name, quantity and price)

    4. Tested purchasing a product and made sure the order was created succesfully in Stripe.

    5. While clicking on "Complete order" made sure the order was completed and redirected to the checkout_success.html page

    6. On the checkout_success.html page made sure all the order information was displaying correctly and that the success toast pops to confirm the order was processed.

    7. On the checkout_success.html page tested the "Back to store" button to make sure it redirects back to the /products/ page.

    8. Made sure after the order is succesfull that the order now displays in the Order History under the My Profile page.

    9. Tested the webhooks for payment intent succeed and payment intent failed.

    10. Made sure that when the "Save this delivery information to my profile" information is selected the information is indeed saved to the user profile.

-   ### Testing profiles app and profile.html page:
    1. Tested the "Update Information" button to make sure the information is updated correctly on the database.

    2. made sure the Order History is showing all the past order accordingly.

    3. When clicking on the Order History ID made sure the past order details appears and a toast alert pops in to inform the user is viewing a past confirmation order.

-   ### Testing toasts and main-nav.html and mobile-header.html pages:
    1. Tested all the toasts information (error, info, success and warning) throug the website to make sure they are appearing accordingly.

    2. On the toast_success.html made sure the button "View your Cart" shows correctly and redirects to the cart page.

    3. While selecting a product under €100 made sure the yellow bar advising about the free shipping fee appears.

-   ### Testing main navigation and collapsible bar:

    1. On the main top navigation bar tested all the links to make sure they are working properly and also the filters.

    2. On the main top navigation bar tested the Cart and Account icongs to make sure they are working. And while checking the account it is displaying the account options correctly.

    3. Made sure that only admins the product Management option.

    4. Tested the search bar to make sure it is working properly and the page is updating with the correct search query.

    5. On the collapsible bar made sure that all links are working properly.

    6. On the the collapsible bar made sure that the Search, Cart, and My Account are working as expected and that the total cart price is also updated.

## Bugs and Fixes

1. After adding the search functionality every time I was searching for anything it was displaying all the products.
	- 1.1 **Fix:** The indendation of both lines (lines followed below) was wrong. I have to remove one indendation level: 
    ```
            queries = Q(name__icontains=query) | Q(description__icontains=query)
            products = products.filter(queries)
    ```

2. After adding the search functionality for product types the server was running fine and not showing any error, but everytime I selecting the product type like "Jets" on the navbar it wasn't showing anything.
    - 2.1 **Fix:** I have to add a Friendly name to models.py so while selecting the type on navbar would retrieve the type name all in lowercase and show the friendly name with the first letter capitalized.

3. While trying to setup webhook I got a few 401 errors while trying to send a test event to a webhook endpoint. While investigating it better I have found out that this error was related to an Unauthorized request.
    - 3.1 **Fix:** The 8000 port was set to private and while checking Slack I have found out that the 8000 port must be set to public. After changing the 8000 port to public I was still getting a 401 error and this time was due to the URL added in stripe not containing the 8000 port on the URL (https://8000-coffee-mongoose-wi4a85v2.ws-eu18.gitpod.io/checkout/wh/).

4. After I deleted a product on Django Admin panel to perform a test the entire website started returning a 404 with the error message `RelatedObjectDoesNotExist at /admin/login/`
    - 4.1 **Fix:** After trying several times to close and start the python server and also shutting off and opening again the workspace on gitpod I found that the issue was with the session cookies. After clearing all the cookies I manage to see the website again without the products that I have deleted.

5. After deploying to Heroku I was trying to access the Postgres database to create Superuser but it was only accessing the SQLite database.
    - 4.1 **Fix:** After checking with Tutor Support he informed I forgot to add the DATABASE_URL to gitpod vars.

6. After deploying to Amazon S3 bucket the images were not showing.
    - 4.1 **Fix:** After a very detailed check I have found that instead of using `/media/` the images in Amazon S3 bucket were set to /static/media/. After I updated the URL the images appeared again.

# Deployment

## Heroku

The project was deployed on [Heroku](the-Lotus.herokuapp.com), the following steps were taken:

1. Created a requirements.txt file by typing: `pip3 freeze --local > requirements.txt` in the terminal.
2. Created a procfile.
3. Logged in to Heroku.
4. Pressed the button "new" and then "create new app".
5. Chose an app name and a region and pressed create app.
6. Went to deployment section.
7. Under deployment method pressed Github.
8. Chose the right repository in the list, pressed search and then connect.
9. Pressed enable automatic deploys under automatic deploys.
10. Click on the find more addons button.
11. Click on the Heroku Postgres button.
12. Click on install Heroku Postgres.
13. Went to settings.
14. Added all the config vars needed for the project.
15. Pressed open app.

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

## GitHub Pages 

**Under the repository page:**

    1. Click on Settings 
    2. Scroll down to the "GitHub Pages" section 
    3. Select the Source Branch 
    4. Click Save.

- For this project, I have used the cloud-based IDE [Gitpod](https://gitpod.io/) and [GitHub](http://github.com/) as a free git repository hosting.

    1. I started the project by creating a new Repository on GitHub and loading the [Code Institute Gitpod Template](https://github.com/Code-Institute-Org/gitpod-full-template).

    2. Installed the [Gitpod extension](https://chrome.google.com/webstore/detail/gitpod-dev-environments-i/dodmmooeoklaejobgleioelladacbeki) and on my GitHub repo I clicked on the Gitpod button to create a new Master Workspace on GitPod.

    3. After creating the workspace I developed the website using Gitpod and pushing my commits to GitHub using the following commands:
        - `git add "file-name"` - To add a file for staging.
        - `git commit -m "description-of-update"` - To commit.
        - `git push` - To push my commits to GitHub
        - I have also used extra git commands such as: 
        - `python3 -m http.server` - To run a preview of the website on the browser.
        - `git status` - To display the current state of the working directory and the staging area.

## Running locally

1. Go tho this [project repository](https://github.com/MatSim91/Milestone-Project-4-The-Lotus) in GitHub while signed in in your own GitHub account.
2. Click on the dropdown menu Code option.
3. Click on "Open with GitHub Desktop" to clone and open the repository locally.
4. Click on the "Choose" option and navigate to the local path where you want the cloned repository to be.
5. Click "Clone".

- [Click here](https://docs.github.com/en/free-pro-team@latest/desktop/contributing-and-collaborating-using-github-desktop/adding-and-cloning-repositories) for more cloning GitHub options.

# Credits

- [Code Institute Course](https://codeinstitute.net/) helping on setuping up the e-commerce store.

- [Font Awesome](https://fontawesome.com/icons) for the huge collection of free icons they offer.

- [Web Formatter](https://webformatter.com/) Used for formatting HTML, CSS and Javascript and also to check for errors.

- [Google Fonts:](https://fonts.google.com/) Thanks to Google for providing this huge amount of free fonts on the site.

- [Bootstrap](https://getbootstrap.com) for the large and free libraries 

- [Pixabay](https://pixabay.com/images/search/Lotus/) - Thanks to Pixabay for providing the awesome hero image of The Lotus

## Content

-  The  details and descriptions of the products were taken from [Wikipedia](https://www.wikipedia.org/) and from [Revell](https://www.revell.de/).

## Media

-  The media for the Aircraft Products was taken from a website that sell Aircraft Models: [Revell](https://www.revell.de/).

## Acknowledgements

- My mentor Akshat for all his help and ideas.

- Thanks to the tutors at Code Institute for all help during the course (Especial thanks to Scott for all his help).

- Slack channel help regarding ongoingissues and problem solving ideas.