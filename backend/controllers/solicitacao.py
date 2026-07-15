from flask import request, jsonify

from backend.services.solicitacao_service import SolicitacaoService


class SolicitacaoController:

    def __init__(self):

        self.service = SolicitacaoService()


    def criar_solicitacao(self):

        nome = request.form["nome"]

        email = request.form["email"]

        senha = request.form["senha"]

        try:
            self.service.criar_solicitacao(nome, email, senha)

        except ValueError as erro:
            return jsonify(ok=False, erro=str(erro)), 400

        return jsonify(ok=True), 201


    def listar_solicitacoes(self):

        solicitacoes = self.service.listar_solicitacoes()

        return jsonify([
            {
                "id": solicitacao.id,
                "nome": solicitacao.nome,
                "email": solicitacao.email,
                "status": solicitacao.status,
                "data_solicitacao": solicitacao.data_solicitacao,
                "revisado_por": solicitacao.revisado_por,
                "data_revisao": solicitacao.data_revisao,
                "usuario_id": solicitacao.usuario_id
            }
            for solicitacao in solicitacoes
        ])


    def aprovar_solicitacao(self, id):

        revisor_id = request.form["revisor_id"]

        try:
            self.service.aprovar_solicitacao(id, revisor_id)

        except ValueError as erro:
            return jsonify(ok=False, erro=str(erro)), 400

        return jsonify(ok=True)


    def recusar_solicitacao(self, id):

        revisor_id = request.form["revisor_id"]

        self.service.recusar_solicitacao(id, revisor_id)

        return jsonify(ok=True)