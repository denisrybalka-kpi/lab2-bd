# View.py
from utils.printer import Printer
from entities import Exhibit, Exhibition, Museum, Director

class View:
    def print_menu(self, indent=0):
        Printer.print_text("Navigation Menu", indent=0)
        Printer.print_text("1. Show One Table", indent)
        Printer.print_text("2. Insert Data", indent)
        Printer.print_text("3. Delete Data", indent)
        Printer.print_text("4. Update Data", indent)
        Printer.print_text("5. Select Data", indent)
        Printer.print_text("6. Randomize Data", indent)
        Printer.print_text("7. Exit", indent)
        return input("Enter your choice: ")
    
    entities = [Exhibit, Exhibition, Museum, Director];

    def get_table_index(self):
        return int(input("Enter table index: "))
    
    def get_row_id(self):
        return int(input("Enter id: "))
    
    def get_rows_count(self):
        return int(input("Enter how many rows do you want to add: "))
    
    def get_row_index(self):
        return int(input("Enter row index: "))

    def show_table_name(self, table_name):
        Printer.print_text(table_name, indent=1)

    def show_all_tables_names(self):
        tables = self.entities

        for i, table in enumerate(tables, start=1):
            table_name = table.getName()
            self.show_table_name(f"{i}. {table_name.capitalize()}")

    def print_table_content(self, tableRows):
        if tableRows:
            for i, row in enumerate(tableRows, start=1):
                Printer.print_text(f"{i}. {row}")
        
    def exit_program(self):
        Printer.print_info("Program terminated successfully!")
    
    def get_input_data_for_table(self, table_index):
        tables = self.entities

        if 0 <= table_index <= len(tables):
            return self.get_input_data(table_index)
        else:
            Printer.print_error("Invalid table index.")

    def get_input_data(self, table_index, isUpdate=False):
        tables = self.entities

        if 0 <= table_index <= len(tables):
            return tables[table_index].get_input_data(isUpdate)
        else:
            Printer.print_error("Invalid table index.")

    def get_table_properties(self, table_index):
        tables = self.entities

        if 0 <= table_index <= len(tables):
            return tables[table_index].print_properties()
        else:
            Printer.print_error("Invalid table index.")

    def print_select_options(self):
        Printer.print_text("1. Show Exhibit by author and Exhibitions they represented at")
        Printer.print_text("2. Show list of authors that are represented at specific Exhibition")

        option_index = int(input("Enter row index (1-2): "))
        data = {}
        
        while (option_index < 1 or option_index > 3):
           option_index = int(input("Enter row index (1-2): "))

        if (option_index == 1):
            data['author_name'] = input("Enter Author name: ")
        elif (option_index == 2):
            data['exhibition_id'] = int(input("Enter Exhibition id: "))

        return {"option_index": option_index, "data": data}