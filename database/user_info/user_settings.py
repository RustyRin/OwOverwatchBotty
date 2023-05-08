"""
This is supposed to be a user version of
server_settings.py

This will
"""
import os.path
import re
import sqlite3


def sanitize_input(input_string: str) -> str:
    return re.sub(r'[^a-zA-Z0-9]', '', input_string)


class UserSettingsDefaults:
    def __init__(self):
        self.preferred_name = None
        self.pronouns = None


class UserSettings(UserSettingsDefaults):
    def __init__(self):

        # does db exist?
        if os.path.exists("./database/user_info/user_settings.db"):
            # it exists!

            connection = sqlite3.connect("./database/user_info/user_settings.db")
            cursor = connection.cursor()
            pass
        else:
            # it does not exist
            # make it
            connection = sqlite3.connect("./database/user_info/user_settings.db")
            cursor = connection.cursor()

            # make table
            cursor.execute("CREATE TABLE users (user_id TEXT)")

        self.__cursor = cursor
        self.__connection = connection

    def exists_row(self, row_name: str) -> bool:
        """Checks if row exists in the user batabase"""

        self.__cursor.execute(f"SELECT * FROM users WHERE user_id = {row_name}")
        rows = self.__cursor.fetchall()

        if len(rows) > 0:
            return True
        else:
            return False

    def exists_column(self, col_name: str) -> bool:
        """Checks if the column exists inthe user database"""

        self.__cursor.execute("PRAGMA table_info(users)")
        columns = self.__cursor.fetchall()
        for column in columns:
            if column[1] == col_name:
                return True

        return False

    def add_row(self, row_name: str):
        """Adds a row (individual user) to the user database with a given user id"""

        if self.exists_row(row_name=row_name):
            raise Exception("The row \"" + row_name + "\" already exists in the user table")
        else:
            # the row does not exist
            # you can cont.
            pass

        self.__cursor.execute(f"INSERT INTO users (user_id) VALUES ({row_name})")
        self.__connection.commit()
