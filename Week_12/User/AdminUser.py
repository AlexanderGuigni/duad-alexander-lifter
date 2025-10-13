from User  import User

class AdminUser(User):

    def get_role(self):
        return "Admin User"

    def has_permissions(self, permission):
        allowed_permissions = ["read", "write", "delete", "modify"]
        return permission in allowed_permissions