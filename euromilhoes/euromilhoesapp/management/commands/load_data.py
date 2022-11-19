from django.core.management.base import BaseCommand
from euromilhoesapp.models import Result
import pandas as pd
from sqlalchemy import create_engine


class Command(BaseCommand):
    def handle(self, *args, **options):
        print('hi')
        csv_file = 'eurom_.csv'
        df = pd.read_csv(csv_file)
        print(df)
        engine = create_engine('sqlite:///db.sqlite3')
        df.to_sql(Result._meta.db_table, con=engine, if_exists='append', index=False, index_label=None, method=None)
