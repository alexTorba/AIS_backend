from External.NetworkModule.Data.DtoData.RequestData.RequestDto import RequestDto
from External.NetworkModule.Data.DtoData.ResponceData.ResponseDto import ResponseDto
from External.NetworkModule.Data.ExceptionsData.ServerLogicException import ServerLogicException
from Server.ClusteringModule.Dto.RunClusteringDto import RunClusteringDto
from Server.ClusteringModule.Data.ImageView import ImageView


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
        return None
