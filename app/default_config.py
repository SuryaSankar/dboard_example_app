SERVER_NAME = 'localhost:5000'

DEBUG = True

FLASK_CACHE_CONFIG = {
    "CACHE_TYPE": "null",
}

DATA_SOURCES = {
    "pagila": {
        "db_type": "postgresql+psycopg2",
        "db_user": "pagila_admin",
        "db_password": 'pagila_pwd',
        "db_server": 'localhost:5432',
        "db_name": "pagila",
    },
    "sakila": {
        "db_type": "mysql+mysqldb",
        "db_user": "sakila_admin",
        "db_password": 'sakila_pwd',
        "db_server": 'localhost:3306',
        "db_name": "sakila",
    }
}