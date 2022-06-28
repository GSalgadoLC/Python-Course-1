# Notes:
# A Django application can have many applications within it, like reusable subunits like Legos
# Model View Controller Architecture
# Model Template View in Django
# admin . terminal. python manage.py createsuperuser
# admin moderator guests
# A database abstraction API allows you to bypass the complexities of the database


#!/usr/bin/env python
import os
import sys

if __name__ == '__main__':
    os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'vidly.settings')
    try:
        from django.core.management import execute_from_command_line
    except ImportError as exc:
        raise ImportError(
            "Couldn't import Django. Are you sure it's installed and "
            "available on your PYTHONPATH environment variable? Did you "
            "forget to activate a virtual environment?"
        ) from exc
    execute_from_command_line(sys.argv)
