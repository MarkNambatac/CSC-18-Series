import os
basedir = os.path.abspath(os.path.dirname(__file__))
DB_NAME = "students"
DB_HOST = "localhost"
DB_USERNAME = "postgres"
DB_PASSWORD = "123456789"
DB_CONN_STRING = "postgresql://%s:%s@%s:5432/%s" % (DB_USERNAME,DB_PASSWORD,DB_HOST,DB_NAME)
SECRET_KEY="sawa"