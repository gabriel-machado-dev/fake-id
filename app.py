from faker import Faker
import json 



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

def generate_full_name():
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

    # print(json.dumps(names, indent=4, ensure_ascii=False))
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
                print(f'{" "* 5}Rua: {address}')
            elif i == 1:
                if address.isdigit():
                    print(f'{" "* 5}Complemento: {address}')
                else:
                    print(f'{" "* 5}Número: {address}')    
            elif i == 2:
                print(f'{" "* 5}Bairro: {address}')
            elif i == 3:   
                parts = address.split()
                cep = parts[0]
                estado = parts[-1]
                cidade = ' '.join(parts[1:-2])
    
                print(f'{" "* 5}CEP: {cep}')
                print(f'{" "* 5}Cidade: {cidade}')
                print(f'{" "* 5}Estado: {estado}')

        print('-'*50)

print_title()
names = generate_full_name()
generate_strucutured_data(names)

'''NOTE:

1. Gerar os dados num dicionario sendo o nome a chave e o valor o dado gerado
2. Salvar os dados gerados em um arquivo json ou csv
3. Exibir os dados de forma estruturada no terminal 
  - Exemplo: 
    Nome: Gabriel Machado
      -> CPF: 123.456.789-10
      -> Email: gabrieldiasmachado@gmail.com
      -> Endereço: Rua dos Bobos, 0 - São Paulo - SP
      -> Telefone: (11) 99999-9999 
4. Adicionar uma opção para gerar um dado específico
5. Adicionar uma opção para gerar todos os dados

'''