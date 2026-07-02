from connection import get_connection

def reset_db():
    conn = get_connection()
    cursor = conn.cursor()
    
    #apaga as músicas, os usuários e os pedidos

    cursor.execute("DELETE FROM songs")
    cursor.execute("SELECT * FROM songs")

    cursor.execute("DELETE FROM song_request")
    cursor.execute("SELECT * FROM song_request")
    
    cursor.execute("DELETE FROM users")
    cursor.execute("SELECT * FROM users")
    
    cursor.execute("DELETE FROM sqlite_sequence")
    cursor.execute("SELECT * FROM sqlite_sequence")
        
        
    conn.commit()
    conn.close()
    
    
if __name__ == "__main__":
    reset_db()