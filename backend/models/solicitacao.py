class Solicitacao:

    def __init__(self, id = None, nome = "", email = "", senha = "", status = "PENDING",
                 data_solicitacao = None, revisado_por = None, data_revisao = None, usuario_id = None):
        self.id = id
        self.nome = nome
        self.email = email
        self.senha = senha
        self.status = status
        self.data_solicitacao = data_solicitacao
        self.revisado_por = revisado_por
        self.data_revisao = data_revisao
        self.usuario_id = usuario_id


    def aprovar(self, revisor_id):
        self.status = "APPROVED"
        self.revisado_por = revisor_id
        return self.status


    def recusar(self, revisor_id):
        self.status = "REJECTED"
        self.revisado_por = revisor_id
        return self.status
