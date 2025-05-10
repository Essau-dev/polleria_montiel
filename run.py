from app import create_app, db # Importamos create_app y db desde el paquete app (app/__init__.py)

app = create_app()

if __name__ == "__main__":
    # Este bloque with app.app_context() es importante para que SQLAlchemy
    # sepa a qué aplicación pertenecen las operaciones de base de datos.
    with app.app_context():
        # db.drop_all() # Descomenta con cuidado si necesitas borrar y recrear todas las tablas
        db.create_all() # Crea las tablas definidas en models.py si no existen
                        # Esto es para desarrollo inicial. Para producción/cambios, usa Alembic.
    
    # Obtenemos el valor de DEBUG de la configuración de la app
    # El segundo argumento de app.config.get es un valor por defecto si no se encuentra.
    debug_mode = app.config.get('FLASK_DEBUG', False) 
    app.run(debug=debug_mode, host='0.0.0.0', port=5000)