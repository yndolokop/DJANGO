from django.core.management.base import BaseCommand
from euromilhoesapp.models import Result, User


class Command(BaseCommand):

    def handle(self, *args, **options):
        # Выбираем ВСЕ категории
        categories = Result.objects.all()
        print(categories)
        print(type(Result))
        for item in categories:
            print(item)
            print(type(item))
        print('Это моя команда')


