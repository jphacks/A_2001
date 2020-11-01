import logging
from flask import Blueprint, jsonify, request
from flask_jwt_extended import get_jwt_identity, jwt_required
from ..models import Quest
from ..database import db

users = Blueprint("users", __name__)
logger = logging.getLogger("app")


@users.route("/users", methods=["GET"])
@jwt_required
def user_exp():
    user_id = get_jwt_identity()
    try:
        payload = request.json
        level = payload.get("level")
        title = payload.get("title")
        quests = Quest.query.filter(Quest.user_id == user_id).all()

        d = {que.id: {"exp": que.exp, "name": que.content} for que in quests}

    except Exception as e:
        logger.error(e)
        return jsonify({"message": "Internal server error"}), 500

    return jsonify({"exps": d, "level": level, "title": title})
