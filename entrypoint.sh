#!/bin/bash
set -e

# Aguarda um pouco para garantir que o serviço do banco já esteja disponível (opcional)
echo "Aguardando o banco de dados ficar disponível..."
sleep 5

# Executa as migrações
echo "Executando migrações do banco de dados..."
poetry run alembic upgrade head

# Inicia o servidor uvicorn
echo "Iniciando a aplicação..."
exec poetry run uvicorn --host 0.0.0.0 --port 8000 fast_zero.app:app
