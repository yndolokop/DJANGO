from django.core.management.base import BaseCommand
from euromilhoesapp.models import Result, User


class Command(BaseCommand):

    def handle(self, *args, **options):


        print('Это моя команда')


