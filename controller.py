from model import Model
from view import View
from utils.printer import Printer
import sys

class Controller:
    def __init__(self):
        self.model = Model()
        self.view = View()

    def run(self):
        while True:
            choice = self.view.print_menu(indent=1)

            if choice == "1":
                self.show_one_table()
            elif choice == "2":
                self.insert_data()
            elif choice == "3":
                self.delete_data_from_table()
            elif choice == "4":
                self.update_data()
            elif choice == "5":
                self.select_data()
            elif choice == "6":
                self.randomize_data()
            elif choice == "7":
                self.exit_program()
                break
            else:
                Printer.print_error("Invalid choice. Please try again.", indent=1)

    def get_table_index(self):
        self.view.show_all_tables_names()
        table_index = self.view.get_table_index()

        return table_index
    
    def get_table_row_index(self, table_name):
        tableData = self.model.get_table_data(table_name)
        self.view.print_table_content(tableData)
        row_index = self.view.get_row_index()

        return row_index

    def show_one_table(self):
        tables = self.view.entities
        table_index = self.get_table_index() - 1
        table_name = tables[table_index].getName()

        tableData = self.model.get_table_data(table_name)
        self.view.print_table_content(tableData)

    def show_all_tables(self):
        self.model.get_all_tables_data()

    def insert_data(self):
        tables = self.view.entities
        table_index = self.get_table_index() - 1
        input_data = self.view.get_input_data_for_table(table_index)
        table_name = tables[table_index].getName()

        self.model.insert_data(table_name, input_data)

    def delete_data_from_table(self):
        tables = self.view.entities
        table_index = self.get_table_index() - 1
        table_name = tables[table_index].getName()
        id = self.view.get_row_id()

        self.model.delete_data(table_name, id)

    def update_data(self):
        tables = self.view.entities
        table_index = self.get_table_index() - 1
        table_name = tables[table_index].getName()
        id = self.view.get_row_id()
        new_data = self.view.get_input_data(table_index, isUpdate=True)


        self.model.update_data(table_name, id, new_data)

    def select_data(self):
        selected_options = self.view.print_select_options()

        self.model.select_data(selected_options)


    def randomize_data(self):
        count = self.view.get_rows_count()

        self.model.randomize_data(count)

    def exit_program(self):
        self.view.exit_program()
        sys.exit()
