from connection import get_connection


requests = [
    ("José", "Trem das Onze", "É minha música favorita", "Queijo", "01/07"),
    ("Josiane", "Cerveja de Garrafa", "É minha música favorita", "Queijo", "04/07"),
    ("Atlas", "Saudosa Maloca", "Me lembra do meu pai", "Queijo", "01/07"),
    ("Bianca", "Lapada Dela", ".", "Queijo", "01/07"),
    ("Candido", "Tempo Perdido", "Eu gosto de presunto", "Queijo", "09/05"),
    ("Flávio", "Derê", "Derê BELO", "Queijo", "11/08"),

]


def seed():
    conn = get_connection()
    cursor = conn.cursor()
    
    #verifica se existem pedidos
    cursor.execute("SELECT COUNT(*) FROM song_request")
    quantidade = cursor.fetchone()[0]
    
    if quantidade == 0:
        
        cursor.executemany(
            """
            INSERT INTO song_request
            (client_name, song_name, observation, status, created_at)
            VALUES (?, ?, ?, ?, ?)
            """,
            requests
            )
        
        
    conn.commit()
    conn.close()
    
    
if __name__ == "__main__":
    seed()