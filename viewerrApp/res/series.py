from res.resource import Resource
from db.database import Database


class SeriesResource(Resource):
    def get_list_data(self, table_name, series_id):
        connection = Database().connect()
        response = connection.table(table_name).select("*").eq('series_id', series_id).execute()
        return response
