# CrawlerWithMOM

#### Prerequisites
- Docker
- Docker-compose

#### Development
- Copy .env.example => .env
- Edit mapping port, or environment if need
- `docker-compose up` to start mysql and kafka
- `pip install -r requirements.txt`
- `flask db upgrade heads` to make sure you database up-to-date
-  If there is no migration before:
    - Create new migration: `flask db init` (only once)
    - Upgrade: `flask db upgrade`
    - Downgrade: `flask db downgrade`

- `flask run` to run your app.
- Swagger: http://localhost:{APP_PORT}/api

##### Module folder structure
- /api: define api url, request body, params
- /extensions: setup base configuration
- /helpers: define helper function (must be pure function)
- /models: define orm model
- /repositories: define repository to access data
- /services: handle business logic

#### Libraries
- Flask http://flask.pocoo.org/
- Flask restplus: document api https://flask-restplus.readthedocs.io/en/stable/
- SqlAlchemy: orm http://flask-sqlalchemy.pocoo.org/2.3/

