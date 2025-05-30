# Todo Space

## A Task management web app that tracks user habits, allows them to add tasks, view calendar and use the famous pomodoro focus timer







# How to collaborate
Follow these instructions to get a local copy of this project up and running on your machine.

## Prerequisites
Ensure you have the following installed on your system.

- Python: Version 3.9 or higher (https://www.python.org/downloads/)
- pip: Python package installer (usually included with Python)
- Django: Version 4.x (https://docs.djangoproject.com/en/stable/intro/install/)
- A Database: PostgreSQL is recommended for production, but SQLite can be used for development. Ensure you have the necessary drivers installed if using PostgreSQL or MySQL.
- Git For version control (https://git-scm.com/downloads)


## Installation

- 1. Clone the repository:
``` git clone https://github.com/tomi3-11/Todo-Space
	cd Todo-Space
```

- 2. Create and activate a virtual environment:
``` python -m venv venv
	# On macOS/Linux
	source venv/bin/activate
	# On windows
	venv\Scripts\activate # Command Prompt
	venv\Scripts\Activate # Powershell
```

- 3. Install the project dependencies:
``` pip install -r requirements.txt ```  
## Configuration
- 1. Database Setup:
	- Configure your database settings in the ```Todo-Space/settings.py``` file. Update the ```DATABASES``` dictionary with your database credentials.
	- Run datbase migrations to create the necessary tables:
	```python manage.py makemigrations todoappp```
	```python manage.py migrate```
	- Create a superuser to access the Django admin panel:
	```python manage.py createsuperuser```

## Running the Development Server
To run the standard Django devlopment server:
``` python manage.py runserver ```