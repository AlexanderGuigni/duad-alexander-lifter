import psycopg2

class DatabaseConnection:

    def __init__(self, host ="localhost", port=54674, user="postgres", password="postgres", dbname="postgres"):
        self.host = host
        self.port = port
        self.user = user
        self.password = password
        self.dbname = dbname

        self.connection = self.__connect()

    def __connect(self):
        try:
            connection = psycopg2.connect(
                host=self.host,
                port=self.port,
                user=self.user,
                password=self.password,
                dbname=self.dbname,
            )
            print("Connected to the database")
            return connection
        except Exception as e:
            print(f"An error occurred: {e}")
            return None

    def disconnect(self):
        if self.connection:
            self.connection.close()
            print("Database connection closed")

    def execute_query(self, query, *args):
        if self.connection is None:
            return None
        try:
            cursor = self.connection.cursor()
            cursor.execute(query, args)
            self.connection.commit()
            if cursor.description:
                results = cursor.fetchall()
            else:
                results = None
            cursor.close()
            return results
        except Exception as e:
            self.connection.rollback()
            print(f"An error occurred while executing the query: {e}")
            raise
        finally:
            self.disconnect()

    def execute_multiple_queries(self, *args):
        if self.connection is None:
            return None
        try:
            for query, params in args:
                cursor = self.connection.cursor()
                cursor.execute(query, params)
                cursor.close()
            self.connection.commit()
        except Exception as e:
            self.connection.rollback()
            print(f"An error occurred while executing the query: {e}")
            raise
        finally:
            self.disconnect()