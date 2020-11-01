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
        quests = Quest.query.filter(Quest.user_id == user_id).all()
        if quests is None:
            return jsonify({"message": "User's quest not found"}), 404

        d = {}
        for quest in quests:
            l = {}
            l["name"] = quest.content
            l["exp"] = quest.exp
            d[quest.id] = l

    except Exception as e:
        logger.error(e)
        return jsonify({"message": "Internal server error"}), 500

    return jsonify({"exps": d, "level": 0, "title": " "})
