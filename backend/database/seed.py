from connection import get_connection
from werkzeug.security import generate_password_hash


songs = [
    ("Pra Curtir um Pagode/Já Virou Rotina", "Di Propósito", "Pagode", 0, 0),
    ("Já É", "Jorge Aragão", "Samba", 0, 0),
    ("Eu e Você Sempre", "Jorge Aragão", "Samba", 0, 0),
    ("Problema Emocional", "Reinaldo", "Pagode", 0, 0),
    ("Deixa Acontecer", "Grupo Revelação", "Pagode", 0, 0),
    ("Deixa Alagar", "Grupo Revelação", "Pagode", 0, 0),
    ("Cheia de Manias", "Raça Negra", "Pagode", 0, 0),
    ("Bebe e Vem Me Procurar/Quem Ama Sente Saudade", "Turma do Pagode", "Pagode", 0, 0),
    ("Trem das Onze", "Fundo de Quintal", "Samba", 0, 0),
    ("Ô Queiroz", "Grupo Revelação", "Pagode", 0, 0)
]

# usuario_admin = {
#     "nome": "Admin",
#     "email": "admin@pedepagode.com",
#     "senha": generate_password_hash("admin123")
# }

usuario_admin = {
    "name": "Admin",
    "email": "admin@pedepagode.com",
    "password": generate_password_hash("admin123")
}


def seed():
    conn = get_connection()
    cursor = conn.cursor()
    
    #verifica se existem músicas
    cursor.execute("SELECT COUNT(*) FROM songs")
    quantidade = cursor.fetchone()[0]
    
    if quantidade == 0:
        
        cursor.executemany(
            """
            INSERT INTO songs
            (name, artist, genre, likes, dislikes)
            VALUES (?, ?, ?, ?, ?)
            """,
            songs
            )
        
        
    #verifica se há usuários
    cursor.execute("SELECT COUNT(*) FROM users")
    quant_users = cursor.fetchone()[0]
    
    if quant_users == 0:
        cursor.execute("""INSERT INTO users
                       (name, email, password)
                       VALUES (?, ?, ?)
                       """,
                       (usuario_admin["name"], usuario_admin["email"], usuario_admin["password"])
                       )
        
    conn.commit()
    conn.close()
    
    
if __name__ == "__main__":
    seed()