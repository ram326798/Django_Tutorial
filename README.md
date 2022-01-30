# Django_Tutorial


step 1: Install pip

python -m pip install -U pip


Step 2:Install virtual environment

pip install virtualenv
		or
pip install virtualenvwrapper-win

Step 2.1 Create and activating virtual environment

rmvirtualenv test

Step 2.3 To work in existing virtual environment

workon Name

Step 2.4 To delete virtual environment

rmvirtualenv test

Step 3:Install Django

pip install django

Step 4: To create a basic Django application

django-admin startproject projectName

Step 5: Navigate to project folder

cd projectName

Step 6:To run Django application

Python manage.py runserver

Step7 :To create sub application under main application

python manage.py startapp calc

Step 8 : In order to make static folder into django first add that folder in setings.py then give the below command from root directory

python manage.py collectstatic

Step 9: To install sql in your django application

pip install mysql

Step 10: To create tables in database automatically using orm create model and add database details in settings.py

Eg:

class Destination(models.Model):
    name = models.CharField(max_length=100)
    img = models.ImageField(upload_to='pis')
    desc = models.TextField()
    price = models.IntegerField()
    offer = models.BooleanField(default=False)

>then run the below command

python manage.py makemigrations

Step 11:to migrate table into database 

python manage.py sqlmigrate app_name file_name

Step 12:To see in database

python manage.py migrate

Flow:
~~~~
1.project starts from urls.py
2.from there to include urls.
3.from there to views