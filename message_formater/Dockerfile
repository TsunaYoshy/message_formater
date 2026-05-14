FROM python:3.11-slim

# Diretório interno do container
WORKDIR /app

# Copia requirements
COPY requirements.txt .

# Instala dependências
RUN pip install --no-cache-dir -r requirements.txt

# Copia projeto
COPY . .

# Executa aplicação
CMD ["python", "message_formater.py"]