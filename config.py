import os

PROJECT_ROOT = os.path.dirname(os.path.realpath(__file__))
DATABASE_CONNECTION_URI = f'sqlite:///{os.path.join(PROJECT_ROOT, "localdb.db")}'
