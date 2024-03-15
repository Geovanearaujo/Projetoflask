from app import app, db
from flask import jsonify, request
from .models import Evento, Inscrito

@app.route('/')
def index():
    return jsonify({'message': 'Hello, World!'})

# Adicione suas rotas aqui
