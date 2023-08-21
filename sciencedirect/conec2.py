import requests
import mysql.connector

# Função que padroniza campos
def standardize_field(value):
    return value.strip().title()  # Remove espaços em excesso e capitalizar a primeira letra

conn = mysql.connector.connect(
    host='localhost',
    user='root',
    password='sua-senha',
    database='projeto2'
)
cursor = conn.cursor()

# Definindo a URL da API do ScienceDirect
api_url = "https://api.elsevier.com/content/search/sciencedirect"

# Definindo os parâmetros da consulta
params = {
    "query": "bigdata",
    "apiKey": "sua-chave-api",
    "count": 30,
    "startPage": 1
}

# Fazendo a chamada à API usando requests
response = requests.get(api_url, params=params)

# Verificando se a chamada foi bem-sucedida
if response.status_code == 200:
    data = response.json()  # Convertendo a resposta JSON em um dicionário Python
    print(data)
    
    # Percorrendo as entradas no dicionário
    for entry in data['search-results']['entry']:
        title = entry['dc:title']
        authors = entry.get('authors', {}).get('author', [])
        creator = ', '.join(author['$'] for author in authors)
        publication_name = entry['prism:publicationName']
        volume = entry['prism:volume']
        doi = entry['prism:doi']
    
        print("----")
        print("Título:", title)
        print("Autor:", creator)
        print("Nome da Publicação:", publication_name)
        print("Volume:", volume)
        print("DOI:", doi)
        print("----") 
            

        # Inserindo os dados no banco de dados MySQL
        query = "INSERT INTO projeto2 ( title, creator, publication_name, volume, doi) VALUES (%s, %s, %s, %s, %s)"
        values = ( title, creator, publication_name, volume, doi)
        cursor.execute(query, values)
        conn.commit()
    
    # Fechando a conexão com o banco de dados
    cursor.close()
    conn.close()

else:
    print("Erro na chamada à API:", response.status_code)
