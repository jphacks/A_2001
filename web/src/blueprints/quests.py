import logging
from flask import Blueprint, jsonify, request
from ..models import Quest
from ..database import db

quests = Blueprint("quests", __name__)
logger = logging.getLogger("app")


@quests.route("/quests", methods=["GET"])
def get_quests():
    user_id = 1  # dummy
    quests = Quest.query.filter(Quest.user_id == user_id).all()
    return jsonify({"quests": [quest.to_dict() for quest in quests]})


@quests.route("/quests", methods=["POST"])
def post_quest():
    user_id = 1  # dummy
    payload = request.json
    content = payload.get("content")
    category = payload.get("category")

    try:
        quest = Quest(user_id, content, category)
        db.session.add(quest)
        db.session.commit()
    except Exception as e:
        logger.error(e)
        db.session.rollback()
        return jsonify({"message": "Internal server error"}), 500

    response = jsonify(quest.to_dict())
    return response, 201
