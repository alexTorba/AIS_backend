from External.JsonFomatterModule.JsonContract import JsonContract
from Server.ClusteringModule.Data.ImageView import ImageView


class RunClusteringDto(JsonContract):
    image_view: ImageView
    __json_fields = {
        "i": "image_view"
    }

    def __init__(self, image_view: ImageView = None):
        super().__init__(self.__json_fields)
        if image_view is not None:
            self.image_view = image_view
