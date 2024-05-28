from db.database import Database
from res.resource import Resource


class PhotoResource(Resource):

    def get_all_data(self, table_name, series_id):
        connection = Database().connect()
        response = connection.table(table_name).select("id, object_path").eq('series_id', series_id).execute()
        return response
