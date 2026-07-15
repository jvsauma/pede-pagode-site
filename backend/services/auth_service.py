from werkzeug.security import check_password_hash

from backend.database.connection import get_connection
from backend.models.usuario import Usuario


class AuthService:

    def autenticar(self, email, senha):

        connection = get_connection()

        cursor = connection.cursor()

        cursor.execute("SELECT * FROM users WHERE email = ?", (email,))

        row = cursor.fetchone()

        connection.close()

        if row is None or not check_password_hash(row["password"], senha):

            return None

        usuario = Usuario(
            id=row["id"],
            nome=row["name"],
            email=row["email"],
            senha=row["password"]
        )

        return usuario


    def buscar_por_id(self, user_id):

        connection = get_connection()

        cursor = connection.cursor()

        cursor.execute("SELECT * FROM users WHERE id = ?", (user_id,))

        row = cursor.fetchone()

        connection.close()

        if row is None:

            return None

        return Usuario(
            id=row["id"],
            nome=row["name"],
            email=row["email"],
            senha=row["password"]
        )
