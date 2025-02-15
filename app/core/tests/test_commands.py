from unittest.mock import patch

from django.core.management import call_command
from django.db.utils import OperationalError
from django.test import SimpleTestCase
from psycopg2 import OperationalError as Psycopg2Error


@patch('core.management.commands.wait_for_db.Command.check')
class CommandTest(SimpleTestCase):
    """
    Unit test class for testing the `wait_for_db` management command.

    This class contains unit tests for the `wait_for_db` management command,
    which ensures the database is ready and operational. It tests the behavior
    of the command in scenarios where the database becomes available
    immediately or after some delay due to errors.

    Attributes:
        None

    Methods:
        test_wait_for_db_is_ready(patched_check)
            Test that the database is accessible and ready when the command
            is called, ensuring no errors occur.
        test_wait_for_db_delay(patched_sleep, patched_check)
            Test the behavior of the command when database connectivity errors
            occur and validate that it retries until the database becomes ready.
    """

    def test_wait_for_db_is_ready(self, patched_check):
        """
        Tests the functionality of the wait_for_db command to ensure it interacts
        with check and call_command appropriately.

        Ensures that the command executes successfully when the database check
        returns True, and verifies the check is called with the correct parameters.

        Arguments:
            self: The instance of the test class.
            patched_check: Mocked function that simulates the behavior of the database
            connection check.

        Raises:
            None

        Returns:
            None
        """
        patched_check.return_value = True

        call_command('wait_for_db')

        patched_check.assert_called_once_with(databases=['default'])

    @patch('time.sleep')
    def test_wait_for_db_delay(self, patched_sleep, patched_check):
        """
        A test function that ensures the `wait_for_db` command retries checking the database
        connection with delays in between attempts and ultimately succeeds after several
        failures. This test confirms that the command handles consecutive database errors
        and successfully verifies the database connection.

        @param patched_sleep
            Mocked version of the `time.sleep` function to prevent actual delays during the test.

        @param patched_check
            Mocked version of the database check to simulate errors and success responses.

        @return
            None

        @raises AssertionError
            If the number of retries does not match the expected call count, or if the mocked
            database check is not called correctly.
        """
        patched_check.side_effect = [Psycopg2Error] * 2 + \
                                    [OperationalError] * 3 + [True]

        call_command('wait_for_db')

        self.assertEqual(patched_check.call_count, 6)
        patched_check.assert_called_with(databases=['default'])
