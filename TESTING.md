# TESTING

## Code validation

### W3C HTML Validator
* Index

![HTML validator result - index page](documentation/testing/validation/index.png)

* Products

![HTML validator result - products page](documentation/testing/validation/products.png)

* Add product

![HTML validator result - add product page](documentation/testing/validation/add.png)

* Add product image

![HTML validator result - add product image page](documentation/testing/validation/add-image.png)

* Edit product

![HTML validator result - edit product page](documentation/testing/validation/edit.png)

* Product detail

![HTML validator result - product detail page](documentation/testing/validation/product-detail.png)

* Bag

![HTML validator result - bag page](documentation/testing/validation/bag.png)

* Checkout

![HTML validator result - checkout page](documentation/testing/validation/checkout.png)

* Checkout success

![HTML validator result - checkout success page](documentation/testing/validation/checkout-success.png)

* Profile

![HTML validator result - profile page](documentation/testing/validation/profile.png)

* Edit address

![HTML validator result - edit page](documentation/testing/validation/edit-address.png)

* Wishlist

![HTML validator result - wishlist page](documentation/testing/validation/wishlist.png)

* Sign up 

![HTML validator result - signup page](documentation/testing/validation/sign-up.png)

* Sign in

![HTML validator result - signin page](documentation/testing/validation/sign-in.png)

### W3C CSS Validator

![CSS validator result](documentation/testing/validation/css-validator.png)

### JSHINT Javascript Validator

![JSHINT results - bag](documentation/testing/validation/jshint/bag.png)

![JSHINT results - product detail](documentation/testing/validation/jshint/product-detail.png)

![JSHINT results - product management](documentation/testing/validation/jshint/product-management.png)

![JSHINT results - products](documentation/testing/validation/jshint/products.png)

![JSHINT results - quantity input script](documentation/testing/validation/jshint/quantity-input-script.png)

![JSHINT results - stripe elements](documentation/testing/validation/jshint/stripe-elements.png)

### Python Validator

* I have checked all Python documents using flake8 to ensure they are compliant.
* I left the code which I did not write 

## Lighthouse reports

* Index page

![Lighthouse validator result - index page](documentation/testing/validation/lighthouse/index.png)

* Products

![Lighthouse validator result - products page](documentation/testing/validation/lighthouse/products.png)

* Add product

![Lighthouse validator result - add product page](documentation/testing/validation/lighthouse/add-product.png)

* add product image

![Lighthouse validator result - add product image page](documentation/testing/validation/lighthouse/add-image.png)

* Edit product

![Lighthouse validator result - edit product page](documentation/testing/validation/lighthouse/edit-product.png)

* Product detail

![Lighthouse validator result - product detail page](documentation/testing/validation/lighthouse/product-detail.png)

* Bag

![Lighthouse validator result - bag page](documentation/testing/validation/lighthouse/bag.png)

* Checkout

![Lighthouse validator result - checkout page](documentation/testing/validation/lighthouse/checkout.png)

* Order history

![Lighthouse validator result - order history page](documentation/testing/validation/lighthouse/order-history.png)

* Profile

![Lighthouse validator result - profile page](documentation/testing/validation/lighthouse/profile.png)

* Edit address

![Lighthouse validator result - edit address page](documentation/testing/validation/lighthouse/edit-address.png)

* Wishlist

![Lighthouse validator result - wishlist page](documentation/testing/validation/lighthouse/wishlist.png)

* Sign up 

![Lighthouse validator result - add product image page](documentation/testing/validation/lighthouse/sign-up.png)

* Sign in

![Lighthouse validator result - sign in page](documentation/testing/validation/lighthouse/sign-in.png)

## Responsiveness testing
* Responsiveness testing was carried out on Chrome devtools
* The website was tested on 3 browsers: Firefox, Chrome and Opera to make sure they work correctly

## Manual testing
### Navbar and footer
* The navigation links have been tested and worked. The navbar switches to mobile view for smaller screens 
* The social links in the footer have been tested and work

### Homepage
* The links to product category correctly lead to products page and filter by category
* The hero image changes for mobile view

### All products and filters
* The filters have been tested and work
* Reset filters also work as desired
* Links are working correctly

### Search
* Search bar works correctly
* Empty search works

### Products details page
* All buttons work as desired
* The edit and delete product link works when tested
* Images are enlarged when clicked on

### Bag
* Users can add and remove items
* Buttons work as expected

### Checkout
* Signed in users can save their address to their profile
* Successful orders are added to user profile page and users are taken to the checkout success page

### Profile page
* Users can add, edit and remove their addresses
* Links to order history works

### Wishlist page
* Users can remove items from their wishlist successfully

### User authentification
* Users can sign up, sign in and sign out sucessfully
* New users will recieve an email to authenticate their email address

### Product management
* Admin can successfully add a new product with images

## Bugs

### Updating images for product

* I attempted to create a form to allow admin to edit any extra images stored or each product through the website. However this proved difficult as the form would not be populated with the data and any attempt to save to the database would fail. Therefore I decided to discard this feature.

### Pre-populating the checkout form with a default address

* As users can have multiple addresses I tried to populate the checkout form with their selected default address. However this proved problematic since if they are ordering for the first time without an address already saved, there would be an error. This was due to me not filtering the data correctly so I had to use a filter rather than a get statement. Then I could use an if statement to check whther the address exists or not.
