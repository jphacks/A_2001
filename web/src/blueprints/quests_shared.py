import logging
from flask import Blueprint, jsonify, request
from flask_jwt_extended import get_jwt_identity, jwt_required
from ..models import Quest, QuestShared
from ..database import db

quests_shared = Blueprint("quests_shared", __name__)
logger = logging.getLogger("app")


@quests_shared.route("/share", methods=["GET"])
def search_quest():
    word = request.args.get("word", type=str)
    if word is None:
        return jsonify({"message": "Bad request error"}), 400

    try:
        found_quests = (
            db.session.query(Quest, QuestShared)
            .filter(
                Quest.id == QuestShared.quest_id, Quest.content.like("%" + word + "%")
            )
            .all()
        )
    except Exception as e:
        logger.error(e)
        return jsonify({"message": "Internal server error"}), 500
    return (
        jsonify(
            {"quests": [found_quest.Quest.to_dict() for found_quest in found_quests]}
        ),
        200,
    )


# TODO: Return more information (ex: downloads, rating)
@quests_shared.route("/<int:quest_id>/share", methods=["GET"])
def get_quest(quest_id):
    try:
        quest_shared = QuestShared.query.filter(
            QuestShared.quest_id == quest_id,
        ).first()
        if quest_shared is None:
            return jsonify({"message": "Quest not found"}), 404
    except Exception as e:
        logger.error(e)
        return jsonify({"message": "Internal server error"}), 500

    quest = Quest.query.filter(Quest.id == quest_id).first()
    return jsonify(quest.to_dict()), 200


@quests_shared.route("/<int:quest_id>/share", methods=["PUT"])
@jwt_required
def start_share(quest_id):
    user_id = get_jwt_identity()
    try:
        quest = Quest.query.filter(
            Quest.user_id == user_id, Quest.id == quest_id
        ).first()
        if quest is None:
            return jsonify({"message": "Quest not found"}), 404
        quest_shared = QuestShared.query.filter(
            QuestShared.quest_id == quest_id
        ).first()
        if quest_shared is not None:
            return jsonify({"message": "Quest is already shared"}), 400
        quest_shared = QuestShared(quest_id)
        db.session.add(quest_shared)
        db.session.commit()
    except Exception as e:
        logger.error(e)
        db.session.rollback()
        return jsonify({"message": "Internal server error"}), 500
    return jsonify({}), 204


@quests_shared.route("/<int:quest_id>/share", methods=["DELETE"])
@jwt_required
def stop_share(quest_id):
    user_id = get_jwt_identity()
    try:
        quest = Quest.query.filter(
            Quest.user_id == user_id, Quest.id == quest_id
        ).first()
        if quest is None:
            return jsonify({"message": "Quest not found"}), 404
        quest_shared = QuestShared.query.filter(
            QuestShared.quest_id == quest_id
        ).first()
        if quest_shared is None:
            return jsonify({"message": "Quest is not shared"}), 400

        db.session.delete(quest_shared)
        db.session.commit()
    except Exception as e:
        logger.error(e)
        db.session.rollback()
        return jsonify({"message": "Internal server error"}), 500
    return jsonify({}), 204
