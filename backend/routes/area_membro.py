from flask import Blueprint

from backend.controllers.area_membro import AreaMembroController
from backend.utils.decorators import login_required

area_membro_bp = Blueprint("area_membro", __name__, url_prefix="/area-membro")

controller = AreaMembroController()

@area_membro_bp.get("/")
@login_required
def pagina_inicial():

    return controller.pagina_inicial()
