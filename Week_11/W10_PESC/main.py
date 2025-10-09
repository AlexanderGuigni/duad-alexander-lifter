import menu


def main():
    students_list = []
    show_menu_again = True
    try:
        while show_menu_again:
            menu.display_menu()
            result =  menu.run_menu_option(menu.get_menu_option(),students_list)
            show_menu_again =result[0]
            students_list = result[1]
    except Exception as ex:
        print(f"Error: {ex}")
    print("-You have logged out of the system.")
    


main()