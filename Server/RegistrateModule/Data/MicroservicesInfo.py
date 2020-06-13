from typing import List

from External.NetworkModule.Data.UrlData.UrlInfo import UrlInfo


class MicroservicesInfo:
    __microservice: List[UrlInfo]

    def add_microservice(self, url_info: UrlInfo) -> None:
        if url_info not in self.__microservice:
            self.__microservice.append(url_info)

    def get_microservice_count(self) -> int:
        return len(self.__microservice)

    def get_microservices(self):
        return (i for i in self.__microservice)
