import time

from django.core.management.base import BaseCommand
from django.db.utils import OperationalError
from psycopg2 import OperationalError as Psycopg2Error


class Command(BaseCommand):
    """
    Defines a custom command integrated with the Django management framework.

    This command checks the availability of the default database by repeatedly
    attempting to establish a connection in a loop until successful. It is
    designed to handle startup situations where the database service might not
    yet be ready, mitigating possible race conditions during deployment in
    environments where dependencies may not start simultaneously.

    Attributes:
        stdout: Provides mechanisms for writing output messages to the console.
        style: Allows styling of output messages such as success, error, or
               warning.
    """

    def handle(self, *args, **options):
        """
        Handles the waiting process for the database to become available. This method repeatedly attempts
        to check the database connection until it succeeds. It logs messages to indicate the status during
        the waiting period and confirms when the database becomes available.

        Args:
            *args: Variable length argument list.
            **options: Arbitrary keyword arguments.

        Raises:
            Psycopg2Error: If there is an issue with the PostgreSQL database connection.
            OperationalError: If the database operation fails due to connectivity reasons.
        """
        self.stdout.write('Esperando pelo banco de dados...')
        db_up = False

        while db_up is False:
            try:
                self.check(databases=['default'])
                db_up = True
            except (Psycopg2Error, OperationalError):
                self.stdout.write('Banco de dados indisponível, espere 1 segundo...')
                time.sleep(1)

        self.stdout.write(self.style.SUCCESS('Banco de dados disponível!'))
