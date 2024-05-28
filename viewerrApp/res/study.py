from res.resource import Resource
from db.database import Database


class StudyResource(Resource):
    def get_list_data(self, table_name, study_id):
        connection = Database().connect()
        response = connection.table(table_name).select("*").eq('study_id', study_id).execute()
        return response
