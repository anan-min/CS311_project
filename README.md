Sure, I can help you create a README file for your GitHub repository based on the information you provided. Here's a basic template you can use:

---

# ShopNow

ShopNow is a desktop e-commerce application developed as part of the CS311: Computer Programming II course at Bangkok University.

## Table of Contents

1. [Introduction](#introduction)
   - [Project Name](#project-name)
   - [Objectives](#objectives)
   - [Scope](#scope)
2. [Application Functionality](#application-functionality)
   - [Flowchart](#flowchart)
     - [Authentication](#authentication)
     - [Add to Cart](#add-to-cart)
     - [Confirm Payment](#confirm-payment)
     - [Browsing](#browsing)
3. [Appendix](#appendix)
   - [Source Code (.py)](#source-code-py)

## Introduction

### Project Name

ShopNow - An e-commerce application for managing products, orders, and payments.

### Objectives

The project aims to develop a desktop application for buying and selling products. It focuses on enhancing programming skills using Python, supporting functions such as adding or changing products in the cart, creating and signing in to accounts, recording payment information, and adding products for sale in the store.

### Scope

The project involves developing a desktop e-commerce application divided into authentication, add_to_cart, confirm_payment, and browsing functionalities.

## Application Functionality

### Flowchart

#### Authentication
- Register or log in with user-entered information.
- If the user enters incomplete or unusable information in the form, they will be alerted and the user's typing will be moved to the relevant form. 
- Data used to enter the system includes username and password. Data used to register include username, fullname, password, email, and address.

#### Add to Cart
- Add products and quantities to be purchased to the cart. If the quantity is less than one, the product will not be added to the customer's cart.

#### Confirm Payment
- Receive payment information including transfer amount and transfer time to confirm payment via the store's QR code displayed on the left side of the Payment page.

#### Browsing
- Display products, orders, and payments using drop-down menus to select pages. If there are more items than one page can display, they will be displayed appropriately.
- Products will be displayed 8 items per page and can be clicked to view more details and add to the cart.

## Appendix

### Source Code (.py)
