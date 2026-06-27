from backend.controllers.repertorio import RepertorioController
from flask import Blueprint

repertorio_bp = Blueprint("repertorio" , __name__ , url_prefix="/repertorio")

controller = RepertorioController()

@repertorio_bp.get("/")
def listar_repertorio():
    return controller.listar_repertorio()


@repertorio_bp.post("/like/<int:musica_id>")
def adicionar_like(musica_id):
    return controller.adicionar_like(musica_id)


@repertorio_bp.post("/dislike/<int:musica_id>")
def adicionar_like(musica_id):
    return controller.adicionar_dislike(musica_id)