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
    print('~'*90)
    print(msg.center(90))
    print('~'*90)

def choose_category():
    categories = ['Pizza', 'Italian', 'Japanese', 'French', 'Mexican', 'Chicken', 'Meat', 'Fish', 'Seafood', 'Vegan', 'Drinks']
    for n, c in enumerate(categories):
        print(f'{n + 1}.{c}')

    choice = validate_entry('Choose the category: ', 1, len(categories))
    choice = categories[choice - 1]
    return choice

def register_restaurant():
    show_sub_title('REGISTER RESTAURANTS')
    name = str(input('Enter the name of the restaurant: ')).strip()
    category = choose_category()
    print(f'{name} was successfully registered as {category} restaurant!')
    restaurant = {'name' : name, 'category' : category, 'active' : False}
    return_main_menu()
    return restaurant


def list_restaurants(restaurants):
    show_sub_title('RESTAURANTS')

    print('Cod.'.ljust(15), 'Name'.ljust(17), 'Category'.ljust(20), 'Status'.ljust(15))

    for n, restaurant in enumerate(restaurants):
        print(f'\n{n:<15}', end='')
        for key, value in restaurant.items():
            if key == 'active':
                if value == True:
                    print('Active'.ljust(20), end='')
                else:
                    print('Inactive'.ljust(20), end='')
            else:        
                print(f'{value:<20}', end='')
    
    print('\n')
    
    return_main_menu()
    