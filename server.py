from paste.translogger import TransLogger
from waitress import serve

from app import create_app

app = create_app()

serve(TransLogger(app, setup_console_handler=False), port=5001)
