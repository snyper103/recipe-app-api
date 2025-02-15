from django.apps import AppConfig


class CoreConfig(AppConfig):
    """
    Configuration class for the 'core' application in a Django project.

    This class inherits from Django's AppConfig and provides configuration
    parameters specific to the 'core' app, such as the default field type for
    automatically generated primary keys and the app's name.

    Attributes:
        default_auto_field:
            Specifies the type of field to use for automatically generated
            primary keys by default in this app. In this case, it is set to
            'django.db.models.BigAutoField'.

        name:
            Indicates the full Python path to the application, which is used
            internally by Django to reference the app throughout the project.
    """
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'core'
