from External.NetworkModule.Data.DtoData.RequestData.RequestDto import RequestDto
from External.NetworkModule.Data.DtoData.ResponceData.BaseResponseDto import BaseResponseDto
from External.NetworkModule.Data.ExceptionsData.ServerLogicException import ServerLogicException
from External.NetworkModule.Data.UrlData.UrlInfo import UrlInfo
from Server.RegistrateModule.Data.MicroservicesInfo import MicroservicesInfo


class RegistrateManager:
    __microservices: MicroservicesInfo = MicroservicesInfo()

    @staticmethod
    def registrate_microservice(dto: RequestDto[UrlInfo]) -> BaseResponseDto:
        url_info: UrlInfo = dto.data

        if not hasattr(url_info, "ip_address") or not hasattr(url_info, "port"):
            raise ServerLogicException(401, "Received wrong data from client !")

        RegistrateManager.__registrate_microservice_impl(url_info)
        return BaseResponseDto(200)

    @classmethod
    def __registrate_microservice_impl(cls, url_info: UrlInfo) -> None:
        cls.__microservices.add_microservice(url_info)

    @classmethod
    def get_microservices(cls):
        return cls.__microservices.get_microservices()

    @classmethod
    def get_microservices_count(cls) -> int:
        return cls.__microservices.get_microservice_count()
