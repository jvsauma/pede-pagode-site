from flask import Flask
from config import Config

from backend.database.schema import init_db
from backend.controllers.home_controller import home_bp

app = Flask(__name__)

init_db()

app.config.from_object(Config) #Carrega as configurações

app.register_blueprint(home_bp) #register_blueprint faz o Flask pegar todas as rotas de home_bp, adicionar essas rotas à aplicação e deixa o app.py limpo.

if __name__ == "__main__":
    app.run(debug=True)