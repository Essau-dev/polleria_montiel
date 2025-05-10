# app/__init__.py
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_ninja import NinjaAPI
from .config import Config

db = SQLAlchemy()

#importar el router por defecto
from .api.default_api import default_router 

def create_app(config_class=Config):
    app = Flask(__name__)
    app.config.from_object(config_class)

    db.init_app(app)
    
    api_ninja = NinjaAPI(app, title="Pollería Montiel API", version="0.1.0",
                         description="API para el sistema de gestión de Pollería Montiel",
                         docs_url="/api/docs")
    

    # Añadimos el default_router con el prefijo /api
    api_ninja.add_router(prefix="/api", router=default_router)

    @app.route('/')
    def hello_flask():
        return "¡Hola, Pollería Montiel! El sistema está en camino. API en /api/docs"

    # --- Registrar Routers de Flask-Ninja para la API (más adelante) ---
    # from .api.proveedores_api import proveedores_router
    # api_ninja.add_router("/gestion", proveedores_router)
    
    return app