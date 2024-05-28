from res.resource import Resource
from db.database import Database


class PatientResource(Resource):
    def get_list_data(self, table_name, patient_id):
        connection = Database().connect()
        response = connection.table(table_name).select("*").eq('patient_id', patient_id).execute()
        return response

