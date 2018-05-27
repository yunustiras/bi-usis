from flask import Flask
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__, template_folder="app/templates", static_folder='app/static')
app.config.from_pyfile("app.cfg")
db = SQLAlchemy(app)

if __name__ == "__main__":
    from app.routes import *
    from app.blueprints.users.routes import users
    app.register_blueprint(users)
    app.run(host="0.0.0.0", port=5000)
