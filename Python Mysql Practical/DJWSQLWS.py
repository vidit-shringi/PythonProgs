import mysql.connector
from django.db import models

# Connect to the MySQL database
mydb = mysql.connector.connect(
  host="localhost",
  user="yourusername",
  password="yourpassword",
  database="website"
)

# Create a cursor object
mycursor = mydb.cursor()

# Define a model for the website page
class Page(models.Model):
    title = models.CharField(max_length=255)
    content = models.TextField()

    def __str__(self):
        return self.title

# Define a function to insert page information into the database
def insert_page(title, content):
    # Insert the page information into the database
    sql = "INSERT INTO page (title, content) VALUES (%s, %s)"
    val = (title, content)
    mycursor.execute(sql, val)
    mydb.commit()

# Create the Django app
python manage.py startapp website

# Create the Django model migration
python manage.py makemigrations website

# Apply the Django model migration
python manage.py migrate

# Create the Django view for the website page
from django.shortcuts import render
from .models import Page

def page(request, page_id):
    page = Page.objects.get(id=page_id)
    return render(request, 'page.html', {'page': page})

# Create the Django template for the website page
<!DOCTYPE html>
<html>
<head>
    <title>{{ page.title }}</title>
</head>
<body>
    <h1>{{ page.title }}</h1>
    <p>{{ page.content }}</p>
</body>
</html>

I hope this helps you get started with your website. Let me know if you have any questions or need further assistance. 😊

#  Code for sql    #
"""
CREATE DATABASE website;
USE website;
CREATE TABLE page (
    id INT AUTO_INCREMENT PRIMARY KEY,
    title VARCHAR(255),
    content TEXT
);
"""
