from flask import Flask
from config import Config

from backend.database.schema import init_db
from backend.controllers.home_controller import home_bp
from backend.routes.repertorio import repertorio_bp
from backend.routes.pedido import pedido_bp
from backend.routes.solicitacao import solicitacao_bp

app = Flask(
    __name__,
    template_folder="frontend/templates",
    static_folder="frontend/static"
)

init_db()

app.config.from_object(Config) #Carrega as configurações

app.register_blueprint(home_bp) #register_blueprint faz o Flask pegar todas as rotas de home_bp, adicionar essas rotas à aplicação e deixa o app.py limpo.
app.register_blueprint(repertorio_bp)
app.register_blueprint(pedido_bp)
app.register_blueprint(solicitacao_bp)

if __name__ == "__main__":
    app.run(debug=True)