from KeyTable import KeyTable
from KeySet import Key, KeySet
from datetime import date
import sys
import os

class AssetManagementTable(KeyTable):
    
    def __init__(self, primary_key_set = KeySet(0, 99999)) -> None:
        categories = ('Asset Description', 'Location', 'Purchase Date', 'Purchase Price', 'End of Life (EOL)', '% Value at EOL')
        super().__init__(categories, primary_key_set=primary_key_set)
    
    def append_records_from_txt_file(self, file_path: str = os.path.realpath('.'), file_name: str = "assets") -> None:
        SUCCESS = 1
        FAILURE = None

        if os.name == 'nt':
            file_to_open = f'{file_path}\\{file_name}.txt' 
        else:
            file_to_open = linux_interaction.win_path_to_linux_path(file_to_open)

        try:
            with open(file_to_open, 'r') as input_file:
                raw_input = input_file.readlines()
                for raw_line in raw_input:
                    fields = raw_line.split(', ')
                    description = fields[0]
                    location = fields[1]
                    raw_purchase_date = [int(number) for number in fields[2].split('-')]
                    purchase_year = raw_purchase_date[0]
                    purchase_month = raw_purchase_date[1]
                    purchase_day = raw_purchase_date[2]
                    purchase_date = date(purchase_year, purchase_month, purchase_day)
                    purchase_price = Money(int(fields[3]))
                    raw_eol = [int(number) for number in fields[4].split('-')]
                    eol_year = raw_eol[0]
                    eol_month = raw_eol[1]
                    eol_day = raw_eol[2]
                    eol_date = date(eol_year, eol_month, eol_day)
                    value_at_eol = Percent(float(fields[5]))
                    self.add_records((description, location, purchase_date, purchase_price, eol_date, value_at_eol))
                return SUCCESS
        except FileNotFoundError:
            print(f'\nFailed to append from {file_to_open}, no such file was found!\n')
            return FAILURE
    
    def write_table_to_txt_file(self, file_path:str, file_name:str) -> None:
        output = []
        for line, record in enumerate(self.__records.values()):
            print(f'{record[line]}')
            output.append(record)
        
        if os.name == 'nt':
            file_to_open = f'{file_path}\\{file_name}.txt' 
        else:
            file_to_open = linux_interaction.win_path_to_linux_path(file_to_open)
        
        with open(file_to_open, 'a') as output_file:
            output_file.writelines(output)

class Money(float):
    def __str__(self) -> str:
        return f'${self.__float__():>13,.2f}'

class Percent(float):
    def __str__(self) -> str:
        return f'{self.__float__():.0%}'


#######################################################
#Testing code:
#######################################################
if __name__ == '__main__':
    my_assets = AssetManagementTable()
    some_records =  (
        ('Laptop-1', 'Recruiting', date(2018, 4, 12), Money(4_000), date(2022, 4, 12), Percent(0.1)),
        ('Laptop-2', 'Recruiting', date(2018, 4, 12), Money(4_000), date(2022, 4, 12), Percent(0.1))
    )
    print('\nAdding a record directly from tuple argument:')
    my_assets.add_records(('Laptop-0', 'Recruiting', date(2018, 4, 12), Money(4_000), date(2022, 4, 12), Percent(0.1)))
    print(my_assets)

    print('\nAdding multiple records indirectly from a nested tuple variable:')
    my_assets.add_records(some_records)
    print(my_assets)

    print('\nAdding multiple records by appending from a .txt file:')
    my_assets.append_records_from_txt_file()
    print(my_assets)
    