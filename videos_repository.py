from db_con.config_db import db_conexao

def dados_seriliazados(dados):
    json = [
        {
            "id": dado[0],
            "titulo": dado[1],
            "descricao": dado[2],
            "url": dado[3],
            "categoriaId": dado[4]
        }
        for dado in dados
    ]
    return json

def get_videos():
    conn = db_conexao()
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM videos")
    videos = cursor.fetchall()
    conn.close()
    dados = dados_seriliazados(videos)
    return dados