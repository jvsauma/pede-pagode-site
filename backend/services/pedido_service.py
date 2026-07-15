from datetime import datetime

from backend.database.connection import get_connection
from backend.models.pedido import Pedido


class PedidoService:

    
    def criar_pedido(self, nome, musica, observacao):

        pedido = Pedido(

            nome_cliente=nome,

            musica=musica,

            observacao=observacao,  

            status="Pendente",

            data=datetime.now()

        )

        connection = get_connection()

        cursor = connection.cursor()

        cursor.execute("""

            INSERT INTO song_request(

                client_name,
                song_name,
                observation,
                status,
                created_at

            )

            VALUES (?, ?, ?, ?, ?)

        """,

        (

            pedido.nome_cliente,

            pedido.musica,

            pedido.observacao,

            pedido.status,

            pedido.data

        ))


        connection.commit()

        connection.close()




    
    def listar_pedido(self):

        connection = get_connection()

        cursor = connection.cursor()

        cursor.execute("""

            SELECT *
            FROM song_request
            ORDER BY created_at ASC

        """)

        rows = cursor.fetchall()

        pedidos = []

        for row in rows:

            pedido = Pedido(

                id=row["id"],

                nome_cliente=row["client_name"],

                musica=row["song_name"],

                observacao=row["observation"],

                status=row["status"],

                data=row["created_at"]

            )

            pedidos.append(pedido)


        return pedidos

    def excluir_pedido(self, id):

        connection = get_connection()

        cursor = connection.cursor()

        cursor.execute("""

                       DELETE FROM song_request
                       WHERE id = ?

        """, (id,))

        connection.commit()
        connection.close()


    def aprovar_pedido(self, id):

        connection = get_connection()

        cursor = connection.cursor()

        cursor.execute("""

            UPDATE song_request
            SET status = 'Aprovado'
            WHERE id = ?

        """, (id,))

        connection.commit()
        connection.close()

