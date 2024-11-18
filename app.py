from data_numbers import validate_entry
from close import close_app

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
    show_title()
    chosen_option = create_menu('Register a Restaurant', 'List Restaurant', 'Activate Restaurant', 'Exit\n')
    execute_option(chosen_option)


    

if __name__ == '__main__':
    main()