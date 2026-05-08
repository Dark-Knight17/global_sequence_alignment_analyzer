from flask import Flask
import os

def create_app():
    app = Flask(__name__, instance_relative_config=True)
    
    # Ensure instance folder exists
    try:
        os.makedirs(app.instance_path)
    except OSError:
        pass
    
    with app.app_context():
        from .services.history_service import HistoryService
        HistoryService.init_db()
    
    # Register blueprints
    from .routes.main import main_bp
    app.register_blueprint(main_bp)
    
    return app
