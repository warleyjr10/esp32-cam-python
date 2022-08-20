# Projeto esp32-cam com python

O objetivo desse projeto é capturar imagem a partir do python utilizando o fastapi e futuramente adição de machine learning para classificação de imagens.

## Pré-requisitos:
Python 3.9+

## Para ativar o ambiente virtual no Linux:
### No terminal da IDE executar os seguintes comandos:
- python3 -m venv env
- source env/bin/activate

## Instalar as bibliotecas do projeto utilizando o comando abaixo:
- pip install -r requerimentos.txt

## Para subir a aplicação:

- uvicorn main:app --reload --port 8000