from django.contrib.auth import get_user_model
from django.test import TestCase


class ModelTests(TestCase):
    """
    Test case class for user model functionalities.

    Provides a set of tests to validate the behavior and correctness of user model operations,
    such as the creation of users and superusers, email normalization, and raising appropriate
    errors when expected conditions are not met. The tests verify that the methods in the user
    model function as intended and handle edge cases appropriately.

    Methods
    -------
    test_create_user_with_email_succesfull()
        Verifies that a user can be successfully created with a valid email and password.

    test_new_user_email_normalized()
        Ensures that the email input for newly created users is normalized to a standard format.

    test_new_user_without_email_raises_error()
        Confirms that creating a user without an email raises a ValueError.

    test_create_superuser()
        Tests the creation of a superuser and validates the superuser-specific attributes.
    """

    def test_create_user_with_valid_credentials(self):
        """
        Test case for successfully creating a user with an email and password.

        This test ensures that a user is correctly created when provided with a valid
        email and password. It also verifies that the email is set correctly and the
        password is securely stored by using Django's password hashing mechanism.

        Parameters:
            self (TestCase): The test case instance.

        Raises:
            AssertionError: If the created user's email or password validation does
                not match the expected results.
        """
        email = 'test@example.com'
        password = 'testpassword123'
        user = get_user_model().objects.create_user(
            email=email,
            password=password,
        )

        self.assertEqual(user.email, email)
        self.assertTrue(user.check_password(password))

    def test_new_user_email_normalized(self):
        """
        Tests that the email field of a new user is properly normalized during the user
        creation process. The test uses a variety of email cases to verify this
        functionality, ensuring emails are consistently stored in normalized format.

        Params:
            self (TestCase): Automatically passed instance of the test case class.

        Raises:
            AssertionError: If the normalized version of the email does not match the
                expected value for the corresponding input email.
        """
        sample_emails = [
            ['test1@EXAMPLE.com', 'test1@example.com'],
            ['Test2@Example.com', 'Test2@example.com'],
            ['TEST3@EXAMPLE.COM', 'TEST3@example.com'],
            ['test4@example.COM', 'test4@example.com'],
        ]

        for email, expected in sample_emails:
            user = get_user_model().objects.create_user(email, 'sample123')
            self.assertEqual(user.email, expected)

    def test_new_user_without_email_raises_error(self):
        """
        Test case for verifying that creating a user without an email raises a ValueError.

        This test ensures that the `get_user_model().objects.create_user` method throws
        a ValueError when an empty string is passed as an email during user creation.

        Attributes
        ----------
        None

        Methods
        -------
        None

        Raises
        ------
        ValueError
            Raised when attempting to create a user without providing an email address.
        """
        with self.assertRaises(ValueError):
            get_user_model().objects.create_user('', 'test123')

    def test_create_superuser(self):
        """
        Tests the `create_superuser` functionality.

        This test verifies that the created superuser has the correct attributes
        set, such as `is_superuser` and `is_staff`.

        Raises:
            AssertionError: If the created user does not have `is_superuser` or
            `is_staff` set to True.
        """
        user = get_user_model().objects.create_superuser('test@example.com', 'test123')

        self.assertTrue(user.is_superuser)
        self.assertTrue(user.is_staff)
