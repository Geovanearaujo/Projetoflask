# Define a imagem base
FROM python:3.8-slim

# Define o diretório de trabalho no container
WORKDIR /app

# Copia o arquivo de dependências para o diretório de trabalho
COPY requirements.txt requirements.txt

# Instala as dependências
RUN pip install --no-cache-dir -r requirements.txt

# Copia o resto do seu código fonte para o diretório de trabalho
COPY . .

# Expõe a porta em que o Flask vai rodar
EXPOSE 5000

# Comando para rodar a aplicação
CMD ["flask", "run", "--host=0.0.0.0"]
