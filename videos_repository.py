from db_con.config_db import db_conexao

def dados_seriliazados(dados):
    json = [
        {
            "id": dado[0],
            "titulo": dado[1],
            "descricao": dado[2],
            "url": dado[3],
            "categoriaId": dado[4],
            "ativo": dado[5],
        }
        for dado in dados
    ]
    return json

def get_videos():
    conn = db_conexao()
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM videos WHERE ativo <> false")
    videos = cursor.fetchall()
    conn.close()
    dados = dados_seriliazados(videos)
    return dados

def post_videos(titulo, descricao, url, categoria_id):
    conn = db_conexao()
    cursor = conn.cursor()
    cursor.execute("INSERT INTO videos (titulo, descricao, url, categoriaid) VALUES (%s, %s, %s, %s)", (titulo, descricao, url, categoria_id))
    conn.commit()
    conn.close()
    return True

def put_videos(id, titulo, descricao, url, categoria_id):
    conn = db_conexao()
    cursor = conn.cursor()
    cursor.execute("UPDATE videos SET titulo = %s, descricao = %s, url = %s, categoriaid = %s WHERE id = %s", (titulo, descricao, url, categoria_id, id))
    conn.commit()
    conn.close()
    return True

def delete_videos(id):
    conn = db_conexao()
    cursor = conn.cursor()
    cursor.execute("UPDATE videos SET ativo = false WHERE id = %s", (id,))
    conn.commit()
    cursor.execute("UPDATE favoritos SET ativo = false WHERE videoid = %s", (id,))
    conn.close()
    return True