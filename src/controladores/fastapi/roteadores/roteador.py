from fastapi import APIRouter

from .rotas.rotas_mssinfo import RotaMssInfo
from .rotas.rotas_materias import RotaMaterias

from ....fabricas.controladores.fastapi.fabrica_controlador_fastapi import FabricaControladorFastapi


class Roteador:

    def __call__(self, _ctrl: FabricaControladorFastapi):
        roteador = APIRouter()

        roteador.include_router(RotaMssInfo()())
        roteador.include_router(RotaMaterias()(_ctrl))

        return roteador

