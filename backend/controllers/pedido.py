from flask import (render_template, request, redirect, url_for)

from backend.services.pedido_service import PedidoService


class PedidoController :

    def __init__(self):

        self.service = PedidoService()


    

    def exibir_pagina(self):

        pedidos = self.service.listar_pedido()

        return render_template("pedido.html", pedidos = pedidos)
    
    



    def criar_pedido(self):

        nome = request.form["nome_cliente"]

        musica = request.form["musica"]

        observacao = request.form["observacao"]

        self.service.criar_pedido(
            nome,
            musica,
            observacao
        )

        return redirect(url_for("pedido.pagina_pedido"))