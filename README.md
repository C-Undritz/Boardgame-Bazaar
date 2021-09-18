# Boardgame Bazaar - Readme document

### Website can be viewed here: 

### Project Github site:

### **Disclaimer: This Website is for educational purposes only.**

------

# Table of Contents

- [OVERVIEW](https://github.com/C-Undritz/Community-Treats#overview)
- [STRATEGY](https://github.com/C-Undritz/Community-Treats#strategy)
- [SCOPE](https://github.com/C-Undritz/Community-Treats#scope)
- [STRUCTURE](https://github.com/C-Undritz/Community-Treats#structure)
- [SKELETON](https://github.com/C-Undritz/Community-Treats#skeleton)
- [SURFACE](https://github.com/C-Undritz/Community-Treats#surface)
- [TECHNOLOGIES USED](https://github.com/C-Undritz/Community-Treats#technologies-used)
- [TESTING](https://github.com/C-Undritz/Community-Treats#testing)
- [NOTED DESIGN CHANGES](https://github.com/C-Undritz/Community-Treats#noted-design-changes)
- [FEATURES](https://github.com/C-Undritz/Community-Treats#features)
- [FURTHER DEVELOPMENT](https://github.com/C-Undritz/Community-Treats#further-development)
- [DEVELOPMENT AND DEPLOYMENT](https://github.com/C-Undritz/Community-Treats#development-and-deployment)
- [DOCUMENTATION REFERENCED](https://github.com/C-Undritz/Community-Treats#documentation-referenced)
- [CREDITS AND THANKS](https://github.com/C-Undritz/Community-Treats#credits-and-thanks)

------

> # **OVERVIEW**

The board game industry has seen a resurgence in recent years and it is expected to carry on growing further.  Industry forecasters predict the global board game market will be worth more than £9bn by 2023.

For many gamers, the enjoyment of playing board and card games among friends, family members, and fellow enthusiasts is invaluable. And they are willing to pay for the experience, with the majority of gamers (41%) purchasing five to ten new games or expansions a year.

Consequently recent survey data found that 43% of of board gamers may typically have between 26 to 100+ games and so, often, space becomes an issue.  This has led to a large scene for selling on games that are no longer played enough or just did not click with a gamer or gaming group.  You can now find popular and relatively recent releases available on ebay and there is a 2nd hand games facility available on boardgamegeek and many facebook groups where gamers can sell or trade games.

------

> # **STRATEGY**

Research has revealed that there is no current dedicated online board game store that will allow users to sell games in exchange for store credit.  Boardgame Bazaar uniquely offers this facility to registered site users and manages the end to end sale process through the users account and admin interface.  This allows users to build up credit to spend in store and will also provide Boardgame Bazaar with quality 2nd hand stock to sell longside new stock of the latest games and well known titles.

The goal of this project is to produce a MVP of an e-commerce store dedicated to the sale of new and second hand table top board games.  

# User Stories

| User Story ID | As A        | I want to be able to...                                      | So that I can..                                              |
| ------------- | ----------- | ------------------------------------------------------------ | ------------------------------------------------------------ |
|               |             |                                                              |                                                              |
| 01-01         | Customer    | View all of the products available from the store            | Select a product to purchase                                 |
| 01-02         | Customer    | View a list of products that are on sale, just released and available for preorder | Take advantage of savings, and purchase a new product early  |
| 01-03         | Customer    | View second hand board games available to buy                | Have the option to buy quality approved second hand board games |
| 01-04         | Customer    | Select individual products to view                           | Read additional product details to confirm that this is the item I am looking for and add to my shopping cart (nth: view reviews and ratings on the product) |
| 01-05         | Customer    | Access my shopping cart at any time                          | Check added items and view the purchase total to ensure that I am not spending too much |
|               |             |                                                              |                                                              |
| 02-01         | Customer    | View the products available by board game genres             | More easily find games that match my board game preferences  |
| 02-02         | Customer    | Sort the returned list of board games                        | Easily identify the cheapest/most expensive board games and most highly rated |
| 02-03         | Customer    | Be able to search for a board game by name or description    | Find a specific board game that I am looking to purchase     |
| 02-04         | Customer    | Easily view the search results and number of results         | Quickly determine whether the product I want is available    |
|               |             |                                                              |                                                              |
| 03-01         | Customer    | Easily select the quantity of a board game I would like to buy | Buy multiples of one product in the same purchase            |
| 03-02         | Customer    | View the items in the shopping cart that I have selected to purchase | Keep track of what I have added and the total cost           |
| 03-03         | Customer    | Adjust the quantity of the individual items in my shopping cart and remove them if I wish | Easily make changes to my purchase before checkout           |
| 03-04         | Customer    | Easily enter delivery and payment information                | Check out quickly and confidently with zero hassle           |
| 03-05         | Customer    | Feel that my personal and payment information is safe and secure | Confidently provide the needed information to make a purchase |
| 03-06         | Customer    | View an order after a purchase is made and checkout is complete | Verify that I have not made any mistakes in my order         |
| 03-07         | Customer    | Receive an email confirmation after checkout is complete     | Have a record of what has been purchased should there be any issues |
|               |             |                                                              |                                                              |
| 04-01         | Site User   | Easily register for an account                               | Have a personal account, a profile to view and streamline the checkout |
| 04-02         | Site User   | Easily log in or log out                                     | Access my personal account and streamline the checkout       |
| 04-03         | Site User   | Easily recover my password in case I forget it               | Recover access to my account                                 |
| 04-04         | Site User   | Receive an email confirmation after registering              | Be sure that my account is created and verify that it is myself that set it up |
| 04-05         | Site User   | Sell board games I no longer want to get store credit        | Use that credit to buy new or used board game and therefore reduce the amount of money I spend |
| 04-06         | Site User   | Have a personalised account page                             | View order history, save, view and update contact and delivery information and view my current credit and trade progress / history |
|               |             |                                                              |                                                              |
| 05-01         | Store Owner | Add a product                                                | Add new items to the store through streamlined interface     |
| 05-02         | Store Owner | Edit and Update a product details                            | Change product prices, descriptions, images, and other product criteria |
| 05-03         | Store Owner | Delete a product                                             | Remove items that are no longer available to buy             |
| 05-04         | Store Owner | Manage customer sale of games to the store                   | Reject sales, make offers, dispatch pickup, and add the games to stock when they arrive |

------

> # **SCOPE**

# Content

## The presentation of the site is concerned with:

## Functional Requirements
1. Mobile first; the site is designed to work on mobile and tablet screens first, but responsive design ensures that it scales up and looks good on laptop and desktop screens.
2. Flexible Navbar and site options to reflect a logged in user and admin user to restrict some functionality of the website.
3. A contact function/form that will allow the sending of feedback to an existing email.
4. Clear and obvious links to social media platforms.
5. Feedback animations to provide players with clear interaction cues.
6. Nice to have: Interactive functions for user to provide feedback on a recipe and to view feedback provided by others.


------

> # **STRUCTURE**

The website is broadly separated into three sections:

1. Sections and functions accessible whilst not being logged in:

2. Sections and functions accessible when registered and logged in:

3. Sections and functions accessible when logged in as an admin user:

# Navigation

## Navbar
The Navbar is displayed at all resolutions and is a permanet navigation feature.

### Social Icons
- Social icons link to there respective sites and open the social network site within a new browser tab.  
- Displayed in navbar on desktop screens only.

### Account Buttons
- Conditional display of icons and type to login, register, access account, admin functions and logout.  Each navigates to the appropriate page.  
- Displayed in navbar at all resolutions though type is not shown on mobile screens; only the icons.

### Shopping Cart
- Shopping cart that opens the cart (bootstrap implemented feature here).  From the (bootstrap implemented feature here) a 'checkout button takes the user to the checkout page.
- The Shopping cart is displayed at all resolutions.

### Navigation Menu
- Navigation menu displaying 'home' icon to navigate the user to the landing pages from any page within the site.  
- Shop Front displays a drop-down menu that displays the available boardgames by 'bestsellers', 'new releases', 'pre-orders', 'on sale' and 'used'.  
- Shop by Genre displays a drop-down menu that displays the available boardgames by genres that have been assigned to each game.
- The navigation menu is responsive and so content collapses behind a button on tablet and mobile screens

### Brand Logo
- Clicking or tapping the brand navigates the user to the landing pages from any page within the site. 
- The logo is displayed at all resolutions.

### Search Bar
- The search bar will return any boardgames that contain the user input search parameter in the product title or description.
- Displayed as a bar at desktop resolutions and as a button at tablet and mobile resolutions.  Button is tapped to display a search bar.

## Products

### Product Display
- Clicking or tapping on the product image navigates the user to the product detail page for that product

### Product Detail page
- Genre tags are displayed below the product price which allows the user to see other board games within the same genres assigned to the product they are viewing.
- Keep shopping button takes the user to the home page.

## Shopping Cart

## Checkout Page

## login & Register

## Account Page

## Admin Page

## Footer


# Database Schema

![database_schema v0.1](assets/readme/boardgame_bazaar-database_design_v0.1.png)

# Searching

------

# Consistent Features between pages

------

> # **SKELETON**

# Wireframes
[wireframes_v0.1](assets/readme/boardgame-bazaar_desktop-wireframes_v0.1.pdf)

------

> # **SURFACE**

# Theme

# Colours
In order to simplify the deployment of the website, bootstrap colours have been used as detailed below:

| Bootstrap colour | #hex code |
|------------------|-----------|
| Secondary        | #6C757D   |
| Danger           | #DC3545   |
| Warning          | #FFC107   |
| Light            | #F8F9FA   |
| Dark             | #212529   |

![Colour Palette](assets/readme/boardgame_bazaar-colour_palette.png)

# Text

## Fonts
- [Love Ya Like A Sister](https://fonts.google.com/specimen/Love+Ya+Like+A+Sister?preview.text=Boardgame%20Bazaar&preview.text_type=custom&query=Love): Used for the title of the store in the nav bar
- [Amatic SC](https://fonts.google.com/specimen/Amatic+SC?query=amatic&preview.text=Buy,%20Sell,%20Play&preview.text_type=custom): Used for the store tag line 'Buy, Sell, Play' on the nav bar
- [Economica](https://fonts.google.com/specimen/Economica?query=economica&preview.text=Boardgame%20Bazaar%20website%20content%20will%20be%20written%20in%20this%20font&preview.text_type=custom): Used for all text througout the site

# User interaction feedback

## Buttons
All buttons change colour upon mouse hover

## Social icons
All social icons change colour and size upon mouse hover

------

> # **TECHNOLOGIES USED**

## Languages

- HTML5
- CSS3
- JavaScript
- Python

## Libraries & Frameworks

- [django web application framework](https://www.djangoproject.com/)
- [Bootstrap v5.1.0](https://getbootstrap.com/)
- [Font Awesome](https://fontawesome.com/)
- [Google Fonts](https://fonts.google.com/)

## Tools

- [Gitpod](https://www.gitpod.io/) - chosen IDE for this project.
- [GitHub](https://github.com/) - for storage and sharing of code remotely.
- [Heroku](https://www.heroku.com/) - Hosting provider for app.
- [Amazon Web Services (AWS)](https://aws.amazon.com/) - for hosting of all image files
- [allauth](https://django-allauth.readthedocs.io/en/latest/index.html) - for site user login and logout of account
- [Balsamiq](https://balsamiq.com/) - to create wireframes.
- [Lucidchart](https://www.lucidchart.com/) - for DB design illustration.
- [Tables Generator](https://www.tablesgenerator.com)
- [jsonformatter.org](https://jsonformatter.org/) - creating json fixture files.
- [favicon](https://favicon.io/) - for generating 32x32 favicon.
- [Am I responsive](http://ami.responsivedesign.is/) - to create the responsive illustrations featured in the TESTING.md.

------

> # **TESTING**

Testing completed is detailed in the [TESTING.md](https://github.com/C-Undritz/Community-Treats/blob/master/TESTING.md) document

ADD TO TESTING DOCUMENT WHEN CREATED:

Issue: When deleting orders within the admin the error "'>=' not supported between instances of 'NoneType' and 'int'" was returned.
Solution: It was found that this was an issue with the def update_total(self) function within the Order Model.  Upon delete the variable 'quantity_total' was 'None'.  It was understood to be due to the fact that the save function on the OrderLineItem model executes first which initiates the update_total function on the Order model and therefore there would be no line items to iterate through as they would have been deleted and the value therefore 'None'.  To solve this and allow a delete to occur, an if statement was added (line 58) before the discount is determined (lines 59 to 64) to determine if quanity_total has a value and the discount determined only if this is true.

------

> # **NOTED DESIGN CHANGES**

# Changes to original design

# New features



------

> # **FEATURES**

# Security

# Data Management and Use
## Product attributes:
### New Releases.
Determined during site startup and when ‘new releases’ selected from the shop front menu through the function ‘determine_new_releases()’ In home app views.py.   

#### Mechanism:
Function checks the recorded release date mandatory field against the date 90 days in the past from the current date.  If the release of the game occurred within the past 90 days then it is checked as being a ‘new release’.

#### Display:
Only games that were released within the last 90 days will be checked as a new release and therefore displayed as such on the website with a banner over the image.

### Pre-orders.
Determined during site startup and when ‘pre-orders’ selected from the shop front menu through the function ‘determine_preorders()’ In home app views.py.   

#### Mechanism: 
function checks the recorded release date mandatory field against the current date.  If the release date of the game is in the future then it is checked as being a ‘pre-order’.

#### Display:
Only games that have a release date recorded in the database that is in the future will be checked as a preorder and therefore displayed as such on the website with a banner over the image.


### Stock.
The stock figure is updated when an item is purchased to reflect the amount purchased.  There are no controls to stop the 'stock' count becoming a minus figure as this should be allowed to highlight if more stock has been sold than is in place.  However there are a number of measures in place to prevent this from happening.

1. To keep the customer informed, the current stock is displayed to the customer along with the product, both on the home page and on the product detail.  If there is over 10 in stock stock then '10+ in stock' is displayed.  If stock is 10 or below, then the actual figure is displayed to the customer as 'X in stock.  If there is no stock then, 'in stock soon' is displayed on the home screen and 'Sorry, currently out of sttock' is displayed within the product detail.  Additionally; to stop the sale of products with no stock, the quantity selector and 'add to cart' button are not displayed.

2. The stock figure is also used to limit the amount a customer can buy at once by affecting the maximum number that can be selected.  If the product stock is more than 9 then the most of any product a customer can buy at once is 10.  However should the current stock fall below 10 then then limit on the quantity selector is set by the current stock number. 

3. At the point of purchase when the customer clicks/taps on the 'complete order' button on the checkout screen, a realtime check is made against the current stock level of each product in the basket and the intended purchase amount. If any of the items purchased quantity is more than the stock figure for that item, the purchase fails and the customer is directed back back to the cart screen.  A message is also displayed explaining this and asks for the customer to recheck the displayed stock levels for their purchase(s).  This is to catch instances where a customer has been able to add items to their cart, but may be slow to checkout and remaining stock has been sold in the meantime.








------

> # **FURTHER DEVELOPMENT**



------

> # **DEVELOPMENT AND DEPLOYMENT**

# Deploy to Heroku



------

> # **DOCUMENTATION REFERENCED**



------

> # **CREDITS AND THANKS**

# Code
- For rendering the game genres as checkboxes: [Django Forms for Many-to-Many Fields](https://medium.com/swlh/django-forms-for-many-to-many-fields-d977dec4b024)
- To get a calender box to show up to pick a date for the 'release date' field in the add products page: [How to use Datepicker in Django?](https://webpedia.net/how-to-use-datepicker-in-django)

# Images and Content

## Images
- stripe logo badge used in accordance with [Stripe Marks Usage Agreement](https://stripe.com/en-gb/marks/legal)


## Content

- Information for Readme Overview section was found in the following websites:
  - [Board games: Why are they becoming so popular?](https://www.bbc.co.uk/news/av/uk-wales-49859688)
  - [Board Game Industry Statistics](https://printninja.com/board-game-industry-statistics/)

# Acknowledgments
- Thanks to the slack community for support and help throughout the course and this project.  Honourable mentions for this project go to Ed B_alum, Gaff Alumnus, Daisy_mentor
- Thanks to @ckz8780 for the support on slack and helping with getting the stock check against purchase quantity working!
- Thanks to tutor support for all the help throughout this project
- Thanks to Code Institute for the encouragement and great course material. 
