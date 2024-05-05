## Manual Testing Guide

### Global Features

| Feature              | Action                                                   | Expected Result                                                   |
|----------------------|----------------------------------------------------------|-------------------------------------------------------------------|
| Global Navigation    | Click on each navigation link                            | Correct navigation to the respective page or section.             |
| Logo/Home            | Click on the 'Fitness Forge' logo                        | Redirects to the homepage.                                        |
| Search Functionality | Enter a query in the search bar and press enter          | Displays relevant products or content based on the search query.  |
| All Products         | Hover over the 'All Products' dropdown                   | Dropdown displays options: "By Category," "By Rating," "By Price."|
| Adventures           | Hover over the 'Adventures' dropdown                     | Dropdown displays sub-categories: "Hiking Trails," "Water Adventures," "Camping Spots." |
| Sports Events        | Hover over the 'Sports Events' dropdown                  | Dropdown displays categories: "Try-Out Sessions," "Amateur Tournaments," "Health and Fitness Classes." |
| Special Offers       | Hover over the 'Special Offers' dropdown                 | Dropdown displays "Adventure Packages."                           |
| My Account           | Click on the 'My Account' link                           | Prompts login/signup if not logged in, or displays the user's account page if logged in. |
| Shopping Cart        | Click on the cart icon                                   | Displays an empty cart with a message "No items in your cart" if no items have been added. |
| FAQ                  | Click on the 'FAQ' link                                  | Navigates to the FAQ page where frequently asked questions are addressed. |
| Privacy Policy       | Click on the 'Privacy policy' link                       | Navigates to the privacy policy page detailing the site's privacy practices. |
| Footer Links         | Click on any link in the footer                          | Navigates correctly to its respective page or external site.       |
| Accessibility        | Test all features for accessibility using a screen reader | All features fully accessible with screen readers, all images have descriptive alt texts. |


### 404 Error Page

Test the behavior of the site when users encounter a broken link or non-existent page.

| **Feature**        | **Action**                                                          | **Expected Result**                                            |
|--------------------|---------------------------------------------------------------------|----------------------------------------------------------------|
| Custom 404 page    | Append a faulty extension to the home URL (e.g., `/404`).           | User is directed to a customized 404 error page, which informs them of an invalid URL and includes a "Back to Homepage" button. |


### 500 Internal Server Error Page

Test the behavior of the site under scenarios that may trigger an internal server error.

| **Feature**          | **Action**                                                        | **Expected Result**                                              |
|----------------------|-------------------------------------------------------------------|------------------------------------------------------------------|
| 500 Error page       | Trigger a server error by simulating a failure in the backend (Note: This may involve actions like interrupting database access, causing a script to fail, or other actions that should only be performed in a controlled testing environment). | User is directed to a custom 500 error page, which informs them that something went wrong and includes a message encouraging them to try again later or contact support. The page should also include a "Back to Homepage" button or similar navigation aid. |


### Home Page Interactions

Ensure that the home page's interactive elements function correctly and lead users to the expected destinations.

| **Feature**        | **Action**                                                          | **Expected Result**                                            |
|--------------------|---------------------------------------------------------------------|----------------------------------------------------------------|
| Buy Live Poultry button | Click the "Give it a try" button located on the homepage.          | Users are directed to the all products page, listing all available categories. |

### Product Page Interactions

Verify that the product page provides a seamless experience when interacting with product listings.

| **Feature**        | **Action**                                                          | **Expected Result**                                            |
|--------------------|---------------------------------------------------------------------|----------------------------------------------------------------|
| Product hover effect | Hover over any product.                                            | The product is highlighted, indicating it is selected.         |
| Product detail     | Click on any product.                                               | Opens the product detail page.                                 |
| Sort functionality | Use the "sort by" feature with options like price, popularity, etc. | Products are sorted according to the selected criterion.       |
| Back to products button | Click the "back to products" button on the product detail page.   | Navigates back to the main product listing page.               |

### Product Detail Page Interactions

Test the functionalities that allow users to interact with product details, customize their choices, and engage with the community.

| **Feature**          | **Action**                                                        | **Expected Result**                                              |
|----------------------|-------------------------------------------------------------------|------------------------------------------------------------------|
| Increase Quantity    | Click the "+" button to increase the quantity of the product.     | The quantity displayed increments accordingly.                  |
| Customize Product    | Select options or enter data into form fields for customization.  | Selections or inputs reflect in shopping bag. Toast message success is shown |
| Comments Section     | Scroll to the comments section, type a comment, and submit.       | The new comment appears in the comment section.|
| Decrease Quantity     | Click the "-" button to decrease the quantity of the product.      | The quantity displayed decrements accordingly. If the quantity is at its minimum limit, it does not decrease further. |
| Add to Wishlist       | Click the "Add to Wishlist" button on the product detail page.     | The product should be added to the user's wishlist. A confirmation message indicates that the addition was successful. |

