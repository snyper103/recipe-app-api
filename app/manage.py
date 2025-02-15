#!/usr/bin/env python
import os
import sys


def main():
    """
    Represents the main entry point for a Django application. This function initializes
    the Django environment by setting the default settings module and handles the
    execution of management commands. If Django cannot be imported, it raises an
    ImportError providing details on the possible causes.

    Raises:
        ImportError: If Django modules cannot be imported due to missing installation
        or improper environment setup.
    """
    os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'app.settings')
    try:
        from django.core.management import execute_from_command_line
    except ImportError as exc:
        raise ImportError(
            "Couldn't import Django. Are you sure it's installed and "
            "available on your PYTHONPATH environment variable? Did you "
            "forget to activate a virtual environment?"
        ) from exc
    execute_from_command_line(sys.argv)


if __name__ == '__main__':
    main()
