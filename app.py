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
                  
         {6})    /\__/\ 
         {6}(  = (˶ᵔ ᵕ ᵔ˶)
         {1}-------{6}U{1}-{6}U{1}----------------
         {1}|                        |       |‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾|
         {1}|  {3}Code Author: {2}Gabriel Machado  {0}{1}|       {3}GitHub: {2}https://github.com/gabriel-machado-dev{0}
         {1}|      {3}Version: {2}1.0      {0}{1}|             
         {1}|                        |       |_____________________________________________|
         {1}--------------------------                        {6}\ (˶ᵔ ᵕ ᵔ˶) /{0}
                                                            {6}\         /{0}

        '''.format(DEFAULT, GREEN, RED, YELLOW2, YELLOW, BLINK, MAGENTA, CYAN))

def generate_full_id():
    names = {}

    quantity = int(input("Enter the quantity Fake ID's you want to generate: "))    
    print('')
    for i in range(quantity):
        name = fake.name()
        names[name] = {}
        names[name]['CPF'] = fake.cpf()
        names[name]['Email'] = fake.email()
        names[name]['Address'] = fake.address().replace('\n', ', ')
        names[name]['Phone Number'] = fake.phone_number()

    return names

def generate_strucutured_data(data):
    for name in data:
        print(f'{YELLOW2}Name: {DEFAULT}{name}')
        print(f'{YELLOW2}CPF: {DEFAULT}{data[name]["CPF"]}')
        print(f'{YELLOW2}Email: {DEFAULT}{data[name]["Email"]}')
        print(f'{YELLOW2}Phone Number: {DEFAULT}{data[name]["Phone Number"]}')
        print(f'{YELLOW2}Address: {DEFAULT}')
        for i, address in enumerate(data[name]["Address"].split(',')):
            if i == 0:
                print(f'{" "* 5}{CYAN}Rua: {DEFAULT}{address}')
            elif i == 1:
                if address.strip().isdigit():
                    print(f'{" "* 5}{CYAN}Número: {DEFAULT}{address}')
                else:
                    print(f'{" "* 5}{CYAN}Complemento: {DEFAULT}{address}')    
            elif i == 2:
                print(f'{" "* 5}{CYAN}Bairro: {DEFAULT}{address}')
            elif i == 3:   
                print(f'{" "* 5}{CYAN}CEP / ESTADO / CIDADE: {DEFAULT}{address}')

        print('-' * 50)

def main():
    print_title()
    data = generate_full_id()
    generate_strucutured_data(data)

if __name__ == '__main__':
    main()  
    while True:
        print(f'{YELLOW2}Do you want to generate more Fake ID\'s?{DEFAULT}')
        answer = input(f'{YELLOW2}Yes{DEFAULT} or {RED}No{DEFAULT}: ')
        if answer.lower() == 'yes':
            os.system('clear') if os.name == 'posix' else os.system('cls')
            main()
        else:
            print(f'{YELLOW2}Thank you for using the Fake ID Generator!{DEFAULT}')
            break