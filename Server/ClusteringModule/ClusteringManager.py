from External.NetworkModule.Data.DtoData.RequestData.RequestDto import RequestDto
from External.NetworkModule.Data.DtoData.ResponceData.ResponseDto import ResponseDto
from External.NetworkModule.Data.ExceptionsData.ServerLogicException import ServerLogicException
from Common.Dto.RunClusteringDto import RunClusteringDto
from Common.Data.ImageView import ImageView
from Server.RegistrateModule.RegistrateManager import RegistrateManager


class ClusteringManager:

    @staticmethod
    def run_clustering(dto: RequestDto[RunClusteringDto]) -> ResponseDto[RunClusteringDto]:
        data: RunClusteringDto = dto.data

        if not hasattr(data, "image_view"):
            raise ServerLogicException(401, "Received wrong data from client ! Empty ComputerFlow !")

        image_view: ImageView = ClusteringManager.__run_clustering_impl(data.image_view)
        return ResponseDto[RunClusteringDto](200, image_view)

    @classmethod
    def __run_clustering_impl(cls, image_view: ImageView) -> ImageView:
        service_count: int = RegistrateManager.get_microservices_count()

        # logic of separation image_view by service_count pieces

        # send piece of image_view to microservices

        # received all clustering image_view

        # collect all received image_view to one image and send to client

        return ImageView()
