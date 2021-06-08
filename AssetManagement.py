from AssetManagementTable import AssetManagementTable
from Menu import Menu
from KeySet import KeySet
from KeyTable import KeyTable
import os
from NumberFormat import Money, Percent
import datetime
import sys

active_tables = dict()
arguments = sys.argv[1:]

class ParseError(Exception):
    def __init__(self, *args: object) -> None:
        super().__init__('''
ERROR: Invalid arguemnts were proveded.  Proper syntax is:
    command path_1 name_1 path_2 name_2 ...

Running the program without arguments will instead begin a menu-driven interface.

Valid commands are:
    show <path> <name>
        output a stylized representation of the table to the terminal
    write <path1> <name1> <path2> <name2>
        output a stylized representation of the table in the first file into the second file
    copy <path1> <name1> <path2> <name2> ...
        creates a copy of the first file with the name/path in the second file
    append <path1> <name1> <path2> <name2> ...
        append all subsequent files onto the first file
        ''')

def write_log(log_string: str):
    with open('log.txt', 'a') as log:
        log.writelines(log_string)


def parse_arguments():
    log_string = f'{datetime.now()} : {sys.argv}\n\t'

    if len(arguments) >= 3:
        command = arguments[0]
        main_path = arguments[1]
        main_name = arguments[2]
    else: 
        log_string += "Parse Error... Terminated."
        write_log(log_string)
        raise ParseError()
        
    if len(arguments) > 4: 
        remaining_paths = arguments[3::2]
        remaining_names = arguments[4::2]
    else: 
        log_string += "Parse Error... Terminated."
        write_log(log_string)
        raise ParseError()

    if (command == 'show' 
     or command == 'write'
     or command == 'copy'
     or command == 'append'):
        log_string += f'Loading {main_path}\\{main_name}.txt ... '
        main_table = AssetManagementTable()
        main_table.append_records_from_txt_file(main_path, main_name)
        log_string +='AssetManagementTable laoded successfully!\n'

        if command == 'show':
            log_string += f'\tPreparing graphical represneation of {main_path}\\{main_name}.txt ... '
            print(main_table)
            log_string += f'Terminal output complete.\n'
        elif command == 'write':
            log_string += f'\tPreparing graphical represneation of {main_path}\\{main_name}.txt ... \n'
            log_string += f'\t\tOutputting to {remaining_paths[0]}\\{remaining_names[0]}.txt ... '
            main_table.output_to_file(remaining_paths[0], remaining_names[0])
            log_string += 'File written successfully!\n'
        elif command == 'copy':
            for path, name in zip(remaining_paths, remaining_names):
                log_string += f'\tCopying to {path}\\{name}.txt ... '
                main_table.write_table_to_txt_file(path, name)
                log_string += 'Copy complete!\n'
        elif command == 'append':
            for path, name in zip(remaining_paths, remaining_names):
                log_string += f'\tAppending {path}\\{name}.txt ... '
                main_table.append_records_from_txt_file(path, name)
                log_string += 'Appended successfully!\n'
            main_table.write_table_to_txt_file(main_path, main_name)
        else:
            log_string += "Parse Error... Terminated."
            write_log(log_string)
            raise ParseError()
    else:
        log_string += "Parse Error... Terminated."
        write_log(log_string)
        raise ParseError()
    
    write_log(log_string)


def main():

    if arguments: return parse_arguments()
    
    main_menu = Menu(
        '''
Basic Asset Management System Functioinality Test
=================================================

Main Menu
---------
1)   Create a new Table from the Terminal
2)   Load a Table from a file
3)   Add a record
4)   Display a Table
5)   Save a Table to a file
6) **Update a record
7) **Retrieve a record by its primary key
8) **Generate a report
9)   Exit the program

** = Not implemented yet.
        ''', 
        {
            1: create_table,
            2: load_file,
            3: add_record,
            4: display_table,
            5: not_implemented_yet,
            6: not_implemented_yet,
            7: not_implemented_yet,
            9: exit_program
        })
    while True: main_menu.select()
    

def clear():
    os.system('cls' if os.name == 'nt' else 'clear')

def not_implemented_yet():
    print('\nSorry, this option has not been implemented yet.\nReturning to Main Menu...\n')

def select_table() -> KeyTable:
    return Menu('Which table?', active_tables).select()

# 1) Create a new Table from the Terminal
def create_table():
    print('\nCreating a new Table...\n')
    name = input('\nInput a name for your new Table: ')
    min_key = Menu.collect_int('\nChoose a minimum valid primary key value for your new Table.')
    max_key = Menu.collect_int('\nChoose a maximum valid primary key value for your new Table.')

    categories = list()
    while True: 
        category_name = input('\nEnter a name for your first table category (column).')
        if category_name != '': break
    categories.append(category_name)

    while category_name != '':
        category_name = input('\nEnter another category (column) name for this table.\n [or press ENTER on a blank line when you are done entering column names.')
        if category_name: categories.append(category_name)

    active_tables[name] = KeyTable(categories, KeySet(min_key,max_key))

# 2)   Load a Table from a file
def load_file():
    file_path_to_load = input('\nEnter the path to the input file: ')
    file_to_load = input('\nEnter the name of the input file (no extension): ')
    
    new_table : AssetManagementTable = AssetManagementTable()
    if new_table.append_records_from_txt_file(file_path_to_load, file_to_load):
        active_tables[file_to_load] = new_table
    
# 3)   Add a record
def add_record():
    print('\nAdd a record to a table...\n')
    if active_tables:
        active_table = select_table()
        record_to_add = []
        for category in active_table.categories:
            record_to_add.append(input(f"\nEnter a value for this record's {category} category: "))

        print(f'Adding: {tuple(record_to_add)}...')
        active_table.add_records(tuple(record_to_add))

        print(active_table)
    else:
        print('\nThere are no active tables available to accept a new record.  Please create a new table.\nReturning to Main Menu...\n')

# 4)   Display a Table
def display_table():
    if active_tables: print(select_table())
    else:
        print('\nThere are no active tables available to display.  Please create a new table.\nReturning to Main Menu...\n')

# 5)   Save a Table to a file
def save_table():
    table_to_output = select_table()
    output_file_path = input('Enter the file path for the output file: ')
    output_file_name = input('Enter the file name for the output file: ')
    table_to_output.output_to_file(output_file_path, output_file_name)

# 6) **Update a record
def update_record():
    not_implemented_yet()

# 7) **Retrieve a record by its primary key
def retrieve_by_key():
    not_implemented_yet()

# 8) **Generate a report
def generate_report():
    not_implemented_yet()

# 9)   Exit the program
def exit_program():
    print('\nExiting program...\n')
    exit()


if __name__ == '__main__':
    main()