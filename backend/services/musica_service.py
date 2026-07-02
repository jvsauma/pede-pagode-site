from backend.database.connection import get_connection

from backend.models.musica import Musica

class MusicaService:

    def listar_repertorio(self):

        connection = get_connection()

        cursor = connection.cursor()

        cursor.execute(
            """
            SELECT *
            FROM songs
            ORDER BY name
            """
        )

        dados = cursor.fetchall()

        connection.close()

        musicas = []


        for musica in dados:

            musicas.append( 
                Musica(
                    id=musica["id"],
                    nome=musica["name"],
                    artista=musica["artist"],
                    genero=musica["genre"],
                    likes=musica["likes"],
                    dislikes=musica["dislikes"]
                    # arquivo_pdf=musica["arquivo_pdf"]
                )
            )

        return musicas
    



    def adicionar_like(self, id):

        connection = get_connection()

        connection.execute("UPDATE Musicas SET likes = likes + 1 WHERE id = ?" , id)

        connection.commit()

        connection.close()

    


    def adicionar_dislike(self, id):

        connection = get_connection()

        connection.execute("UPDATE Musicas SET dislikes = likes + 1 WHERE id = ?" , id)

        connection.commit()

        connection.close()