# Convoy Shipping Company - https://hyperskill.org/projects/151/
import pandas as pd
import sqlite3
from sqlite3 import Error

class FileHandler:
    def __init__(self):
        self.data = None
        self.checked_data = None
        print("Input file name")

        try:
            self.file_name_complete = input()
            self.file_name = self.file_name_complete.split(sep=".")[0]
            self.file_extension = self.file_name_complete.split(sep=".")[1]
        except IndexError:
            print("You need to put an file extension: .csv or .xlsx")
            self.__init__()

        init_conn = self.create_connection()
        self.create_tables(init_conn)
        self.select_option()
        # self.checked_data = ModifyData.correct_data(self.data, self.file_name)
        for ind in self.checked_data.index:
            # print(self.checked_data['engine_capacity'][ind], self.checked_data ['fuel_consumption'][ind])
            self.insert_into_data(init_conn,self.checked_data['vehicle_id'][ind],self.checked_data['engine_capacity'][ind], self.checked_data ['fuel_consumption'][ind],self.checked_data ['maximum_load'][ind])
        init_conn.close()

    # from sqlite3 import Error
    def create_connection(self):
        """ create a database connection to a database that resides
            in the memory
        """
        connection = None
        try:
            connection = sqlite3.connect(f'./{self.file_name}.s3db')
            return connection
        except Error as e:
            print(e)
            return connection

    def create_tables(self, conn):
        table_data = f"""
        create table if not exists {self.file_name} (
            vehicle_id INTEGER PRIMARY KEY,
            engine_capacity INTEGER NOT NULL UNIQUE
            fuel_consumption INTEGER NOT NULL UNIQUE
            maximum_load INTEGER NOT NULL UNIQUE
        )"""
        try:
            c = conn.cursor()
            c.execute(table_data)
        except Error as e:
            print(e)

    def insert_into_data(self, connection,id, capacity, consumption, load):
        try:
            cursor = connection.cursor()
            # stmt = f"insert into quantity( quantity, recipe_id, measure_id, ingredient_id) values ('{quantity}','{elements}', '{ela}', '{i}')"
            stmt = f"insert into {self.file_name}(vehicle_id, engine_capacity,fuel_consumption,maximum_load) values ('{id}','{capacity}','{consumption}','{load}')"
            # values = [*map(lambda el, e: (None, el, e), elements, ela)]
            cursor.execute(stmt)
            # cursor.executemany(stmt, values)
            connection.commit()
            return cursor
        except Error as e:
            print(e)
            return False

    def select_option(self):
        options = {"xlsx": self.convert_xlsx,
                   "csv": self.read_csv_data}
        options[self.file_extension](self.file_name)

    def read_csv_data(self, file_name):
        try:
            self.data = pd.read_csv(file_name + ".csv")
        except FileNotFoundError:
            print("No such file")
            self.__init__()
        return ModifyData.correct_data(self.data, self.file_name)

    def convert_xlsx(self, file_name):
        self.data = pd.read_excel(file_name + ".xlsx", sheet_name='Vehicles', dtype=str)
        return self.save_csv(self.file_name)

    def save_csv(self, file_name):
        self.data.to_csv(file_name + ".csv", index=False)
        FileInfo.line_counter(self.file_name)
        # Call the ModifyData.correct_data and save the data to attribute
        self.checked_data = ModifyData.correct_data(self.data, self.file_name)


    @staticmethod
    def save_checked_csv(checked_data, filename):
        checked_data.to_csv(filename + "[CHECKED].csv", index=False)


class FileInfo:
    @staticmethod
    def line_counter(file):
        csv_data_frame = pd.read_csv(file + ".csv")
        lines = csv_data_frame.shape[0]
        if lines > 1:
            print(f'{lines} lines were imported to {file}.csv')
        else:
            print(f'{lines} line was imported to {file}.csv')

    @staticmethod
    def print_data(data):
        print(data)

    @staticmethod
    def print_modified_info(modification_count, filename):
        print(f"{modification_count} cells were corrected in {filename}[CHECKED].csv")


class ModifyData:
    @classmethod
    def correct_data(cls, data, filename):
        corrected_data = data.replace(to_replace='[^0-9]', value='', regex=True, inplace=False)

        FileHandler.save_checked_csv(corrected_data, filename)
        # Get the number of corrections made
        modification_count = int(data.compare(corrected_data, 'index').count().sum() / 2)
        FileInfo.print_modified_info(modification_count, filename)
        return corrected_data


data_frame = FileHandler()