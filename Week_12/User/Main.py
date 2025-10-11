from AdminUser import AdminUser
from RegularUser import RegularUser

def main():
    admin = AdminUser("Jorge")
    regular = RegularUser("Samuel")

    print(f"{admin.username} is an {admin.get_role()}")
    print(f"{regular.username} is a {regular.get_role()}")

    print(f"Admin has write permissions: {admin.has_permissions('write')}")
    print(f"Regular user has write permissions: {regular.has_permissions('write')}")

main()