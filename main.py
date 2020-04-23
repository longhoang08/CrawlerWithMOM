import os

from dotenv import load_dotenv

from app import app
from app import services

_DOT_ENV_PATH = os.path.join(os.path.dirname(__file__), '.env')
load_dotenv(_DOT_ENV_PATH)

if __name__ == '__main__':
    app.run(debug=True)


@app.cli.command("url-consumer")
def url_consumer():
    services.url_consumer.listen()
