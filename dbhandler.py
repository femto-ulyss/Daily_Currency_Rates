import cx_Oracle
import settingsloader


class DatabaseHandler:
    """Database connection and query execution"""

    def __init__(self):

        self.check = 0
        self.connector = cx_Oracle.connect(settingsloader.db_login,
                                           settingsloader.db_password,
                                           cx_Oracle.makedsn(settingsloader.db_host,
                                                             settingsloader.db_port,
                                                             settingsloader.db_name))
        self.cursor = self.connector.cursor()

    def execute_query(self, query):

        self.cursor.execute(query)
        self.connector.commit()

    def check_already_inserted(self):

        self.cursor.execute(settingsloader.check_query)
        self.check = self.cursor.fetchall()[0][0]
        return self.check

    def close_connection (self):

        self.connector.close()
