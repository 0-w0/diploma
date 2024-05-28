import abc
from db.database import Database


class Resource:
    @abc.abstractmethod
    def get_all_data(self, table_name):
        connection = Database().connect()
        response = connection.table(table_name).select("*").execute()
        return response

    @abc.abstractmethod
    def get_row_by_id(self, table_name, row_id):
        connection = Database().connect()
        response = connection.table(table_name).select("*").eq('id', row_id).execute()
        return response
