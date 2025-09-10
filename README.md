# Desafio para desenvolvedor backend júnior da Valcann
Repositório para as respostas dos desafios técnicos para vaga de desenvolvedor júnior na Valcann.

Os arquivos para a resposta de cada problema estão nas pastas ``primeira_questao``
e ``segunda_questao``.

## Para a segunda questão: 

Minha solução para a segunda questão foi feita por inteira em Python, utilizando FastAPI. Após clonar o repositório, utilize o [uv](https://docs.astral.sh/uv/) para criar o ambiente virtual necessário com os seguintes comandos:

- ``uv venv``
- ``uv sync``
- ``source .venv/bin/activate``

Então, no terminal, é possível utilizar os seguintes comandos, criados com taskipy:
- ``task run``: Inicia o servidor FastAPI em modo dev
- ``task test``: Roda testes unitários com pytest, contidos em ``segunda_questao/tests/test_users.py``.