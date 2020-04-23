from flask import Blueprint
from flask_restplus import Api

api_bp = Blueprint('api', __name__, url_prefix='/api')

api = Api(
    app=api_bp,
    version='1.0',
    title='Crawler API',
    validate=False,
)

def init_app(app, **kwargs):
    from app.extensions.exceptions import global_error_handler
    from .crawler import ns as crawler_ns
    api.add_namespace(crawler_ns)
    app.register_blueprint(api_bp)
    api.error_handlers[Exception] = global_error_handler