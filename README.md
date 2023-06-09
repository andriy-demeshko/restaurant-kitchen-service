# ChefConnect

Restaurant kitchen service Django project to improve interaction between cooks and create new dishes and dishes types

## Check it out!

[Restaurant Kitchen Service project deployed to Render](https://restaurant-kitchen-service-tum5.onrender.com)

## Installation

Python3 must be already installed

```shell
git clone https://github.com/andriy-demeshko/restaurant-kitchen-service
cd restaurant_kitchen_service
python -m venv venv
venv\Scripts\activate
pip install -r requirements.txt

create file .env with vars:  # Set Environment Variables
DJANGO_SECRET_KEY=<your Django secret key>
DATABASE_URL=<postgres://user:pass@localhost:5432/test>  # your Postgres URL
DJANGO_DEBUG=False

python manage.py migrate
python manage.py runserver  # starts Django server

You can use the following test user to test the functionality of the site:
login: user
password: user12345

Or create a super-user — python manage.py createsuperuser
```

## Features

* Authentication functionality for Cook/User
* Managing cooks & dishes directly from website interface
* Powerful admin panel for advanced managing

## DB Structure

![](for_readme/db-structure.png)

## Page examples

Login page
![Website Interface](for_readme/login.png)

Registration page
![Website Interface](for_readme/registration.png)

Home page
![Website Interface](for_readme/home.png)

Dishes types list page
![Website Interface](for_readme/dishes_types_list.png)

Dishes list page
![Website Interface](for_readme/dishes_list.png)

Cooks list page
![Website Interface](for_readme/cooks_list.png)

Dishes types details page
![Website Interface](for_readme/dishes_types_details.png)

Dishes details page
![Website Interface](for_readme/dishes_details.png)

Cooks details page
![Website Interface](for_readme/cooks_details.png)
