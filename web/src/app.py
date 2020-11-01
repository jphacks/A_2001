import logging
import logging.handlers
import datetime
from flask import Flask, jsonify
from flask_jwt_extended import JWTManager
from .database import init_db
from .blueprints import api, auth, quests, tasks, subtasks
from .models import User, Quest, QuestShared, Task, Subtask
from .seeder import register_command

app = Flask(__name__)
app.config["JSON_AS_ASCII"] = False
app.config.from_object("app.config.Config")

app.config["JWT_SECRET_KEY"] = "aqwsedrftgyhujkil"
app.config["JWT_ACCESS_TOKEN_EXPIRES"] = 3600
jwt = JWTManager(app)

handler = logging.handlers.RotatingFileHandler(
    f"logs/log_{datetime.datetime.now().strftime('%Y%m%d_%H%M%S')}.log",
    "a+",
    maxBytes=3000,
    backupCount=5,
)
handler.setLevel(logging.WARN)
handler.setFormatter(
    logging.Formatter("[%(asctime)s] %(levelname)s in %(module)s: %(message)s")
)
logger = logging.getLogger("app")
logger.addHandler(handler)


app.register_blueprint(api, url_prefix="/")
app.register_blueprint(tasks, url_prefix="/quests/<int:quest_id>/")
app.register_blueprint(quests, url_prefix="/")
app.register_blueprint(
    subtasks, url_prefix="/quests/<int:quest_id>/tasks/<int:task_id>/"
)
app.register_blueprint(auth, url_prefix="/")

init_db(app)
register_command(app)


@app.route("/")
def index():
    app.logger.warn("warn")
    app.logger.error("error")
    app.logger.critical("critical")
    return jsonify({"message": "test"})


if __name__ == "__main__":
    app.run()
