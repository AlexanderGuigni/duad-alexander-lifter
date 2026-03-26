from sqlalchemy import create_engine

class DatabaseConnection:

    __DB_URL = "postgresql://postgres:postgres@localhost:54674/postgres"  # Default database URL 
     # Create engine with echo for debugging

    def __init__(self):
    
        self.engine = create_engine(self.__DB_URL, echo=True)

    def execute_statement(self, statement):
        try:
            with self.engine.connect() as connection:
                result = connection.execute(statement)
                connection.commit()
                if result.returns_rows:
                    return result.fetchall()
                else:
                    return None
        except Exception as e:
            print(f"Error executing statement: {e}")
            return None   
    def execute_multiple_statements(self, statements):
        try:
            with self.engine.connect() as connection:
                for statement in statements:
                    connection.execute(statement)
                connection.commit()
        except Exception as e:
            print(f"Error executing multiple statements: {e}")
            return None
            
    