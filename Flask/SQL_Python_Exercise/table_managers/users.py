from datetime import datetime
from enum import Enum
import re


class Users:
    def __init__(self, db_connection):
        self.db_connection = db_connection

    def create_user(self, body):
        self.validate_user(body.get(UserFields.USERNAME.value))
        self.validate_email_format(body.get(UserFields.EMAIL.value))
        self.validate_password_strength(body.get(UserFields.PASSWORD.value))
        self.validate_birthdate(body.get(UserFields.BIRTHDATE.value))

        if body.get(UserFields.IS_ENABLED.value) is None:
            body[UserFields.IS_ENABLED.value] = 1
        else:
            self.validate_one_or_cero(body.get(UserFields.IS_ENABLED.value), UserFields.IS_ENABLED.value)
        if body.get(UserFields.IS_IN_ARREARS.value) is None:
            body[UserFields.IS_IN_ARREARS.value] = 0
        else:
            self.validate_one_or_cero(body.get(UserFields.IS_IN_ARREARS.value), UserFields.IS_IN_ARREARS.value)

        self.db_connection.execute_query(
            "INSERT INTO lifter.users (username, password, birthdate, email, is_enabled, is_in_arrears) VALUES (%s, %s, %s, %s, %s, %s)",
            body[UserFields.USERNAME.value], body[UserFields.PASSWORD.value], body[UserFields.BIRTHDATE.value], body[UserFields.EMAIL.value], body[UserFields.IS_ENABLED.value], body[UserFields.IS_IN_ARREARS.value]
        )

        return self.get_last_user()



    def update_user_status(self, user_id, is_enabled):
        self.validate_one_or_cero(is_enabled, UserFields.IS_ENABLED.value)
        self.db_connection.execute_query(
            "UPDATE lifter.users SET is_enabled = %s WHERE user_id = %s",
            is_enabled, user_id
        )

        return self.get_user_by_id(user_id)

    def update_user_arrear_status(self, user_id, is_in_arrears):
        self.validate_one_or_cero(is_in_arrears, UserFields.IS_IN_ARREARS.value)
        self.db_connection.execute_query(
            "UPDATE lifter.users SET is_in_arrears = %s WHERE user_id = %s",
            is_in_arrears, user_id
        )

        return self.get_user_by_id(user_id)

    def get_all_users(self):
        results = self.db_connection.execute_query(
            "SELECT user_id, username, email, birthdate, is_enabled, is_in_arrears FROM lifter.users"
        )
        users = []
        if results:
            for row in results:
                user = {
                    UserFields.ID.value: row[0],
                    UserFields.USERNAME.value: row[1],
                    UserFields.EMAIL.value: row[2],
                    UserFields.BIRTHDATE.value: row[3].strftime('%Y-%m-%d'),
                    UserFields.IS_ENABLED.value: row[4],
                    UserFields.IS_IN_ARREARS.value: row[5]
                }
                users.append(user)
        return users
    
    def get_users_by_status(self, is_enabled):
        is_enabled = int(is_enabled)
        self.validate_one_or_cero(is_enabled, UserFields.IS_ENABLED.value)
        results = self.db_connection.execute_query(
            "SELECT user_id, username, email, birthdate, is_enabled, is_in_arrears FROM lifter.users WHERE is_enabled = %s", is_enabled
        )
        users = []
        if results:
            for row in results:
                user = {
                    UserFields.ID.value: row[0],
                    UserFields.USERNAME.value: row[1],
                    UserFields.EMAIL.value: row[2],
                    UserFields.BIRTHDATE.value: row[3].strftime('%Y-%m-%d'),
                    UserFields.IS_ENABLED.value: row[4],
                    UserFields.IS_IN_ARREARS.value: row[5]
                }
                users.append(user)
        return users
    
    def get_users_by_arrear_status(self, is_in_arrears):
        is_in_arrears = int(is_in_arrears)
        self.validate_one_or_cero(is_in_arrears, UserFields.IS_IN_ARREARS.value)
        results = self.db_connection.execute_query(
            "SELECT user_id, username, email, birthdate, is_enabled, is_in_arrears FROM lifter.users WHERE is_in_arrears = %s", is_in_arrears
        )
        users = []
        if results:
            for row in results:
                user = {
                    UserFields.ID.value: row[0],
                    UserFields.USERNAME.value: row[1],
                    UserFields.EMAIL.value: row[2],
                    UserFields.BIRTHDATE.value: row[3].strftime('%Y-%m-%d'),
                    UserFields.IS_ENABLED.value: row[4],
                    UserFields.IS_IN_ARREARS.value: row[5]
                }
                users.append(user)
        return users
    
    def get_user_by_id(self, user_id):
        results = self.db_connection.execute_query(
            "SELECT user_id, username, email, birthdate, is_enabled, is_in_arrears FROM lifter.users WHERE user_id = %s", user_id
        )
        users = []
        if results:
            for row in results:
                user = {
                    UserFields.ID.value: row[0],
                    UserFields.USERNAME.value: row[1],
                    UserFields.EMAIL.value: row[2],
                    UserFields.BIRTHDATE.value: row[3].strftime('%Y-%m-%d'),
                    UserFields.IS_ENABLED.value: row[4],
                    UserFields.IS_IN_ARREARS.value: row[5]
                }
                users.append(user)
        return users
    
    def get_last_user(self):
        results = self.db_connection.execute_query(
            "SELECT user_id, username, email, birthdate, is_enabled, is_in_arrears FROM lifter.users ORDER BY user_id DESC LIMIT 1"
        )
        if results:
            row = results[0]
            user = {
                UserFields.ID.value: row[0],
                UserFields.USERNAME.value: row[1],
                UserFields.EMAIL.value: row[2],
                UserFields.BIRTHDATE.value: row[3].strftime('%Y-%m-%d'),
                UserFields.IS_ENABLED.value: row[4],
                UserFields.IS_IN_ARREARS.value: row[5]
            }
            return user
        return None

    def validate_user(self, user):
        if not user or not user.strip():
            raise ValueError(f"User cannot be empty")
        if len(user) < 3:
            raise ValueError(f"User must be at least 3 characters long")
        if not isinstance(user[0], str):
            raise ValueError(f"User must start with a string")
            
    def validate_email_format(self, email):
        if not email or not email.strip():
                raise ValueError(f"Email cannot be empty")
        
        email_regex = r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$'
        if not re.match(email_regex, email):
            raise ValueError("Invalid email format")
        
    def validate_password_strength(self, password):
        if not password or not password.strip():
                raise ValueError(f"Password cannot be empty")
        if len(password) < 8:
            raise ValueError("Password must be at least 8 characters long")
        if not any(char.isdigit() for char in password):
            raise ValueError("Password must contain at least one digit")
        if not any(char.isupper() for char in password):
            raise ValueError("Password must contain at least one uppercase letter")
        
    def validate_birthdate(self, birthdate):
        if not birthdate or not birthdate.strip():
                raise ValueError(f"Birthdate cannot be empty")
        try:
            datetime.strptime(birthdate, '%Y-%m-%d')
        except ValueError:
            raise ValueError("Birthdate must be in YYYY-MM-DD format")
        
    def validate_one_or_cero(self, value, field_name):
        if int(value) not in [0, 1]:
            raise ValueError(f"{field_name} must be 1 = TRUE or 0 = FALSE")
        


class UserFields(Enum):
    ID = "user_id"
    USERNAME = "username"
    PASSWORD = "password"
    EMAIL = "email"
    BIRTHDATE = "birthdate"
    IS_ENABLED = "is_enabled"
    IS_IN_ARREARS = "is_in_arrears"
    