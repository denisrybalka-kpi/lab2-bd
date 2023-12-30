from dotenv import load_dotenv
from utils.printer import Printer
from db import Base, Session, engine
from sqlalchemy.orm import relationship
from sqlalchemy import Column, Integer, String, Numeric, TIMESTAMP, ForeignKey, Table, Date
from sqlalchemy.sql import func
import time
from entities import Entity
from datetime import datetime, timedelta
import random
import math

s = Session()

class Exhibit(Entity, Base):
    __tablename__ = 'Exhibit'
    exhibit_id = Column(Integer, primary_key=True)
    exhibition_id = Column(Integer)
    name = Column(String)
    author = Column(String)
    creation_date = Column(Date)

class Exhibition(Entity, Base):
    __tablename__ = 'Exhibition'
    exhibition_id = Column(Integer, primary_key=True)
    name = Column(String)
    start_date = Column(Date)
    end_date = Column(Date)

class Museum(Entity, Base):
    __tablename__ = 'Museum'
    museum_id = Column(Integer, primary_key=True)
    name = Column(String)

class Director(Entity, Base):
    __tablename__ = 'Director'
    director_id = Column(Integer, primary_key=True)
    firstname = Column(String)
    lastname = Column(String)

class Model:
    def __init__(self):
        self.session = Session()
        self.connection = engine.connect()

    def get_table_data(self, table_name):
        c = self.conn.cursor()
        Printer.print_info(table_name)
        c.execute(f'SELECT * FROM public."{table_name}"')
        result = c.fetchall()

        Printer.print_success(f"Successfull fetch from {table_name}: {result}", 5)

    def get_all_tables_data(self):
        Printer.print_success(f"get_all_tables_data tables", 5)
    
    def print_notices(self, notices):
        for notice in notices:
            _, _, notice_text = notice.partition(':')
            clean_notice = notice_text.strip()
            Printer.print_info(clean_notice)

    def insert_data(self, table_name, data):
        try:
            if table_name == "Exhibit":
                exhibit = Exhibit(**data)
                self.session.add(exhibit)
            elif table_name == "Exhibition":
                exhibition = Exhibition(**data)
                self.session.add(exhibition)
            elif table_name == "Museum":
                museum = Museum(**data)
                self.session.add(museum)
            elif table_name == "Director":
                director = Director(**data)
                self.session.add(director)
            
            self.session.commit()
            Printer.print_success("Successfully added to {} table".format(table_name))
        except Exception as e:
            self.session.rollback()
            Printer.print_error(f"Error: {e}")
        finally:
            self.session.close()
            
    def delete_data(self, table_name, id):
        try:
            item_deleted = False

            if table_name == "Exhibit":
                exhibit = self.session.query(Exhibit).filter_by(exhibit_id=id).first()
                if exhibit:
                    self.session.delete(exhibit)
                    item_deleted = True

            elif table_name == "Exhibition":
                exhibition = self.session.query(Exhibition).filter_by(exhibition_id=id).first()
                if exhibition:
                    self.session.delete(exhibition)
                    item_deleted = True

            elif table_name == "Museum":
                museum = self.session.query(Museum).filter_by(museum_id=id).first()
                if museum:
                    self.session.delete(museum)
                    item_deleted = True

            elif table_name == "Director":
                director = self.session.query(Director).filter_by(director_id=id).first()
                if director:
                    self.session.delete(director)
                    item_deleted = True

            if item_deleted:
                self.session.commit()
                Printer.print_success(f"Removed successfully from {table_name} element with id: {id}", 5)
            else:
                Printer.print_error(f"No {table_name} with {table_name.lower()}_id {id} found.")

        except Exception as e:
            self.session.rollback()
            Printer.print_error(f"Error: {e}", 5)

        finally:
            self.session.close()


    def update_data(self, table_name, id, new_data):
        try:
            item_updated = False

            if table_name == "Exhibit":
                exhibit = self.session.query(Exhibit).filter_by(exhibit_id=id).first()
                if exhibit:
                    for key, value in new_data.items():
                        setattr(exhibit, key, value)
                    item_updated = True

            elif table_name == "Exhibition":
                exhibition = self.session.query(Exhibition).filter_by(exhibition_id=id).first()
                if exhibition:
                    for key, value in new_data.items():
                        setattr(exhibition, key, value)
                    item_updated = True

            elif table_name == "Museum":
                museum = self.session.query(Museum).filter_by(museum_id=id).first()
                if museum:
                    for key, value in new_data.items():
                        setattr(museum, key, value)
                    item_updated = True

            elif table_name == "Director":
                director = self.session.query(Director).filter_by(director_id=id).first()
                if director:
                    for key, value in new_data.items():
                        setattr(director, key, value)
                    item_updated = True

            if item_updated:
                self.session.commit()
                Printer.print_success(f"Successfully updated {table_name} table", 5)
            else:
                Printer.print_error(f"No {table_name} with {table_name.lower()}_id {id} found.")

        except Exception as e:
            self.session.rollback()
            Printer.print_error(f"Error: {e}", 5)

        finally:
            self.session.close()

    def select_data(self, selected_options):
        option_index = selected_options['option_index']
        data = selected_options['data']

        try:
            if option_index == 1:
                author_name = data['author_name']

                query = self.session.query(Exhibit.name.label('exhibit_name'),
                                           Exhibition.name.label('exhibition_name'),
                                           Exhibit.author)\
                                   .join(Exhibition, Exhibition.exhibition_id == Exhibit.exhibition_id)\
                                   .filter(Exhibit.author == author_name)

                begin = int(time.time() * 1000)
                result_objects = query.all()
                end = int(time.time() * 1000) - begin

                Printer.print_info(f"Request took {end} ms")

                Printer.print_text('fetched {}'.format(result_objects))

            elif option_index == 2:
                exhibition_id = data['exhibition_id']

                query = self.session.query(Exhibit.author)\
                                   .join(Exhibition, Exhibition.exhibition_id == Exhibit.exhibition_id)\
                                   .filter(Exhibition.exhibition_id == exhibition_id)\
                                   .group_by(Exhibit.author)

                begin = int(time.time() * 1000)
                result_objects = query.all()
                end = int(time.time() * 1000) - begin

                Printer.print_info(f"Request took {end} ms")

                result_objects = [{'author_name': author_name} for (author_name,) in result_objects]

                Printer.print_text('fetched authors: {}'.format(result_objects))

        except Exception as e:
            Printer.print_error(f"Error: {e}", 5)

        finally:
            self.session.close()
            
    def randomize_data(self, count):
        try:
            current_exhibition_id = self.session.query(func.coalesce(func.max(Exhibition.exhibition_id), 0) + 1).scalar()

            for _ in range(count):
                exhibition = Exhibition(
                    exhibition_id=current_exhibition_id,
                    name=''.join(chr(math.trunc(65 + random.random() * 26)) for _ in range(3)),
                    start_date=(datetime.now() + timedelta(days=random.uniform(0, 365))).date(),
                    end_date=(datetime.now() + timedelta(days=(random.uniform(0, 365) + 30))).date()
                )
                current_exhibition_id += 1
                self.session.add(exhibition)

            self.session.commit()

            current_exhibit_id = self.session.query(func.coalesce(func.max(Exhibit.exhibit_id), 0) + 1).scalar()

            for _ in range(count):
                exhibit = Exhibit(
                    exhibit_id=current_exhibit_id,
                    author=''.join(chr(math.trunc(65 + random.random() * 26)) for _ in range(3)),
                    creation_date=(datetime.now() - timedelta(days=random.uniform(0, 365))).date(),
                    name=''.join(chr(math.trunc(65 + random.random() * 26)) for _ in range(3)),
                    exhibition_id=self.session.query(Exhibition.exhibition_id).order_by(func.random()).first()[0]
                )
                current_exhibit_id += 1
                self.session.add(exhibit)

            self.session.commit()

            Printer.print_success(f"Successfully randomized {count} records for Exhibition and Exhibit tables", 5)

        except Exception as e:
            self.session.rollback()
            Printer.print_error(f"Error: {e}", 5)

        finally:
            self.session.close()