# app/schemas.py
from pydantic import BaseModel # <--- CAMBIO IMPORTANTE AQUÍ

class MessageOut(BaseModel): # <--- Y AQUÍ, hereda de BaseModel
    message: str

# ... otros esquemas que definirás más adelante ...
# Todos tus esquemas de Flask-Ninja heredarán de pydantic.BaseModel