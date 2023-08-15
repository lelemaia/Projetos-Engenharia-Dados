import requests
import json
import mysql.connector

# Função que padroniza campos
def standardize_field(value):
    return value.strip().title()  # Remove espaços em excesso e capitalizar a primeira letra

# Conectando ao banco de dados MySQL
conn = mysql.connector.connect(
    host='localhost',
    user='root',
    password='sua-senha',
    database='projeto'
)
cursor = conn.cursor()

# Definindo a URL base da API do IEEE Xplore
base_url = "http://ieeexploreapi.ieee.org/api/v1/search/articles"

# Definindo os parâmetros de pesquisa
params = {
    "apikey": "sua-chave-Api",  # Chave de API
    "format": "json",    # Formato da resposta
    "max_records": 100,  # Número máximo de resultados
    "start_year": 2000,  # Ano de início da pesquisa
    "end_year": 2023,    # Ano de término da pesquisa
    "querytext": "data quality AND big data"  # Palavras-chave da pesquisa
}

# Fazendo a chamada à API usando requests
response = requests.get(base_url, params=params)

# Verificando se a chamada foi bem-sucedida
if response.status_code == 200:
    data = response.json()  # Transforma a resposta JSON em um dicionário Python
    
    # Percorrendo cada um dos artigos que foram obtidos
    for article in data['articles']:
        author_name = standardize_field(', '.join(article.get('authors', [])))
        title_text = standardize_field(article.get('title', ''))
        keywords = standardize_field(', '.join(article.get('index_terms', [])))
        abstract_text = article.get('abstract', '')  # não estamos padronizando o abstract
        publication_year = article.get('publication_year', '')
        publication_type = standardize_field(article.get('content_type', ''))
        doi_text = article.get('doi', '')  # não estamos padronizando o DOI
        
        # Inserindo os dados no banco de dados MySQL
        query = "INSERT INTO projeto (author, title, keywords, abstract, year, type_publication, doi) VALUES (%s, %s, %s, %s, %s, %s, %s)"
        values = (author_name, title_text, keywords, abstract_text, publication_year, publication_type, doi_text)
        cursor.execute(query, values)
        conn.commit()
    
    # Fechando a conexão com o banco de dados
    cursor.close()
    conn.close()
    
else:
    print("Erro na chamada à API:", response.status_code) # Em caso de erro
    