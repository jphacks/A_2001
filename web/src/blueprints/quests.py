import logging
from flask import Blueprint, jsonify, request
from flask_jwt_extended import get_jwt_identity, jwt_required
from ..models import Quest
from ..database import db

quests = Blueprint("quests", __name__)
logger = logging.getLogger("app")


@quests.route("/quests", methods=["GET"])
@jwt_required
def get_quests():
    user_id = get_jwt_identity()
    quests = Quest.query.filter(Quest.user_id == user_id).all()
    return jsonify({"quests": [quest.to_dict() for quest in quests]})


@quests.route("/quests", methods=["POST"])
@jwt_required
def post_quest():
    user_id = get_jwt_identity()
    try:
        payload = request.json
        content = payload.get("content")
        category = payload.get("category")
        description = payload.get("description")
        if content is None or category is None:
            raise ValueError("content or category is None")
    except Exception as e:
        logger.error(e)
        return jsonify({"message": "Bad request error"}), 400

    try:
        quest = Quest(user_id, content, category, description)
        db.session.add(quest)
        db.session.commit()
    except Exception as e:
        logger.error(e)
        db.session.rollback()
        return jsonify({"message": "Internal server error"}), 500

    response = jsonify(quest.to_dict())
    return response, 201
