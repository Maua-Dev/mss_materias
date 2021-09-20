from fastapi import FastAPI

from src.config.proj_config import ProjConfig
from src.config.enums.fastapi import *
from src.controladores.fastapi.c_get_all_materias import CGetAllMateriasFastapi
from src.interfaces.i_getters_materias import IGettersMaterias


class FabricaControladorFastapi:
    repo: IGettersMaterias

    __config__: dict

    protocolo: str
    host: str
    porta: str
    root: str
    url: str

    app: FastAPI

    def __init__(self, repo: IGettersMaterias):
        self.repo = repo

        self.__config__ = ProjConfig.getFastapi()

        self.protocolo = self.__config__[KEY.PROTOCOLO.value]
        self.host = self.__config__[KEY.HOST.value]
        self.porta = self.__config__[KEY.PORTA.value]
        self.root = self.__config__[KEY.ROOT.value]
        self.url = f'{self.protocolo}://{self.host}:{self.porta}{self.root}'

        self.app = FastAPI()

    def getAllMaterias(self):
        return CGetAllMateriasFastapi(self.repo)
