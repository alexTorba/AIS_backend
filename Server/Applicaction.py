from External.NetworkModule.Handlers.MethodHandler import MethodHandler
from External.NetworkModule.Managers.NetworkManager import NetworkManager
from Server.ClusteringModule.ClusteringManager import ClusteringManager
from Server.RegistrateModule.RegistrateManager import RegistrateManager


class Application:
    __method_handler: MethodHandler

    def __init__(self):
        method_by_name = {
            "RunClustering": ClusteringManager.run_clustering,
            "RegistrateMicroservice": RegistrateManager.registrate_microservice
        }
        self.__method_handler = MethodHandler(method_by_name)

    def run(self):
        print("Server start listening..")
        NetworkManager.start_listening(self.__method_handler)
