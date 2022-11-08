from django.core.management.base import BaseCommand
from euromilhoesapp.models import Category


class Command(BaseCommand):

    def handle(self, *args, **options):
        # Выбираем ВСЕ категории
        categories = Category.objects.all()
        print(categories)

        print('End')

