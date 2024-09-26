from faker import Faker
import os

# Colors
DEFAULT = '\033[0m'
GREEN = '\033[1;32m'
RED = '\033[1;31m'
YELLOW = '\033[3m\033[1;33m'
YELLOW2 = '\033[1;93m'
BLUE = '\033[1;34m'
MAGENTA = '\033[1;35m'
CYAN = '\033[1;36m'
BOLD = '\033[1m'
BLINK = '\033[5m'

fake = Faker(locale='pt_BR')

def print_title():
    print('''

        {1} _____                                                            _____ {0}
        {1}( ___ )                                                          ( ___ ){0}
        {1}|   |~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~|   |{0}
        {1}|   |       ███████╗ █████╗ ██╗  ██╗███████╗    ██╗██████╗       |   |{0}
        {1}|   |       ██╔════╝██╔══██╗██║ ██╔╝██╔════╝    ██║██╔══██╗      |   |{0}
        {1}|   |       █████╗  ███████║█████╔╝ █████╗      ██║██║  ██║      |   |{0}
        {1}|   |       ██╔══╝  ██╔══██║██╔═██╗ ██╔══╝      ██║██║  ██║      |   |{0}
        {1}|   |       ██║     ██║  ██║██║  ██╗███████╗    ██║██████╔╝      |   |{0}
        {1}|   |       ╚═╝     ╚═╝  ╚═╝╚═╝  ╚═╝╚══════╝    ╚═╝╚═════╝       |   |{0}
        {1}|___|~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~|___|{0}
        {1}(_____)                                                          (_____){0}

         {6})    /\__/\ 
         {6}( = (˶ᵔ ᵕ ᵔ˶)
         {1}-------{6}U{1}-{6}U{1}----------------
         {1}|                        |       |‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾|
         {1}|  {3}Code Author: {2}Gabriel Machado  {0}{1}|       {3}GitHub: {2}https://github.com/gabriel-machado-dev{0}
         {1}|      {3}Version: {2}1.0      {0}{1}|             
         {1}|                        |       |_____________________________________________|
         {1}--------------------------                        {6}\ (˶ᵔ ᵕ ᵔ˶) /{0}
                                                            {6}\         /{0}

        '''.format(DEFAULT, GREEN, RED,YELLOW2
                   ,YELLOW, BLINK, MAGENTA, CYAN))

def generate_full_id():
    names = {}

    try:
        
        quantity = int(input("Enter the quantity Fake ID's you want to generate: "))

        if quantity <= 0:   

            print(f'{RED}Invalid value!{DEFAULT}')
            print(f'{YELLOW2}Please enter a valid number!{DEFAULT}')
            print('')
            return generate_full_id()   

        for i in range(quantity):
            name = fake.name()
            names[name] = {}
            names[name]['CPF'] = fake.cpf()
            names[name]['Email'] = fake.email()
            names[name]['Address'] = fake.address().replace('\n', ', ')
            names[name]['Phone Number'] = fake.phone_number()

    except ValueError:
        print(f'{RED}Invalid value!{DEFAULT}')
        print(f'{YELLOW2}Please enter a valid number!{DEFAULT}')   
        print('')     
        return generate_full_id()   


    return names

def generate_strucutured_data(data):
    for name in data:
        print(f'{YELLOW2}{BOLD}Name: {DEFAULT}{name}')
        print(f'{YELLOW2}{BOLD}CPF: {DEFAULT}{data[name]["CPF"]}')
        print(f'{YELLOW2}{BOLD}Email: {DEFAULT}{data[name]["Email"]}'.replace('@example', '@gmail'))
        print(f'{YELLOW2}{BOLD}Phone Number: {DEFAULT}{data[name]["Phone Number"]}')
        print(f'{YELLOW2}{BOLD}Address: {DEFAULT}')
        for i, address in enumerate(data[name]["Address"].split(',')):

            length_address = len(data[name]["Address"].split(','))

            if length_address == 4:
                if i == 0:
                    print(f'{" " * 5}{CYAN}{BOLD}Street: {DEFAULT}{address}')
                elif i == 1:
                        print(f'{" " * 5}{CYAN}{BOLD}Number: {DEFAULT}{address}')
                elif i == 2:
                    print(f'{" " * 5}{CYAN}{BOLD}Neighborhood: {DEFAULT}{address}')
                elif i == 3:
                    print(f'{" " * 5}{CYAN}{BOLD}CEP | State | City: {DEFAULT}{address}')

            if length_address == 3:
                if i == 0:
                    print(f'{" " * 5}{CYAN}{BOLD}Street: {DEFAULT}{address}')
                elif i == 1:
                    print(f'{" " * 5}{CYAN}{BOLD}Neighborhood: {DEFAULT}{address}')
                elif i == 2:
                    print(f'{" " * 5}{CYAN}{BOLD}CEP | State | City: {DEFAULT}{address}')

        print('-' * 50)

def instructions():
    print(f'{YELLOW2}Instructions:{DEFAULT}')
    print(f'{YELLOW2}1. Enter the quantity of Fake ID\'s you want to generate.{DEFAULT}')
    print(f'{YELLOW2}2. The program will generate the Fake ID\'s and display them on the screen.{DEFAULT}')
    print(f'{YELLOW2}3. If you want to generate more Fake ID\'s, enter "yes".{DEFAULT}')
    print(f'{YELLOW2}4. If you want to exit the program, enter "no".{DEFAULT}')
    print('Note: The program generates Fake ID\'s with Brazilian data.')
    print('Note: There\'s no limit to the quantity of Fake ID\'s you can generate.')    
    print('') 

def main():
    print_title()
    instructions()  
    data = generate_full_id()
    generate_strucutured_data(data)

if __name__ == '__main__':
    main()
    while True:
        print(f'{YELLOW2}Do you want to generate more Fake ID\'s?{DEFAULT}')
        answer = input(f'{YELLOW2}Yes{DEFAULT} or {RED}No{DEFAULT}: ').lower().strip()
        
        if answer == 'yes':
            main()
        elif answer == 'no':
            print(f'{YELLOW2}See you later!{DEFAULT}')
            break
        else:
            print(f'{RED}Invalid value!{DEFAULT}')
            print(f'{YELLOW2}Please enter "yes" or "no"!{DEFAULT}')
            print('')             
