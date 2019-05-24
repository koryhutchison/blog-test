from django.db import models

# Create your models here.
from django.contrib.auth.models import AbstractUser

class ExampleUser(AbstractUser):
    # id
    # username
    # password
    # first_name
    # last_name
    # password
    # email
    # last_login
    # is_superuser
    # is_staff
    # is_active
    # date_joined
        ###The above and more are fields that are already generated and inherited
        ###from the classes
    phone = models.CharField(max_length=10)