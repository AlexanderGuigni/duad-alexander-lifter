import menu


def main():
    show_menu_again = True
    while show_menu_again:
        menu.display_menu()
        show_menu_again = menu.run_menu_option(menu.get_menu_option())

    print("-You have logged out of the system.")
    


main()