# Community Treats - Testing document

## [Associated Readme document](README.md)

---
# Table of Contents
* [RESPONSIVE DESIGN TESTING](#responsive-design-testing)
* [FUNCTIONALITY TESTING](#functionality-testing)
* [QUALITY CHECKS](#quality-checks)
* [USER STORIES TESTING](#user-stories-testing)
* [PROBLEMS AND FIXES](#problems-and-fixes)
* [REMAINING ISSUES](#remaining-issues)
* [REMAINING BUGS](#remaining-bugs)

---
># **RESPONSIVE DESIGN TESTING**
Research detailed screen resolutions that are most popular today (see [here](https://kinsta.com/blog/responsive-web-design/#common-responsive-breakpoints) and [here](https://www.browserstack.com/guide/responsive-design-breakpoints)).  This information was used along with the required resolutions for [am-i-responsive](http://ami.responsivedesign.is/) to determine 17 resolutions as a guide for media breakpoints and to test for responsive design using Google Chrome DevTools. The resolutions tested were:

    * 1920 x 1080
    * 1600 x 992
    * 1536 x 864
    * 1366 x 768
    * 1280 x 802
    * 1366 x 768
    * 768 x 1024
    * 540 x 720 (Surface Duo)
    * 414 x 896
    * 411 x 731 (Pixel 2)
    * 411 x 823 (Pixel 2 XL)
    * 375 x 812 (iPhone X)
    * 375 x 667 (iPhone 6/7/8)
    * 360 x 720
    * 360 x 640
    * 320 x 568 (iPhone 5)
    * 320 x 480

![Am I Responsive image showing the landing page across four devices of different screen sizes](assets/readme/am_i_responsive_landing_page.png)
![Am I Responsive image showing the product detail page across four devices of different screen sizes](assets/readme/am_i_responsive_product_details.png)
![Am I Responsive image showing the customer account page across four devices of different screen sizes](assets/readme/am_i_responsive_customer_account.png)

The responsive design test sheets and results can be viewed using the below link.  

*Note - The test sheet linked below is stored as a single google docs sheet which contains images that do not seem to load in the initial window.   This document is therefore best viewed in Google Sheets once open.*

* [Boardgame Bazaar Responsive Design test results](https://drive.google.com/file/d/1WW3HqHdbh4FxPSX5Nz79_YN6zn9hiIgM/view?usp=sharing)

For each resolution each page was tested to ensure that all text can be viewed and that all features of the page can be seen and do not overlap.

Also successfully tested the live site on the following devices:
* Huawei P smart 2019 smart phone
* Samsung A12 smart phone 
* Laptop at 1920 x 1080 resolution
* Amazon Fire HD 8 tablet
* Apple iPad 7th Generation
* Apple iPhone 8

---
># **FUNCTIONALITY TESTING**
Functionality testing of all of the implemented CRUD functionality was completed.  This was conducted on a desktop PC using Google Chrome dev tools.

*Note - The test sheets are linked below and are stored as google docs sheet.  Most of these files have mulitple tabs for each function so please do check to see the full range of tests completed.  Some of these also have images and are therefore best viewed in Google Sheets once open.*

The functionality test sheets and results can be viewed using the below links:
* [CREATE](https://drive.google.com/file/d/1RbawwFMKYuLDV1O0xnDrTe-lKLN1lYJu/view?usp=sharing)
* [READ](https://drive.google.com/file/d/11SzVZ2177d3hsJoUb8Y4LBBZHLew9a2q/view?usp=sharing)
* [UPDATE](https://drive.google.com/file/d/15f0skkOKx_7S72A-npP7XqQpiYzEqGtD/view?usp=sharing)
* [DELETE](https://drive.google.com/file/d/1cyloMQR1OJoU0xTZgKkvgPffjscJOqdY/view?usp=sharing)

># **SECURITY TESTING**
Security testing was conducted to test that any areas of the website that require a login or admin privileges cannot be accessed by manipulation of the url. 

*Note - The test sheet linked below is stored as a single google docs sheet with two tabs and is best viewed in Google Sheets once open.*

The security test sheet and results can be viewed using the below link:
* [Security tests](https://drive.google.com/file/d/1ArQhNUNXUrGTEk0enZY-GvhWzcjV3lQo/view?usp=sharing)  

---
># **QUALITY CHECKS**
# Approach
## CSS style sheet:
The following quality checks were completed on the css style sheet (style.css):
* Manual review on comments against code to ensure relevancy.
* Manual review to ensure all quoted-out code was removed.
* Manual check of the spacing between code lines.
* Code run through [Autoprefixer](https://autoprefixer.github.io/) to ensure compatibility across browsers.
* Code checked on [W3C CSS validation](https://jigsaw.w3.org/css-validator/) using direct input.

## HTML:
The following quality checks were completed on each of the four HTML files:
* Manual review on comments against code to ensure relevancy.
* Manual review to ensure all quoted-out code was removed.
* Manual check of the spacing between code lines.
* Code checked on [W3C Markup Validation](https://validator.w3.org/) using direct input.  Due to the django template code within the HTML this was done by opening each page, right clicking and selecting 'view page source', and then copying the HTML code displayed for direct input.

## JavaScript:
The following quality checks were completed on each of JavaScript files:
* Manual review on comments against code to ensure relevancy.
* Manual review to ensure all quoted-out code was removed.
* Manual check to ensure that all console.log entries were removed.
* Manual check of the spacing between code lines.
* Code checked on [JSHint](https://jshint.com/) using direct input.  Note that '//jshint esversion: 6' was entered at the top of the code window prior to pasting in JS code. This ensures that the feedback received from JSHint takes into account that the JS code uses ECMAScript 6 specific syntax.  '/*globals $:false */' was also added when using JSHint to check jQuery.

## Python:
The following quality checks were completed on the app.py file:
* Manual review on comments against code to ensure relevancy.
* Manual review to ensure all quoted-out code was removed.
* Manual check to ensure that all print() entries were removed.
* Manual check of the spacing between code lines.
* Addressing all PEP8 non-compliancy flags in Gitpod.
* Code checked on [pep8online.com](http://pep8online.com/).

## Website performance:
The site performance was tested on the following browsers by using Lighthouse :
* Chrome
* Opera
* Edge
* Firefox

N.B: Internet Explorer was not tested as the site uses ES6 so it's not fully compatible with Internet Explorer builds.

---
# Results
## W3C CSS Validation:

## W3C Markup Validation:

## JSHint:

## Python PEP8:

## Lighthouse results:
### Chrome:
![Chrome Lighthouse results]()
### Opera:
![Opera Lighthouse results]()
### Microsoft Edge:
![Edge Lighthouse results]()
### Firefox:
![Firefox Lighthouse results]()

Brief testing on Safari browser was conducted by using the website on a relatives iPad.  The website functioned as expected and no problems observed.

---
># **USER STORIES TESTING**
The below details how the website meets the requirements of each user story. 

# Business Owner

# First time user of the software:

# Returning user of the software:
---
># **PROBLEMS AND FIXES**

## 1. Deleting an Order
**Issue**: When deleting orders within the admin the error "'>=' not supported between instances of 'NoneType' and 'int'" was returned.  
***Solution**: It was found that this was an issue with the def update_total(self) function within the Order Model.  Upon delete the variable 'quantity_total' was 'None'.  It was understood to be due to the fact that the save function on the OrderLineItem model executes first which initiates the update_total function on the Order model and therefore there would be no line items to iterate through as they would have been deleted and the value therefore 'None'.  To solve this and allow a delete to occur, an if statement was added (line 58) before the discount is determined (lines 59 to 64) to determine if quanity_total has a value and the discount determined only if this is true.*

## 2. Displaying rating stars 
**Issue**: The code for the rating stars was the same custom code from my other project 'Community Treats'.  However here when the stars were rendered, the radio buttons were also showing:  
![Ratings stars display issue](assets/readme/rating_stars_issue.png)  
***Solution**: a similar question was asked on [stackoverflow](https://stackoverflow.com/questions/29346385/hide-radio-button-while-keeping-its-functionality/29346555) and one of the answers featured on the page detailed the below css fix which, when applied, solved the issue:*
```
.radio_item {
    position: fixed; 
    opacity: 0;
}
```
![Ratings stars display issue](assets/readme/rating_stars_fix.png)  

## 4. Restricting interaction with the quantity select input box
**Issue**: Within the product detail page and the cart page, it was found that the customer could use the keyboard to enter any number above the stock limit of the input max figure of 10.  it was also found that the built in increment and decrement mouse functions could be used to select a figure above the stock level (should it be less than 10), to the max of 10.  
***Solution**: To limit how the customer can interact with the quantity selector inputs, the ability to use the built in increment and decrement functions and the keyboard was limited (see code section in credit and thanks).  This will then direct the customer to use the custom mobile friendly increment and decrement functions.*

## 5. Form input elements affected by mouse wheel
**Issue**: It was found when entering a number value into any form input element and then scrolling the mouse wheel to navigate the form changed the input value (up or down depending on the scroll wheel direction) whilst the cursor was briefly still within the input box.  Therefore when making a price entry of 69.99 it would be very easy to make it then appear as 69.97 or 69.98.  
***Solution**: This was solved by disabling the mousewheel for all input elements throughout the site.  The jQuery solution was found [here](https://stackoverflow.com/questions/9712295/disable-scrolling-on-input-type-number)*



---
># **REMAINING ISSUES**



># **REMAINING BUGS**
 