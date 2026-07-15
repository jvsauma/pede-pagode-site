from flask import Blueprint

from backend.controllers.solicitacao import SolicitacaoController

solicitacao_bp = Blueprint("solicitacao", __name__, url_prefix="/solicitacao")

controller = SolicitacaoController()


@solicitacao_bp.post("/")
def criar_solicitacao():

    return controller.criar_solicitacao()


@solicitacao_bp.get("/")
def listar_solicitacoes():

    return controller.listar_solicitacoes()


@solicitacao_bp.post("/<id_solicitacao>/aprovar")
def aprovar_solicitacao(id_solicitacao):

    return controller.aprovar_solicitacao(id_solicitacao)


@solicitacao_bp.post("/<id_solicitacao>/recusar")
def recusar_solicitacao(id_solicitacao):

    return controller.recusar_solicitacao(id_solicitacao)