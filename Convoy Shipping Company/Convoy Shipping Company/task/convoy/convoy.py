# Convoy Shipping Company - https://hyperskill.org/projects/151/
import pandas as pd
from sqlalchemy import MetaData, Table, inspect, exc, create_engine, Column, Integer
import json
from lxml import etree
from dicttoxml import dicttoxml
import numpy as np


class DataBase:
    def __init__(self, db_name):
        """
        Class responsible for DB creation, update, read and get/print info.
        :param db_name: the name of the database to be created
        """
        self.db_name = db_name
        self.engine = create_engine(f'sqlite:///{db_name}.s3db')
        self.inspector = inspect(self.engine)
        self.table = None
        self.table_name = None
        self.columns_structure = None

    def create(self):
        metadata = MetaData()
        self.table = Table('convoy', metadata,
                           Column('vehicle_id', Integer, primary_key=True),
                           Column('engine_capacity', Integer, nullable=False),
                           Column('fuel_consumption', Integer, nullable=False),
                           Column('maximum_load', Integer, nullable=False),
                           Column('score', Integer, nullable=False)
                           )

        metadata.create_all(self.engine)

    def read_database(self):
        self.table = pd.read_sql('select * from convoy', self.engine)
        self.get_table_info()
        return self.table

    def insert_data_in_db(self, pd_data):
        try:
            pd_data.to_sql('convoy', con=self.engine, if_exists='append', index=False)
        except exc.IntegrityError:
            print("ERROR: The Table already contain vehicles with the same IDs")
        self.read_database()

    def get_table_info(self):
        self.table_name = self.inspector.get_table_names()
        self.columns_structure = self.inspector.get_columns(self.table_name[0])


db = DataBase  # the db instance


class FileHandler:
    def __init__(self):
        """
        Handle the input, read/creation/conversion of files (except the s3db).
        Will call other classes methods to create db, clean data or print info.
        """
        self.data = None
        self.checked_data = None
        self.data_with_score = None
        self.number_of_records = None
        self.serialized_data_json = None
        self.parsed_dict_json = None
        self.xml_data = None
        self.xml_root = None
        self.json_scored = None
        self.xml_scored = None
        print("Input file name")

        try:
            self.file_name_complete = input()
            self.file_name_checked = self.file_name_complete.find("[CHECKED]")
            self.file_name = self.file_name_complete.split(sep=".")[0]
            self.file_extension = self.file_name_complete.split(sep=".")[1]
            self.clean_filename = self.file_name.split(sep="[")[0]  # Without [CHECKED]
        except IndexError:
            print("You need to put an file extension: .csv or .xlsx")
            self.__init__()

        self.select_option()

    def select_option(self):
        options = {"xlsx": self.convert_xlsx,
                   "csv": self.read_csv_data,
                   "s3db": self.save_json}
        options[self.file_extension]()

    def checked_to_s3db(self):
        global db
        db = DataBase(self.clean_filename)
        db.create()
        self.data_with_score = ModifyData.include_score(self.checked_data)
        db.insert_data_in_db(self.data_with_score)
        self.score_qualifier()
        InfoPrinter.print_rows_inserted_db(self.number_of_records, self.clean_filename)

    def read_s3db(self):
        global db
        db = DataBase(self.clean_filename)
        self.checked_data = db.read_database()
        self.data_with_score = ModifyData.include_score(self.checked_data)
        self.score_qualifier()
        self.number_of_records = self.checked_data.shape[0]

    def score_qualifier(self):
        self.json_scored = self.data_with_score[self.data_with_score["score"] > 3]
        self.xml_scored = self.data_with_score[self.data_with_score["score"] <= 3]

    def read_csv_data(self):
        try:
            self.data = pd.read_csv(self.file_name + ".csv")
        except FileNotFoundError:
            print("No such file")
            self.__init__()
        if self.file_name_checked == -1:
            self.checked_data = ModifyData.correct_data(self.data, self.file_name)
        else:
            self.checked_data = pd.read_csv(self.file_name + ".csv")
        self.number_of_records = self.checked_data.shape[0]
        self.checked_to_s3db()
        self.save_json()
        return self.checked_data

    def convert_xlsx(self):  # Open the Excel file and call save_csv to convert
        try:
            self.data = pd.read_excel(self.file_name + ".xlsx", sheet_name='Vehicles', dtype=str)
        except FileNotFoundError:
            print("No such file")
            self.__init__()
        return self.save_csv(self.file_name)

    def save_csv(self, file_name):
        """
        Save the csv, call ModifyData to correct the data, save it and return the checked_data
        to attribute. Then call checked_to_s3db() to save the checked data to s3db and save_json()
        to save the json in the correct format.
        :param file_name:
        """
        self.data.to_csv(file_name + ".csv", index=False)
        self.number_of_records = self.data.shape[0]
        InfoPrinter.print_number_of_lines(self.number_of_records, self.file_name)
        # Call the ModifyData.correct_data and save the data to attribute
        self.checked_data = ModifyData.correct_data(self.data, self.file_name)
        self.checked_to_s3db()
        self.save_json()

    @staticmethod
    def save_checked_csv(checked_data, filename):
        checked_data.to_csv(filename + "[CHECKED].csv", index=False)

    def save_json(self):  # Convert the table in the .s3db file to .json file
        self.read_s3db()
        # Drop the column score. Will not be in json or xml
        self.serialized_data_json = self.json_scored.drop(columns='score').to_dict(orient='records')
        self.parsed_dict_json = {db.table_name[0]: self.serialized_data_json}
        with open(f"{self.clean_filename}.json", "w") as json_file:
            json.dump(self.parsed_dict_json, json_file, indent=4)
        InfoPrinter.print_vehicles_saved(self.json_scored.shape[0], self.clean_filename, "json")
        self.save_xml()

    def save_xml(self):
        serialized_data_xml = self.xml_scored.drop(columns='score').to_dict(orient='records')
        parsed_dict_xml = serialized_data_xml
        self.xml_data = dicttoxml(parsed_dict_xml, attr_type=False, custom_root="convoy",
                                  item_func=lambda x: "vehicle")
        self.xml_root = etree.fromstring(self.xml_data)
        elementtree = etree.ElementTree(self.xml_root)
        # Need method="c14n" to save the <convoy> root tag correctly when there is 0 vehicles
        elementtree.write(f'{self.clean_filename}.xml', pretty_print=True, method="c14n")
        InfoPrinter.print_vehicles_saved(self.xml_scored.shape[0], self.clean_filename, "xml")


