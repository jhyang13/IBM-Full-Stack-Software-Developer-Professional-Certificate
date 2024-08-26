from django.db import models

class User(models.Model):
    # CharField for user's first name
    first_name = models.CharField(null=False, max_length=30, default='john')
    # CharField for user's last name
    last_name = models.CharField(null=False, max_length=30, default='doe')
    # CharField for user's date for birth
    dob = models.DateField(null=True)

# python3 manage.py makemigrations orm

# python3 manage.py sqlmigrate orm 0001

# python3 manage.py migrate

# Databases->postgres->Schemas->public->Tables
