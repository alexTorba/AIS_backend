from External.NetworkModule.Handlers.MethodHandler import MethodHandler
from External.NetworkModule.Managers.NetworkManager import NetworkManager
from Microservice.ClusteringModule.ClusteringManager import ClusteringManager


class Application:
    __method_handler: MethodHandler

    def __init__(self):
        method_by_name = {
            "RunClustering": ClusteringManager.run_clustering
        }
        self.__method_handler = MethodHandler(method_by_name)

    def run(self):
        # need to in separate thread ping server every 2 minutes
        print("Microservice start listening")
        NetworkManager.start_listening(self.__method_handler)
