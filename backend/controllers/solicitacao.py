from flask import request, g, render_template, redirect, url_for, flash

from backend.services.solicitacao_service import SolicitacaoService


class SolicitacaoController:

    def __init__(self):

        self.service = SolicitacaoService()


    def exibir_pagina(self):

        return render_template("solicitacao.html")


    def criar_solicitacao(self):

        nome = request.form["nome"]

        email = request.form["email"]

        senha = request.form["senha"]

        try:
            self.service.criar_solicitacao(nome, email, senha)

        except ValueError as erro:
            flash(str(erro), "erro")
            return redirect(url_for("solicitacao.exibir_solicitacao"))

        flash("Solicitação enviada com sucesso", "sucesso")

        return redirect(url_for("solicitacao.exibir_solicitacao"))


    def listar_solicitacoes(self):

        solicitacoes = self.service.listar_solicitacoes()

        return render_template("solicitacao_admin.html", solicitacoes=solicitacoes)


    def aprovar_solicitacao(self, id):

        revisor_id = g.usuario.id

        try:
            self.service.aprovar_solicitacao(id, revisor_id)

        except ValueError as erro:
            flash(str(erro), "erro")
            return redirect(url_for("solicitacao.listar_solicitacoes"))

        flash("Solicitação aprovada com sucesso", "sucesso")

        return redirect(url_for("solicitacao.listar_solicitacoes"))


    def recusar_solicitacao(self, id):

        revisor_id = g.usuario.id

        self.service.recusar_solicitacao(id, revisor_id)

        flash("Solicitação recusada", "sucesso")

        return redirect(url_for("solicitacao.listar_solicitacoes"))