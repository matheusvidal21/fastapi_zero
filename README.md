[![Finalizado](https://img.shields.io/badge/Status-Conclu%C3%ADdo-brightgreen)](https://github.com/matheusvidal21/ead-microservices)

<h1 align="center"> 🚀 fastapi-zero  </h1>

**fastapi-zero** é uma aplicação web construída com **FastAPI** que oferece funcionalidades de autenticação, gerenciamento de usuários e gerenciamento de tarefas (*todos*). A aplicação utiliza o **SQLAlchemy** para interação com o banco de dados, **Alembic** para migrações, **Pydantic Settings** para configuração de ambiente e diversas outras ferramentas que auxiliam no desenvolvimento e na manutenção do código.

<p align='center'> 
    <img src="https://img.shields.io/badge/python-3670A0?style=for-the-badge&logo=python&logoColor=ffdd54"/>
    <img src="https://img.shields.io/badge/FastAPI-005571?style=for-the-badge&logo=fastapi"/>  
    <img src="https://img.shields.io/badge/sqlalchemy-D71F00?style=for-the-badge&logo=sqlalchemy&logoColor=white"/>
    <img src="https://img.shields.io/badge/-Pydantic-464646?style=for-the-badge&logo=Pydantic"/>
    <img src="https://img.shields.io/badge/-Docker-2496ED?style=for-the-badge&logo=Docker&logoColor=white"/>
    <img src="https://img.shields.io/badge/postgresql-4169e1?style=for-the-badge&logo=postgresql&logoColor=white"/>
    <img src="https://img.shields.io/badge/JWT-black?style=for-the-badge&logo=JSON%20web%20tokens"/>
</p>    

![image](https://github.com/user-attachments/assets/a5d9e0c1-ff83-4aca-98a0-50ebbfd84ca8)

## Funcionalidades ✨

- **Autenticação:** Login com JWT (JSON Web Tokens) e renovação de tokens.
- **Usuários:** Criação, listagem, atualização e remoção de usuários.
- **Tarefas (Todos):** Criação, listagem, atualização parcial e remoção de tarefas.
- **Banco de Dados:** Interação via SQLAlchemy e migrações com Alembic.
- **Segurança:** Hashing de senhas com pwdlib e validação de credenciais.
- **Ferramentas de Desenvolvimento:** 
  - **Ruff** para linting e formatação do código.
  - **Taskipy** para automação de tarefas.

## Tecnologias e Bibliotecas Utilizadas 🛠️

- [FastAPI](https://fastapi.tiangolo.com/) – Framework web moderno e de alto desempenho.
- [SQLAlchemy](https://www.sqlalchemy.org/) – ORM para interação com bancos de dados relacionais.
- [Alembic](https://alembic.sqlalchemy.org/) – Ferramenta para migrações de banco de dados.
- [Pydantic](https://pydantic-docs.helpmanual.io/) e [Pydantic Settings](https://docs.pydantic.dev/latest/concepts/pydantic_settings/) – Validação de dados e configuração via variáveis de ambiente.
- [PyJWT](https://pyjwt.readthedocs.io/) – Criação e verificação de tokens JWT.
- [pwdlib](https://frankie567.github.io/pwdlib/) – Hashing de senhas.
- [uvicorn](https://www.uvicorn.org/) – Servidor ASGI para executar a aplicação.
- [psycopg](https://www.psycopg.org/) – Driver para PostgreSQL.
- **Ferramentas de Desenvolvimento:**
  - [Ruff](https://beta.ruff.rs/) – Linter e formatador de código.
  - [Taskipy](https://github.com/taskipy/taskipy) – Gerenciador de tarefas definido no `pyproject.toml`.

## Estrutura Básica do Projeto 📁

- **`app.py`**: Arquivo principal que instancia o FastAPI e inclui os routers de autenticação, usuários e tarefas.
- **`database.py`**: Configuração do SQLAlchemy para conexão com o banco de dados.
- **`models.py`**: Definição dos modelos de dados para usuários e tarefas.
- **`schemas.py`**: Esquemas (schemas) do Pydantic para validação e serialização dos dados.
- **`security.py`**: Funções para hashing de senhas, criação de tokens JWT e verificação de usuários.
- **`settings.py`**: Configuração do ambiente via Pydantic Settings, carregando variáveis a partir do arquivo `.env`.
- **`routers/`**: Diretório contendo os routers da API:
  - **`auth.py`**: Endpoints de autenticação.
  - **`users.py`**: Endpoints para gerenciamento de usuários.
  - **`todos.py`**: Endpoints para gerenciamento de tarefas.

## Pré-requisitos ✅

- [Docker](https://www.docker.com/) e [Docker Compose](https://docs.docker.com/compose/) instalados na sua máquina.

## Como executar? ⚙️

1. **Clone o repositório:**
   ```bash
   git clone git@github.com:matheusvidal21/fastapi_zero.git
   cd fastapi_zero
   ```

2. Garanta que o script de inicialização seja executável:
   ```bash
   chmod +x entrypoint.sh
   ```

3. Construa a imagem do Docker:
   ```bash
   docker-compose build
   ```

4. Suba os containers:
   ```bash
   docker-compose up -d
   ```

Após esses passos finalizados, irá iniciar a aplicação na porta 8000 e um container PostgreSQL para o banco de dados.

## Migrações de Banco de Dados 🔄
As migrações são aplicadas automaticamente na inicialização do container através do script entrypoint.sh. Para executar as migrações manualmente, utilize:
```bash
docker-compose run app alembic upgrade head
```

## Endpoints da API 📡
### 1. Autenticação
- **`POST /auth/token`**: Realiza login e retorna um token JWT.

- **`POST /auth/refresh_token`**: Renova o token de acesso.

### 2. Usuários
- **`POST /users/`**: Cria um novo usuário.

- **`GET /users/`**: Lista os usuários.

- **`GET /users/{user_id}`**: Retorna os dados de um usuário específico.

- **`PUT /users/{user_id}`**: Atualiza os dados de um usuário.

- **`DELETE /users/{user_id}`**: Remove um usuário.

### 3. Tarefas (Todos)
- **`POST /todos/`**: Cria uma nova tarefa.

- **`GET /todos/`**: Lista as tarefas do usuário autenticado (suporta filtros de título, descrição e estado).

- **`PATCH /todos/{todo_id}`**: Atualiza parcialmente uma tarefa.

- **`DELETE /todos/{todo_id}`**: Remove uma tarefa.

## Autor 👤
Matheus Vidal – matheusvidal140@gmail.com


