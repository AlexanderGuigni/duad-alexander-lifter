from datetime import datetime
from enum import Enum
import re
from unittest import result


class Users:
    def __init__(self, db_connection):
        self.db_connection = db_connection

    def create_user(self, body):
        self.validate_username(body.get(UserFields.USERNAME.value))
        self.validate_email_format(body.get(UserFields.EMAIL.value))
        self.validate_password_strength(body.get(UserFields.PASSWORD.value))
        self.validate_birthdate(body.get(UserFields.BIRTHDATE.value))

        if body.get(UserFields.IS_ENABLED.value) is None:
            body[UserFields.IS_ENABLED.value] = True
        else:
            self.validate_boolean(body.get(UserFields.IS_ENABLED.value), UserFields.IS_ENABLED.value)
        if body.get(UserFields.IS_IN_ARREARS.value) is None:
            body[UserFields.IS_IN_ARREARS.value] = False
        else:
            self.validate_boolean(body.get(UserFields.IS_IN_ARREARS.value), UserFields.IS_IN_ARREARS.value)

        self.db_connection.execute_query(
            "INSERT INTO lifter.users (username, password, birthdate, email, is_enabled, is_in_arrears) VALUES (%s, %s, %s, %s, %s, %s)",
            body[UserFields.USERNAME.value], body[UserFields.PASSWORD.value], body[UserFields.BIRTHDATE.value], body[UserFields.EMAIL.value], body[UserFields.IS_ENABLED.value], body[UserFields.IS_IN_ARREARS.value]
        )

        return self.get_last_user()

    def update_user_status(self, body):
        self.validate_not_empty(body.get(UserFields.ID.value), UserFields.ID.value)
        self.validate_user_exists(body.get(UserFields.ID.value))
        self.validate_boolean(body.get(UserFields.IS_ENABLED.value), UserFields.IS_ENABLED.value)
        self.db_connection.execute_query(
            "UPDATE lifter.users SET is_enabled = %s WHERE user_id = %s",
            body.get(UserFields.IS_ENABLED.value), body.get(UserFields.ID.value)
        )

        return self.get_users(**{UserFields.ID.value: body.get(UserFields.ID.value)})

    def update_user_arrear_status(self, body):
        self.validate_not_empty(body.get(UserFields.ID.value), UserFields.ID.value)
        self.validate_user_exists(body.get(UserFields.ID.value))
        self.validate_boolean(body.get(UserFields.IS_IN_ARREARS.value), UserFields.IS_IN_ARREARS.value)
        self.db_connection.execute_query(
            "UPDATE lifter.users SET is_in_arrears = %s WHERE user_id = %s",
            body.get(UserFields.IS_IN_ARREARS.value), body.get(UserFields.ID.value)
        )

        return self.get_users(**{UserFields.ID.value: body.get(UserFields.ID.value)})

    def get_users(self, **kwargs):
        filters = ""
        for key,value in kwargs.items():
            if filters == "":
                filters = key + "= %s"
            else:
                filters += " AND " + key + "= %s"

        if filters != "":
            filters = " WHERE " + filters
                            
        results = self.db_connection.execute_query(
            "SELECT user_id, username, email, birthdate, is_enabled, is_in_arrears FROM lifter.users" + filters, *list(kwargs.values())
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
                UserFields.USERNAME.value: row[8],
                UserFields.EMAIL.value: row[2],
                UserFields.BIRTHDATE.value: row[3].strftime('%Y-%m-%d'),
                UserFields.IS_ENABLED.value: row[4],
                UserFields.IS_IN_ARREARS.value: row[5]
            }
            return user
        return None

    def validate_username(self, user):
        if not user or not user.strip():
            raise ValueError(f"User cannot be empty")
        if len(user) < 3:
            raise ValueError(f"User must be at least 3 characters long")
        if not isinstance(user[0], str):
            raise ValueError(f"User must start with a string")
        result = self.get_users(**{UserFields.USERNAME.value: user})
        if result:
            raise ValueError(f"Username {user} already exists.")
            
    def validate_email_format(self, email):
        if not email or not email.strip():
                raise ValueError(f"Email cannot be empty")
        
        email_regex = r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$'
        if not re.match(email_regex, email):
            raise ValueError("Invalid email format")
        result = self.get_users(**{UserFields.EMAIL.value: email})
        if result:
            raise ValueError(f"Email {email} already exists.")
        
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
        
    def validate_boolean(self, value, field_name):
        if not isinstance(value, bool):
            raise ValueError(f"{field_name} must be a boolean value")
        
    def validate_user_exists(self, user_id):
        result = self.get_users(**{UserFields.ID.value:user_id})
        if not result:
            raise ValueError(f"User with id {user_id} does not exist.")
        else:
            return result[0]
        
    def validate_user_is_enabled(self, user_id):
        result = self.get_users(**{UserFields.ID.value:user_id})
        if result and result[0][UserFields.IS_ENABLED.value] == False:
            raise ValueError(f"User with id {user_id} is not enabled.")
        
    def validate_not_empty(self, value, field_name):
        if value is None or not str(value).strip() or value == "" or value == 'None':
            raise ValueError(f"{field_name} must be a non-empty.")
    

  
class UserFields(Enum):
    ID = "user_id"
    USERNAME = "username"
    PASSWORD = "password"
    EMAIL = "email"
    BIRTHDATE = "birthdate"
    IS_ENABLED = "is_enabled"
    IS_IN_ARREARS = "is_in_arrears"
    