from datetime import datetime

from backend.database.connection import get_connection
from backend.models.pedido import Pedido


class PedidoService:

    @staticmethod
    def criar_pedido(nome, musica, observacao):

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

            INSERT INTO pedidos(

                nome_cliente,
                musica,
                observacao,
                status,
                data

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




    @staticmethod
    def listar_pedido(self):

        connection = get_connection()

        cursor = connection.cursor()

        cursor.execute("""

            SELECT *
            FROM Pedido
            ORDER BY data ASC

        """)

        rows = cursor.fetchall()

        pedidos = []

        for row in rows:

            pedido = Pedido(

                id=row["id"],

                nome_cliente=row["nome_cliente"],

                musica=row["musica"],

                observacao=row["observacao"],

                status=row["status"],

                data=row["data"]

            )

            pedidos.append(pedido)


        return pedidos

