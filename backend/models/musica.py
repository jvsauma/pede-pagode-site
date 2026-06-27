class Musica:
    
    def __init__(self, id = None, nome = "", artista = "", genero = "", likes = 0, dislikes = 0, arquivo_pdf = None):
        self.id = id
        self.nome = nome
        self.artista = artista
        self.genero = genero
        self.likes = likes
        self.dislikes = dislikes
        self.arquivo_pdf = arquivo_pdf
    
    
    def adicionar_like(self):
        self.likes += 1
    
    
    def adicionar_dislike(self):
        self.dislikes += 1