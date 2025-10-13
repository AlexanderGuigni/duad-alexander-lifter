from User import User

class RegularUser(User):

    def get_role(self):
        return "Regular User"

    def has_permissions(self, permission):
        allowed_permissions = ["read"]
        return permission in allowed_permissions