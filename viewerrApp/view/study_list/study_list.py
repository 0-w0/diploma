from view.view import View
from view.study_list.components.list_item import StudyListItem


class StudyListView(View):

    def __init__(self, **kw):
        super().__init__(**kw)
        self.model.add_observer(self)

    def on_enter(self):
        self.ids.study_list_items.clear_widgets()
        self.generate_and_added_items_to_list()

    def generate_and_added_items_to_list(self):
        for study in self.model.study_description:
            try:
                study_list_item = StudyListItem(study_id=str(study['id']))
                self.ids.study_list_items.add_widget(study_list_item)
            except ValueError:
                pass


    def on_list_item_click(self, study_id):
        self.manager.transition.direction = "left"
        self.manager_screens.get_screen("study").study_id = study_id
        self.manager_screens.current = "study"
