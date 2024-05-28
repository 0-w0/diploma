from view.photo.photo import PhotoView
from controller.controller import Controller
from res.photo import PhotoResource
import os


class PhotoController(Controller):

    def __init__(self, model):
        self.name = 'object'
        self.model = model
        self.view = PhotoView(controller=self, model=self.model)

    def set_data(self):
        if self.view.series_id:
            # get from db
            resp = PhotoResource().get_all_data(self.name, self.view.series_id)
            self.model.set_data(resp.data)
        else:
            if self.view.path:

                path = self.view.path
                num = 0
                for file in os.listdir(path):
                    if file.endswith('.jpg'):
                        self.model.fill_list.append({'id': str(num), 'object_path': f'{path}/{file}'})
                        num += 1

