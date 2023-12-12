import psycopg2

class group_model:
    def __init__(self, db_connection):
        self.connection = db_connection