class InfoPrinter:
    @staticmethod
    def print_number_of_lines(lines_imported, file):
        if lines_imported > 1:
            print(f'{lines_imported} lines were imported to {file}.csv')
        else:
            print(f'{lines_imported} line was imported to {file}.csv')

    @staticmethod
    def print_data(data):
        print(data)

    @staticmethod
    def print_modified_info(modification_count, filename):
        print(f"{modification_count} cells were corrected in {filename}[CHECKED].csv")

    @staticmethod
    def print_rows_inserted_db(rows_inserted, filename):
        if rows_inserted > 1:
            print(f"{rows_inserted} records were inserted into {filename}.s3db")
        else:
            print(f"{rows_inserted} record was inserted into {filename}.s3db")

    @staticmethod
    def print_vehicles_saved_json(vehicles_saved, filename):
        if vehicles_saved > 1:
            print(f"{vehicles_saved} vehicles were saved into {filename}.json")
        else:
            print(f"{vehicles_saved} vehicle was saved into {filename}.json")

    @staticmethod
    def print_vehicles_saved(vehicles_saved, filename, file_extension):
        if vehicles_saved > 1 or vehicles_saved == 0:
            print(f"{vehicles_saved} vehicles were saved into {filename}.{file_extension}")
        else:
            print(f"{vehicles_saved} vehicle was saved into {filename}.{file_extension}")

    @staticmethod
    def print_table_info(database):
        database.get_table_info()
        print(f'Table name: {database.table_name[0]}')
        print(pd.DataFrame(database.columns_structure))

    @staticmethod
    def print_pretty_xml(xml_root):
        return etree.dump(xml_root)

    @staticmethod
    def print_pretty_json(parsed_dict):
        print(json.dumps(parsed_dict, indent=4, sort_keys=True))


class ModifyData:
    @staticmethod
    def correct_data(data, filename):
        corrected_data = data.replace(to_replace='[^0-9]', value='', regex=True, inplace=False)
        FileHandler.save_checked_csv(corrected_data, filename)
        # Get the number of corrections made
        modification_count = int(data.compare(corrected_data, 'index').count().sum() / 2)
        InfoPrinter.print_modified_info(modification_count, filename)
        return corrected_data

    @staticmethod
    def include_score(checked_data):
        # For some reason, the data on columns came as a string, need to be converted
        dataframe = checked_data.astype('int32')
        dataframe['fuel_autonomy'] = 450 / (dataframe['engine_capacity']
                                            / dataframe['fuel_consumption'] * 100)
        pit_stop_conditions = [dataframe['fuel_autonomy'] < 1, dataframe['fuel_autonomy'] < 2]
        dataframe['pit_stop_score'] = np.select(pit_stop_conditions, [2, 1], default=0)
        dataframe['fuel_consumed_score'] = np.select([(dataframe['fuel_consumption'] * 4.5) < 230],
                                                     [2], default=1)
        dataframe['trunk_capacity_score'] = np.select([dataframe['maximum_load'] >= 20], [2], default=0)
        dataframe['score'] = dataframe['pit_stop_score'] + dataframe['fuel_consumed_score'] \
                                                         + dataframe['trunk_capacity_score']
        dataframe.drop(columns=['fuel_autonomy', 'pit_stop_score', 'fuel_consumed_score',
                                'trunk_capacity_score'], inplace=True)
        return dataframe


data_frame = FileHandler()


