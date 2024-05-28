from kivymd.uix.list import ThreeLineListItem
from kivy.properties import StringProperty


class PatientsListItem(ThreeLineListItem):
    patient_id = StringProperty()
    patient_name = StringProperty()
    birth_date = StringProperty()
    sex = StringProperty()
