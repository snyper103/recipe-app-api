"""
Comandos Django para esperar até que o banco de dados se encontre disponível.
"""
import time

from psycopg2 import OperationalError as Psycopg2Error

from django.core.management.base import BaseCommand
from django.db.utils import OperationalError


class Command(BaseCommand):
    """Classe para os comandos Django relacionados a disponibilidade do banco de dados."""

    def handle(self, *args, **options):
        """Ponto de entrada do comando."""
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