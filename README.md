# Neighborhood

## Author
Caleb bii.
### Description
Neighborhood is web application about different neighborhoods showcasing various bussiness and it also keeps the people in the neighborhood posted on news posts and activities everything happening in your neighborhood.
### Setup and installations
* Clone Project to your machine
* Activate a virtual environment on terminal: source virtual/bin/activate
* Install all the requirements found in requirements file.
* On your terminal run python3.9 manage.py runserver
* Access the live site using the local host provided 
### Prerequisites
* python3.9  
* virtual environment
* pip 
### Clone the Repo 
* git clone https://github.com/Calebbii/Neighborhood.git
* Initialize git and add the remote repository
* git init
* git remote add origin <your-repository-url>
* Create and activate the virtual environment
* python3.9-venv virtual
* source virtual/bin/activate
* Install dependancies
* Install dependancies that will create an environment for the app to run pip install -r requirements.txt
  
### Run The App 
* python3.9 manage.py check
* python manage.py makemigrations news
* python3.9 manage.py sqlmigrate news 0001
* python3.9 manage.py migrate
* python3.9 manage.py runserver 
* Open localhost:5000

### Testing the Application
python3.9 manager.py tests

### Known Bugs
* There are no known bugs at the moment.  

### Built With 
* Python3.9
* Flask
* Boostrap
* HTML
* CSS
### License
[MIT Lisence](https://github.com/Calebbii/Neighborhood/blob/master/LICENSE) Copyright (c) 2021 Calebbii.
