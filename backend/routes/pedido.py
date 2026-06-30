from flask import Blueprint

from backend.controllers.pedido import  PedidoController

pedido_bp = Blueprint("pedido" ,__name__, url_prefix="/pedido")

controller = PedidoController()


@pedido_bp.get("/")
def pagina_pedido():

    return controller.exibir_pagina()


@pedido_bp.post("/")
def criar_pedido():

    return controller.criar_pedido()