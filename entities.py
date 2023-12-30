from utils.printer import Printer
from datetime import date, datetime

class Entity:
    def __init__(self, **kwargs):
        for key, value in kwargs.items():
            setattr(self, key, value)
            
    @classmethod
    def get_input_data(cls, isUpdate):
        input_data = {}
        for prop, prop_type in cls.__init__.__annotations__.items():
            if not (isUpdate and ('_id' in prop)):
                value = cls.get_valid_input(f"Enter {prop} ({prop_type.__name__}): ", prop_type)
                input_data[prop] = value
        return input_data
        
    @classmethod
    def print_properties(self):
        for i, prop in self.__init__.__annotations__.items():
            Printer.print_text(f"{i}. {prop}")

    @classmethod
    def getName(cls):
        return cls.__name__

    @staticmethod
    def get_valid_input(prompt: str, data_type: type):
        while True:
            try:
                if data_type == date:
                    user_input = date.fromisoformat(input(prompt))

                    user_input = user_input.strftime('%Y-%m-%d')
                else:
                    user_input = data_type(input(prompt))
                    
                return user_input
            except ValueError:
                Printer.print_error(f"Invalid input. Please enter a valid {data_type.__name__}.")
    def __repr__(self):
        props = ', '.join([f"{key}={getattr(self, key)}" for key in self.__dict__])
        return f"<{self.__class__.__name__}({props})>"


class Exhibit(Entity):
    def __init__(self, exhibit_id: int, exhibition_id: int, name: str, author: str, creation_date: date):
        super().__init__(exhibit_id=exhibit_id, exhibition_id=exhibition_id, name=name, author=author, creation_date=creation_date)

class Exhibition(Entity):
    def __init__(self, exhibition_id: int, name: str, start_date: date, end_date: date):
        super().__init__(exhibition_id=exhibition_id, name=name, start_date=start_date, end_date=end_date)


class Museum(Entity):
    def __init__(self, museum_id: int, name: str):
        super().__init__(museum_id=museum_id, name=name)


class Director(Entity):
    def __init__(self, director_id: int, firstname: str, lastname: str):
        super().__init__(director_id=director_id, firstname=firstname, lastname=lastname)
