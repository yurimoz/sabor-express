from close import close_app
from os import system
import restaurant

def execute_option(option):

    if option == 1:

        print('Register a Restaurant\n')

    elif option == 2:

        print('List Restaurant\n')

    elif option == 3:

        print('Activate Restaurant\n')

    elif option == 4:

        close_app()

def main():
    system('cls')
    restaurant.show_title()
    chosen_option = restaurant.create_menu('Register a Restaurant', 'List Restaurant', 'Activate Restaurant', 'Exit\n')
    execute_option(chosen_option)


if __name__ == '__main__':
    main()