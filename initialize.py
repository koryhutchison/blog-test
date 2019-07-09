import django
from django.core import management
from django.db import connection
import os, sys


# ensure the user really wants to do this
confirm = input('''
  Do you want to drop and recreate the entire database?

  Please type 'yes' to confirm the data destruction: ''')
if confirm.lower() != 'yes':
    print()
    print('  exiting')
    sys.exit(1)

# initialize the django environment
os.environ['DJANGO_SETTINGS_MODULE'] = 'mysite.settings'

django.setup()

# drop and recreate the database tables
print()
print('Living on the edge!  Dropping the current database tables.')
with connection.cursor() as cursor:
    cursor.execute("DROP SCHEMA public CASCADE")
    cursor.execute("CREATE SCHEMA public")
    cursor.execute("GRANT ALL ON SCHEMA public TO " + os.environ['BLOG_DATABASE_USER'])
    cursor.execute("GRANT ALL ON SCHEMA public TO public")

# make the migrations and migrate
management.call_command('makemigrations')
management.call_command('migrate')

from account import models as amod

user = amod.ExampleUser()
user.first_name = 'John'
user.last_name = 'Smith'
user.username = 'john.smith'
user.set_password('Password1')
user.email = 'john.smith@example.com'
user.phone = '1234567890'
user.save()
