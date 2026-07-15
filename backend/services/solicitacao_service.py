from datetime import datetime

from werkzeug.security import generate_password_hash

from backend.database.connection import get_connection
from backend.models.solicitacao import Solicitacao


class SolicitacaoService:


    def criar_solicitacao(self, nome, email, senha):

        connection = get_connection()

        cursor = connection.cursor()

        if not self._email_disponivel(cursor, email):
            connection.close()
            raise ValueError("Este e-mail já está cadastrado ou aguardando aprovação.")

        solicitacao = Solicitacao(
            nome=nome,
            email=email,
            senha=generate_password_hash(senha),
            status="PENDING",
            data_solicitacao=datetime.now()
        )

        cursor.execute("""

            INSERT INTO membership_requests(
                name,
                email,
                password,
                status,
                requested_at
            )

            VALUES (?, ?, ?, ?, ?)

        """,

        (
            solicitacao.nome,
            solicitacao.email,
            solicitacao.senha,
            solicitacao.status,
            solicitacao.data_solicitacao
        ))

        connection.commit()
        connection.close()


    def _email_disponivel(self, cursor, email):

        cursor.execute("SELECT 1 FROM users WHERE email = ?", (email,))

        if cursor.fetchone():
            return False

        cursor.execute("""

            SELECT 1 FROM membership_requests
            WHERE email = ? AND status = 'PENDING'

        """, (email,))

        if cursor.fetchone():
            return False

        return True


    def listar_solicitacoes(self):

        connection = get_connection()

        cursor = connection.cursor()

        cursor.execute("""

            SELECT *
            FROM membership_requests
            ORDER BY requested_at ASC

        """)

        rows = cursor.fetchall()

        connection.close()

        solicitacoes = []

        for row in rows:

            solicitacoes.append(Solicitacao(
                id=row["id"],
                nome=row["name"],
                email=row["email"],
                senha=row["password"],
                status=row["status"],
                data_solicitacao=row["requested_at"],
                revisado_por=row["reviewed_by"],
                data_revisao=row["reviewed_at"],
                usuario_id=row["user_id"]
            ))

        return solicitacoes


    def aprovar_solicitacao(self, id, revisor_id):

        connection = get_connection()

        cursor = connection.cursor()

        cursor.execute("""

            SELECT * FROM membership_requests
            WHERE id = ? AND status = 'PENDING'

        """, (id,))

        row = cursor.fetchone()

        if row is None:
            connection.close()
            raise ValueError("Solicitação não encontrada ou já revisada.")

        cursor.execute("""

            INSERT INTO users(name, email, password)
            VALUES (?, ?, ?)

        """, (row["name"], row["email"], row["password"]))

        usuario_id = cursor.lastrowid

        cursor.execute("""

            UPDATE membership_requests
            SET status = 'APPROVED',
                reviewed_by = ?,
                reviewed_at = ?,
                user_id = ?
            WHERE id = ?

        """, (revisor_id, datetime.now(), usuario_id, id))

        connection.commit()
        connection.close()


    def recusar_solicitacao(self, id, revisor_id):

        connection = get_connection()

        cursor = connection.cursor()

        cursor.execute("""

            UPDATE membership_requests
            SET status = 'REJECTED',
                reviewed_by = ?,
                reviewed_at = ?
            WHERE id = ? AND status = 'PENDING'

        """, (revisor_id, datetime.now(), id))

        connection.commit()
        connection.close()