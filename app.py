from close import close_app
from os import system
import restaurant

restaurants = [{'name':'Sushi Max', 'category':'Japanese', 'active': True},
               {'name':'Pizza Top', 'category':'Pizza', 'active': True},
               {'name':'Mamma Maglione', 'category':'Italian', 'active': False}
               ]

end = False

def execute_option(option):

    if option == 1:

        restaurants.append(restaurant.register_restaurant())

    elif option == 2:

        restaurant.list_restaurants(restaurants)

    elif option == 3:

        print('Activate Restaurant\n')

    elif option == 4:

        global end
        close_app()
        end = True
        

def main():
    system('cls')
    restaurant.show_title()
    chosen_option = restaurant.create_menu('Register a Restaurant', 'List Restaurant', 'Activate Restaurant', 'Exit\n')
    execute_option(chosen_option)


if __name__ == '__main__':
    while True:
        if end:
            break

        main()