from flask import (render_template, request, redirect, url_for, jsonify)

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

        if request.headers.get("X-Requested-With") == "fetch":
            return jsonify(ok=True)

        return redirect(url_for("pedido.pagina_pedido"))


    def excluir_pedido(self, id):

        self.service.excluir_pedido(id)

        return jsonify(ok=True)

    def aprovar_pedido(self, id):

        self.service.aprovar_pedido(id)

        return jsonify(ok=True)