# import csv
# import json
# import pandas as pd
# import re
# import sqlite3
#
# from lxml import etree
#
#
# def score_vehicle(*args):
#     route_length = 450
#     vehicle_id, engine_capacity, fuel_consumption, maximum_load = args
#     pit_stops = route_length * (fuel_consumption / 100) / engine_capacity
#     fuel_consumed = fuel_consumption * (route_length / 100)
#     score = 0 if pit_stops >= 2 else 1 if pit_stops >= 1 else 2
#     score += 2 if fuel_consumed <= 230 else 1
#     score += 2 if maximum_load >= 20 else 0
#     return score
#
#
# class Convoy:
#     def __init__(self, file):
#         self.file = file
#         self.stem = self.file.split('.')[0].replace('[CHECKED]', '')
#         self.csv_, self.csv_chkd = self.stem + '.csv', self.stem + '[CHECKED].csv'
#         self.db = self.stem + '.s3db'
#         self.json_ = self.stem + '.json'
#         self.xml_ = self.stem + '.xml'
#
#     def check_csv(self):
#         if self.file.split('.')[0].endswith('[CHECKED]'):
#             return
#         count = 0
#         with open(self.csv_, newline='') as f1, open(self.csv_chkd, 'w', newline='') as f2:
#             file_reader, file_writer = csv.reader(f1, delimiter=','), csv.writer(f2, delimiter=',')
#             headers = next(file_reader)
#             file_writer.writerow(headers)
#             pattern = re.compile(r'\D')
#             for row in file_reader:
#                 corrections = len([True for cell in row if pattern.search(cell)])
#                 file_writer.writerow([pattern.sub('', x) for x in row])
#                 count += corrections
#         print(f"{count} {'cell was' if count == 1 else 'cells were'} corrected in {self.csv_chkd}")
#
#     def export2csv(self):
#         if self.file.split('.')[1] == 'xlsx':
#             df = pd.read_excel(self.file, sheet_name='Vehicles', dtype=str)
#             count = len(df.index)
#             df.to_csv(self.csv_, index=None)
#             print(f"{count} {'line was' if count == 1 else 'lines were'} added to {self.csv_}")
#         return self.check_csv()
#
#     def export2s3db(self):
#         conn = sqlite3.connect(self.db)
#         with conn:
#             conn.execute('''create table convoy (vehicle_id int primary key, engine_capacity int not null,
#             fuel_consumption int not null, maximum_load int not null, score int not null)''')
#             with open(self.csv_chkd, newline='') as f:
#                 f_reader = csv.reader(f, delimiter=',')
#                 next(f_reader)
#                 f_entries = []
#                 for row in f_reader:
#                     scored_row = [int(x) for x in row]
#                     vehicle_score = score_vehicle(*scored_row)
#                     scored_row.append(vehicle_score)
#                     f_entries.append(tuple(scored_row))
#                 conn.executemany('insert into convoy values (?, ?, ?, ?, ?)', f_entries)
#                 count = conn.execute('select count(*) from convoy').fetchone()[0]
#         conn.close()
#         print(f"{count} {'record was' if count == 1 else 'records were'} inserted into {self.db}")
#
#     def export2json(self):
#         conn = sqlite3.connect(self.db)
#         conn.row_factory = sqlite3.Row
#         output = {'convoy': []}
#         with conn:
#             for row in conn.execute('''select vehicle_id, engine_capacity, fuel_consumption, maximum_load
#             from convoy where score > 3''').fetchall():
#                 output['convoy'].append(dict(zip(row.keys(), tuple(row))))
#         conn.close()
#         count = len(output['convoy'])
#         with open(self.json_, 'w') as jf:
#             json.dump(output, jf)
#         print(f"{count} {'vehicle was' if count == 1 else 'vehicles were'} saved into {self.json_}")
#
#     def export2xml(self):
#         conn = sqlite3.connect(self.db)
#         conn.row_factory = sqlite3.Row
#         output = {'convoy': []}
#         with conn:
#             for row in conn.execute('''select vehicle_id, engine_capacity, fuel_consumption, maximum_load
#             from convoy where score <= 3''').fetchall():
#                 output['convoy'].append(dict(zip(row.keys(), tuple(row))))
#         conn.close()
#         count = len(output['convoy'])
#         root = etree.Element('convoy')
#         for entry in output['convoy']:
#             vehicle = etree.SubElement(root, 'vehicle')
#             for key, value in entry.items():
#                 elem = etree.SubElement(vehicle, key)
#                 elem.text = str(value)
#         tree = etree.ElementTree(root)
#         tree.write(self.xml_, method="c14n")
#         print(f"{count} {'vehicle was' if count == 1 else 'vehicles were'} saved into {self.xml_}")
#
#
# if __name__ == "__main__":
#     print('Input file name')
#     input_file = input()
#     convoy = Convoy(input_file)
#     if input_file.split('.')[1] != 's3db':
#         convoy.export2csv()
#         convoy.export2s3db()
#     convoy.export2json()
#     convoy.export2xml()