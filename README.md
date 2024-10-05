# STARLITE

## Description
**Starlite** is a full-featured online shopping platform where users can browse products, add items to their shopping cart, and complete purchases securely. The platform includes an admin panel for managing products, categories, and orders.

## Features
* **User Registration & Authentication:** Users can register either as a buyer or a seller.

* **Products Managements:** Sellers can add, delete, and update products to their respective stores, while buyers can browse through products and search for specific products.

* **Shopping Cart:** Each buyer gets a unique cart to which they can add products, remove products, or even update an already added product(s).

* **Order Placement:** Each order placed by each user will be tracked independently, and each order will have a set of status (pending, completed, shipped)

* **Checkout process:** After a successful order has been placed the user will be directed to the checkout flow where they select their preferred payment process (bank transfer, card payment, paypal, etc.).

* **Admin Dashboard:** The admin gets a dashboard to monitor both buyers and sellers, and also get real-time statistics on how the business' sales. The admin also has the ability to deactivate or suspend any suspicious account. (more on this later)


## Technologies Used
* **Frontend:** React, Redux, Bootstrap
* **Backend:** Python, Django
* **Database:** PostgreSQL
* **Authentication:** JWT (JSON Web Tokens)
* **Payment Gateway:** PayPal API
* **Deployment:** Heroku


## Getting Started

### Prerequisites
* Python==3.12.3
* Pyasgiref==3.8.1
* Django==5.1.1
* djangorestframework==3.15.2
* sqlparse==0.5.1

### Installation
1. Clone the Repository
    ```bash
    git clone https://github.com/i-am-Shekinah/starlite.git
    ```

2. Navigate to the Directory
    ```bash
    cd starlite.git
    ```

3. Install the necessary dependencies
    ```bash
    python install -r requirements.txt
    ```

4. Running the project
    ```bash
    python manage.py runserver
    ```

## Folder Structure
```ultree

starlite
├── .gitignore
├── LICENSE.txt
├── README.md
├── cart
│   ├── __init__.py
│   ├── admin.py
│   ├── apps.py
│   ├── migrations
│   │   └── __init__.py
│   ├── models.py
│   ├── tests.py
│   └── views.py
├── manage.py
├── order
│   ├── __init__.py
│   ├── admin.py
│   ├── apps.py
│   ├── migrations
│   │   └── __init__.py
│   ├── models.py
│   ├── tests.py
│   └── views.py
├── product_management
│   ├── __init__.py
│   ├── admin.py
│   ├── apps.py
│   ├── migrations
│   │   └── __init__.py
│   ├── models.py
│   ├── tests.py
│   └── views.py
├── requirements.txt
├── starlite
│   ├── __init__.py
│   ├── asgi.py
│   ├── settings.py
│   ├── urls.py
│   └── wsgi.py
└── user_management
    ├── __init__.py
    ├── admin.py
    ├── apps.py
    ├── migrations
    │   └── __init__.py
    ├── models.py
    ├── tests.py
    └── views.py
```


## Contributing
Contributions are welcome! Please follow the steps below to contribute:

1. Fork the repository.
2. Create a new branch (`git checkout -b feature-branch`)
3. Make your changes
4. Commit your changes (`git commit -m 'Add new feature'`)
5. Push to your branch (`git push origin feature-branch`)
6. Open a Pull Request

The ER-D of this project can be found on [draw.io](https://app.diagrams.net/?src=about#G1rp_KeepYkMad-PPlzIRoDdNVwwYQw7Eb#%7B%22pageId%22%3A%22R2lEEEUBdFMjLlhIrx00%22%7D). Feel free to take a look, and share your thoughts.


## License
This project is licensed under the MIT License - see the [LICENSE](LICENSE.txt) file more details.

## Contact Information
For further inquiries, please reach out to me via mail on [MichaelOlatunji.dev@gmail.com](mailto:MichaelOlatunji.dev@gmail.com)