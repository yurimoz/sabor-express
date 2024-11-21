from data_numbers import validate_entry
from os import system


def show_title():
    print('''
░██████╗░█████╗░██████╗░░█████╗░██████╗░  ███████╗██╗░░██╗██████╗░██████╗░███████╗░██████╗░██████╗
██╔════╝██╔══██╗██╔══██╗██╔══██╗██╔══██╗  ██╔════╝╚██╗██╔╝██╔══██╗██╔══██╗██╔════╝██╔════╝██╔════╝
╚█████╗░███████║██████╦╝██║░░██║██████╔╝  █████╗░░░╚███╔╝░██████╔╝██████╔╝█████╗░░╚█████╗░╚█████╗░
░╚═══██╗██╔══██║██╔══██╗██║░░██║██╔══██╗  ██╔══╝░░░██╔██╗░██╔═══╝░██╔══██╗██╔══╝░░░╚═══██╗░╚═══██╗
██████╔╝██║░░██║██████╦╝╚█████╔╝██║░░██║  ███████╗██╔╝╚██╗██║░░░░░██║░░██║███████╗██████╔╝██████╔╝
╚═════╝░╚═╝░░╚═╝╚═════╝░░╚════╝░╚═╝░░╚═╝  ╚══════╝╚═╝░░╚═╝╚═╝░░░░░╚═╝░░╚═╝╚══════╝╚═════╝░╚═════╝░\n''')


def create_menu(*options):

    for number, option in enumerate(options):
        print(f'{number + 1:>2}.{option}')
    
    chosen_option = validate_entry('Choose an option: ', lowerlim=1, upperlim=len(options))

    return chosen_option


def return_main_menu():

    input('\nPress enter to return to the main menu.')


def show_sub_title(msg):
    system('cls')
    print('~'*30)
    print(msg.center(30))
    print('~'*30)

def register_restaurant():
    show_sub_title('REGISTER RESTAURANTS')
    name = str(input('Enter the name of the restaurant: ')).strip()
    print(f'{name} was successfully registered!')
    return_main_menu()
    return name


def list_restaurants(restaurants):
    show_sub_title('RESTAURANTS')

    for n, r in enumerate(restaurants):
        print(f'{n + 1}. {r}')
    
    return_main_menu()
    