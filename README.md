# Projetoflask
Requisitos
Python 3.8+
pip (gerenciador de pacotes Python)
Docker

1. Configuração do Ambiente Virtual e Instalação de Dependências
A. Criar Ambiente Virtual:

No diretório do projeto, execute:
python3 -m venv venv

Windows:
venv\Scripts\activate

macOS/Linux:
source venv/bin/activate

A. Instalar Dependências:

Assegure-se de ter um requirements.txt no diretório do projeto e execute:

pip install -r requirements.txt

Construir e Executar com Docker
B. Construir Imagem Docker:

No diretório do projeto, execute:
docker build -t nome_da_sua_imagem .
docker run -d -p 5000:5000 nome_da_sua_imagem

2. Acessar Aplicação
Após executar o container, acesse http://localhost:5000 no navegador.

3. Finalização
Para desativar o ambiente virtual quando terminar:

Em qualquer SO:
deactivate






