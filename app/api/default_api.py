from flask_ninja import Router
#from pydantic import BaseModel, MesaggeOut ya utiliza BaseModel, linea comentada, para proxima eliminacion.
from ..schemas import MessageOut

default_router = Router()

@default_router.get("/hello-ninja", responses={200: MessageOut})
def hello_ninja_endpoint(): #creamos y nombramos la función
    # Devuelve una instancia del esquema MessageOut
    return MessageOut(message="¡Hola desde Flask-Ninja usando default_api.py!")