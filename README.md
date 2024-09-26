# Fake ID Generator

## Description
The Fake ID Generator is a Python script that generates fake Brazilian IDs using the `Faker` library. The generated IDs include a name, CPF, email, address, and phone number. The script displays the generated IDs in a formatted manner and allows the user to generate more IDs if desired.

## Features
- Generates fake Brazilian IDs.
- Displays generated IDs in a formatted manner.
- Allows the user to generate more IDs or exit the program.
- Validates user input for the quantity of IDs to generate.

## Requirements
- Python 3.x
- `Faker` library
- `os` module (standard library)

## Installation
1. Clone the repository or download the script.
2. Install the required library using pip:
    ```sh
    pip install faker
    ```

## Usage
1. Run the script:
    ```sh
    python app.py
    ```
2. Follow the on-screen instructions:
    - Enter the quantity of Fake IDs you want to generate.
    - The program will display the generated IDs.
    - You can choose to generate more IDs or exit the program.

## Script Details

### Colors
The script uses ANSI escape codes to format the output with colors.

### Functions
- `print_title()`: Prints the title and author information.
- `generate_full_id()`: Generates the specified quantity of fake IDs.
- `generate_strucutured_data(data)`: Displays the generated IDs in a formatted manner.
- `instructions()`: Prints the instructions for using the script.
- `main()`: Main function that calls other functions to generate and display IDs.

### Example Output

- Name: Asafe Costela
- CPF: 063.548.129-42
- Email: elisacavalcante@gmail.org
- Phone Number: +55 61 9707-1154
- Address: 
    -  Street: Lagoa Abreu
    -  Number:  11
    -  Neighborhood:  Mirtes
    -  CEP | State | City:  98534-328 Garcia / PB



## License
This project is licensed under the MIT License.

## Author
Gabriel Machado

GitHub: [gabriel-machado-dev](https://github.com/gabriel-machado-dev)