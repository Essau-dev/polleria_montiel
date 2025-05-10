import os
from dotenv import load_dotenv

# Determina el directorio base del proyecto (polleria_montiel/)
# __file__ es la ruta al archivo actual (config.py)
# os.path.dirname(__file__) es el directorio de config.py (app/)
# os.path.abspath(os.path.join(os.path.dirname(__file__), '..')) es el directorio padre (polleria_montiel/)
basedir = os.path.abspath(os.path.join(os.path.dirname(__file__), '..'))
load_dotenv(os.path.join(basedir, '.env')) # Carga variables desde el archivo .env en la raíz

class Config:
    SECRET_KEY = os.environ.get('SECRET_KEY') or 'default-secret-key-for-dev-only' # El 'or' es un fallback
    FLASK_DEBUG = os.environ.get('FLASK_DEBUG', 'False').lower() in ('true', '1', 't')

    # Configuración de SQLAlchemy
    # Usaremos SQLite para empezar. El archivo polleria.db se creará en la raíz del proyecto.
    SQLALCHEMY_DATABASE_URI = os.environ.get('DATABASE_URL') or \
        'sqlite:///' + os.path.join(basedir, 'polleria.db')
    SQLALCHEMY_TRACK_MODIFICATIONS = False

    # Puedes añadir más configuraciones aquí a medida que las necesites
    # Por ejemplo, para Flask-Mail, etc.