### Add to Bag

| **Feature**          | **Action**                                                        | **Expected Result**                                              |
|----------------------|-------------------------------------------------------------------|------------------------------------------------------------------|
| Toast Message on Add to Cart | Add an item to the shopping cart.                            | A toast message appears confirming the item has been added, with a link or button that says "Go to Secure Checkout." |
| Secure Checkout Navigation | Click on the "Go to Secure Checkout" link or button in the toast message. | The user is directed to the bag to check again the content |
| Fail to Add Product  | Attempt to add a product to the cart with an error (e.g., product out of stock). | An error toast message appears indicating the product cannot be added. |
| Info Message on Product Addition | Add a product that has specific requirements or notices (e.g., age restrictions, additional processing time). | An informational toast message appears detailing the specific requirements or notices for the product. |


### Shopping Bag Interaction Tests

This section details the tests for interactive features within the shopping bag, ensuring users can manage their cart items and navigate effectively.

| **Feature**          | **Action**                                                        | **Expected Result**                                              |
|----------------------|-------------------------------------------------------------------|------------------------------------------------------------------|
| Remove Item Button   | Click the "Remove Item" button next to an item in the shopping bag. | The item is immediately removed from the shopping bag. The cart updates to reflect the change, including the total price adjustment. |
| Keep Shopping Button | Click the "Keep Shopping" button in the shopping bag.              | Redirects the user back to the product listing or the last visited product category page, allowing for continued shopping. |
| Secure Checkout Button| Click the "Secure Checkout" button in the shopping bag.           | Navigates the user to a secure checkout page where personal and payment details can be safely entered to complete the purchase. |

### Checkout Page Interaction Tests

This section provides detailed testing instructions for the checkout page, focusing on form fields, address options, user preferences, and payment processing.

| **Feature**                          | **Action**                                                           | **Expected Result**                                               |
|--------------------------------------|----------------------------------------------------------------------|-------------------------------------------------------------------|
| Customer Data Form                   | Fill in the customer data form with necessary information.           | All entered data is accepted and validated without errors.        |
| Billing Address Checkbox             | Tick the checkbox if billing address is different from the delivery address. | Additional form fields appear for entering the billing address.   |
| Save Delivery Info Checkbox          | Tick the checkbox to save delivery information to the user profile.  | Upon completion of the order, delivery information is saved to the user’s profile for future transactions. |
| Payment Form (Stripe)                | Enter payment details into the form connected with Stripe.           | Payment information is processed securely without storing sensitive details locally. |
| Adjust Bag Button                    | Click the "Adjust Bag" button.                                       | Redirects back to the shopping bag page to allow modifications to the order. |
| Complete Order Button                | Click the "Complete Order" button after filling out all necessary information. | Completes the transaction and redirects to a confirmation page indicating successful order placement. |

### My Profile Page Interactions

This section details the procedures for testing the functionalities available on the "My Profile" page, ensuring that users can effectively manage their information, view their orders, and interact with their wishlist.

| **Feature**                          | **Action**                                                           | **Expected Result**                                               |
|--------------------------------------|----------------------------------------------------------------------|-------------------------------------------------------------------|
| Update Customer Data                 | Fill out the form to update customer data and click the "Update Information" button. | Customer data is updated successfully, and a confirmation message appears. |
| View Order History                   | Click on a linked order number.                                      | Redirects to the detailed page for that specific order, displaying all relevant information about the order. |
| Manage Wishlist                      | Click the delete option next to a product in the wishlist.           | The product is removed from the wishlist, and the list updates immediately to reflect this change. |

### Admin Panel Product Management Interactions

This section outlines the steps for testing the product management functionalities that allow admin users to add new products via a form. Ensure that all actions, validations, and results are thoroughly tested to confirm that the system behaves as expected.

| **Feature**                    | **Action**                                                          | **Expected Result**                                               |
|--------------------------------|---------------------------------------------------------------------|-------------------------------------------------------------------|
| Add Product                    | Navigate to the product management area. Fill out the product addition form, including necessary details like product name, description, price, categories, and images. Click the "Add Product" button. | The product is successfully added to the database, and a confirmation message is displayed. The new product should appear in the product listing on the site. |

### Visual and Responsive Tests

| **Feature**          | **Action**                                                   | **Expected Result**                                           |
|----------------------|--------------------------------------------------------------|---------------------------------------------------------------|
| Responsive Design    | Resize the browser window to different sizes                 | The website adapts appropriately for different device sizes, maintaining usability and layout integrity. |
| Image Loading        | Check all pages for image loading                            | All images load correctly with no broken links.               |
| Dropdown Functionality | Test dropdown functionality on various devices (desktop, tablet, mobile) | Dropdowns function properly across all devices, with categories easy to select and navigate. |

This manual testing guide provides detailed steps to ensure comprehensive coverage of functionality on the product detail page and across the website, confirming that all interactions result in the expected outcomes for an optimal user experience.