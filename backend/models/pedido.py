class Pedido:
    
    def __init__(self, id = None, nome_cliente = "", musica = "", observacao = "", status = "Pendente", data = None):
        self.id = id
        self.nome_cliente = nome_cliente
        self.musica = musica
        self.observacao = observacao
        self.status = status
        self.data = data
    
    
    def aprovar(self):
        self.status = "Aprovado"
        return self.status
    
    
    def recusar(self):
        self.status = "Rejeitado"
        return self.status