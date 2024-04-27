from db.database import Database


class Resource:
    def get_all_data(self, table_name):
        connection = Database().connect()
        response = connection.table(table_name).select("*").execute()
        return response
