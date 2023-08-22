# Projeto-Engenharia-Dados
Automatização da coleta e padronização de dados bibliográficos relevantes por meio de buscas automatizadas em sistemas acadêmicos.


# Descrição/Explicação do Código:
Este script Python que automatiza a coleta informações bibliográficas a partir de buscas em sistemas de pesquisa acadêmica usando a biblioteca `requests`, 
em seguida, padroniza os campos e insere esses dados em um banco de dados MySQL local.
Este projeto visa simplificar o processo de agregação de dados bibliográficos para pesquisadores interessados no tópico "data quality" AND "big data".
Os dados coletados incluem informações como nome dos autores, título do artigo, palavras-chave, resumo, ano de publicação, tipo de publicação e DOI.

# Recursos Principais:

- Coleta automatizada de informações bibliográficas através de consultas em sites acadêmicos.
- Filtragem e agregação de dados com base em uma string de busca predefinida.
- Tratamento e padronização dos dados coletados para garantir qualidade e consistência.
- Padronização dos campos-chave: autor, título, palavras-chave, resumo, ano, tipo de publicação, DOI.
- Armazenamento eficiente dos dados em um banco de dados MySQL, possibilitando fácil acesso e gerenciamento.

# Instruções de Uso:
1. Clone este repositório: `git clone https://github.com/lelemaia/Projeto-Engenharia-Dados.git`
2. Abra o Visual Studio Code.
3. No menu "File" (Arquivo), selecione "Open Folder" (Abrir Pasta) e escolha a pasta do repositório clonado.
5. Configure as fontes e a string de busca no arquivo de configuração YAML.
4. Abra o arquivo `conec.py`.
6. No canto superior direito do VS Code, clique no botão verde "Run" (Executar) para executar o script Python.
7. O script coletará automaticamente informações bibliográficas relevantes com base na sua string de busca e as armazenará em um banco de dados MySQL local.
#
**Developed by Lethycia Moraes Maia**

My Social Networks 😉:

GitHub: https://github.com/lelemaia

Linkedin: https://www.linkedin.com/in/lethyciamaia000o000/

Email: lethyciamaiacontato@gmail.com

