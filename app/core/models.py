from django.contrib.auth.models import (
    AbstractBaseUser,
    BaseUserManager,
    PermissionsMixin,
)
from django.db import models


class UserManager(BaseUserManager):
    """
    Manager class for handling user creation and management.

    This class contains methods to create general users and superusers with
    appropriate attributes and permissions.

    Attributes:
        model: The user model that this manager works with.
        _db: The database being used for this manager's queries.
    """

    def create_user(self, email, password=None, **extra_fields):
        """
        Creates and saves a new user with the given email, password, and additional fields.
        This function ensures that an email is provided for the user, normalizes the email,
        and securely sets the password before saving the user instance.

        Parameters:
         email (str): The email of the new user. Must not be None or empty.
         password (Optional[str]): The user's password. If not provided, it will not be set.
         **extra_fields (dict): Additional fields to include when creating the user.

        Returns:
         User: The created user instance.

        Raises:
         ValueError: If the email parameter is not provided.
        """
        if not email:
            raise ValueError('O usuário deve conter um e-mail.')

        user = self.model(email=self.normalize_email(email), **extra_fields)
        user.set_password(password)
        user.save(using=self._db)

        return user

    def create_superuser(self, email, password):
        """
        Creates and returns a superuser with the specified email and password.
        The created superuser will have elevated administrative permissions.

        Parameters:
        email (str): The email address for the superuser.
        password (str): The password for the superuser.

        Returns:
        User: The created superuser instance.
        """
        user = self.create_user(email, password)
        user.is_staff = True
        user.is_superuser = True
        user.save(using=self._db)

        return user


class User(AbstractBaseUser, PermissionsMixin):
    """
    Represents a custom user model extending AbstractBaseUser and PermissionsMixin.

    This class defines a user with an email as the unique identifier instead of
    a username. It includes fields such as email, name, is_active, and is_staff,
    and integrates Django's authentication system. The model also leverages
    a custom manager to handle user creation.

    Attributes:
        email (str): The email address of the user, used as the unique identifier
            for authentication.
        name (str): The full name of the user.
        is_active (bool): Boolean indicating whether the user account is active.
            Defaults to True.
        is_staff (bool): Boolean indicating whether the user has staff
            permissions. Defaults to False.
        objects (UserManager): The manager for handling custom user creation
            and management.

    Class variables:
        USERNAME_FIELD: Specifies the model field that should be used as the username
            for authentication. In this case, 'email'.
    """
    email = models.EmailField(max_length=255, unique=True)
    name = models.CharField(max_length=255)
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)

    objects = UserManager()

    USERNAME_FIELD = 'email'
