from flask import Blueprint

from backend.controllers.solicitacao import SolicitacaoController
from backend.utils.decorators import login_required

solicitacao_bp = Blueprint("solicitacao", __name__, url_prefix="/solicitacao")

controller = SolicitacaoController()


@solicitacao_bp.post("/")
def criar_solicitacao():

    return controller.criar_solicitacao()


@solicitacao_bp.get("/")
@login_required
def listar_solicitacoes():

    return controller.listar_solicitacoes()


@solicitacao_bp.post("/<id_solicitacao>/aprovar")
@login_required
def aprovar_solicitacao(id_solicitacao):

    return controller.aprovar_solicitacao(id_solicitacao)


@solicitacao_bp.post("/<id_solicitacao>/recusar")
@login_required
def recusar_solicitacao(id_solicitacao):

    return controller.recusar_solicitacao(id_solicitacao)