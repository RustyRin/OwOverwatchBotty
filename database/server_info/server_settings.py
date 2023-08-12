"""
Server Settings Class

This class will be a wrapper
for the spqlite connection

funtions needed

star board
    enable
    channel id of where to post
    min reactions to post

question of the day
    enabled
    channel id for questions
    channel id for discussions
    question of the day role id for pinging
    time to post in 13:12 format
    cache size, number of days till the question can be pulled again
    baby mode (sfw version, not implemented yet)
    blacklisted question ids (not implemented yet)

points
    enabled

    bonks
        enabled
    fake bans
        enabled

movie list
    enabled

logging
    enabled
    level
        0 basic
            the bot is online
            the bot is going offline if a admin does restart command
        1
            all above
            question posted
            something made the star board
            a weekly board was posted
                duolingo
                ow comp
        2
            all above
            points added
    channel id of logging channel

duolingo
    enabled

    weekly board
        enabled

ow comp
    enabled

    weekly board
        enabled

"""
import os.path
import re
import sqlite3

"""
need a function to scrub inputs for injections!!!!

need a db_backup function to save db to file in a file format like `server_settings_1683128690.db`
    where the big number is unix time
"""


def sanitize_input(input_string: str) -> str:
    return re.sub(r'[^a-zA-Z0-9]', '', input_string)


class ServerSettingsDefaults:

    def __init__(self):
        self.logging = None
        self.logging_channel_id = None

        # connect to the db
        # see if the db even exists
        if os.path.exists("./database/server_info/server_settings.db"):
            # it exists!
            connection = sqlite3.connect("./database/server_info/server_settings.db")
            cursor = connection.cursor()
            pass
        else:
            # does not
            # connect and fill with defaults
            connection = sqlite3.connect("./database/server_info/server_settings.db")
            cursor = connection.cursor()

            cursor.execute("CREATE TABLE servers (server_id TEXT)")

        self.__cursor = cursor
        self.__connection = connection

    def exists_row(self, row_name: str) -> bool:
        # check if the server exists in the db
        self.__cursor.execute(f"SELECT * FROM servers WHERE server_id = '{row_name}'")
        rows = self.__cursor.fetchall()

        if len(rows) > 0:
            return True
        else:
            return False

    def exists_column(self, col_name: str) -> bool:
        # check the database if the column exists

        self.__cursor.execute(f"PRAGMA table_info(servers)")
        columns = self.__cursor.fetchall()
        for column in columns:
            if column[1] == col_name:
                return True

        return False

    def add_row(self, row_name: str):
        # adds a row (server) to the database
        # since this would be a new server, it will have everything disabled

        # check if row exists
        if self.exists_row(row_name=row_name):
            raise sqlite3.OperationalError("The row \"" + row_name + "\" already exists in the server table!")
        else:
            # row does not exist
            # fill with defaults / null
            pass

        self.__cursor.execute(f"INSERT INTO servers (server_id) VALUES ({row_name})")
        self.__connection.commit()

    def add_col(self, col_name: str, data_type: str):
        # adds a column (setting for servers) to the database
        if self.exists_column(col_name=col_name):
            raise sqlite3.OperationalError("The column \"" + col_name + "\" already exists in the server table!")
        else:

            # processing input type
            if data_type == "int":
                data_type = "INTEGER"
            elif data_type == "float":
                data_type = "REAL"
            elif data_type == "str":
                data_type = "TEXT"
            elif (data_type == "bytes") or (data_type == "byte"):
                data_type = "BLOB"
            else:
                raise sqlite3.DataError("Unsupported type \"" + data_type
                                        + "\". Please use one of the following: int, float, str, bytes")

            self.__cursor.execute("""ALTER TABLE servers ADD COLUMN """ + col_name + """ """ + data_type)
        pass

    def cell_read(self, row_name: str, col_name: str):
        # returns data at that coor in the db. if empty, will return None. if cell doesn't exist, will throw exception
        if self.exists_row(row_name=row_name) and self.exists_column(col_name=col_name):
            self.__cursor.execute(f"SELECT {col_name} FROM servers WHERE server_id = {row_name}")
            return self.__cursor.fetchone()
        else:
            raise sqlite3.OperationalError("The row or col you passed does not exist in the database")
        pass

    def cell_update(self, row_name: str, col_name: str, data):
        # updates data in the database

        # clean data
        if type(data) is str:
            data = sanitize_input(data)

        if self.exists_row(row_name=row_name) and self.exists_column(col_name=col_name):
            self.__cursor.execute(f"UPDATE servers SET {col_name} = {data} WHERE server_id = {row_name}")
            self.__connection.commit()
        else:
            raise sqlite3.OperationalError("The row or col you passed does not exist in the database")
        pass

    def toggle_logging(self, status: bool):
        """Turn logging on (True) or off (False)"""
        pass
