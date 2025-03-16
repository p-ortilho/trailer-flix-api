def dados_seriliazados(dados) -> list:
    json = [
        {
            "id": dado[0],
            "nome": dado[1],
            "cor": dado[2],
        }
        for dado in dados
    ]
    return json

def get_categorias() -> list:
    conn = db_conexao()
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM categorias")
    categorias = cursor.fetchall()
    conn.close()
    dados = dados_seriliazados(categorias)
    return dados