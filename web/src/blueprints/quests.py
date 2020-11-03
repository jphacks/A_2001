import logging
from flask import Blueprint, jsonify, request
from flask_jwt_extended import get_jwt_identity, jwt_required
from ..models import Quest, Task
from ..database import db

quests = Blueprint("quests", __name__)
logger = logging.getLogger("app")


@quests.route("/quests/<int:quest_id>", methods=["GET"])
@jwt_required
def get_quest(quest_id):
    user_id = get_jwt_identity()
    quest = Quest.query.filter(Quest.user_id == user_id, Quest.id == quest_id).first()
    quest_info = quest.to_dict()

    tasks_info = []
    tasks = Task.query.filter(Task.quest_id == quest_id)
    for task in tasks:
        tasks_info.append(task.to_dict())
    quest_info["tasks"] = tasks_info
    return jsonify({"quest": quest_info}), 200


@quests.route("/quests", methods=["GET"])
@jwt_required
def get_quests():
    user_id = get_jwt_identity()
    quests = Quest.query.filter(Quest.user_id == user_id).all()
    undone_dict = {quest.id: 0 for quest in quests}
    tasks = Task.query.filter(
        Task.quest_id.in_(undone_dict.keys()), Task.done.is_(False)
    )
    for task in tasks:
        undone_dict[task.quest_id] += not task.done

    quests_info = []
    for quest in quests:
        quest_info = quest.to_dict()
        quest_info["undone"] = undone_dict[quest.id]
        quests_info.append(quest_info)
    return jsonify({"quests": quests_info}), 200


@quests.route("/quests", methods=["POST"])
@jwt_required
def post_quest():
    user_id = get_jwt_identity()
    try:
        payload = request.json
        name = payload.get("name")
        category = payload.get("category")
        description = payload.get("description")
        if name is None or category is None:
            raise ValueError("name or category is None")
    except Exception as e:
        logger.error(e)
        return jsonify({"message": "Bad request error"}), 400

    try:
        quest = Quest(user_id, name, category, description)
        db.session.add(quest)
        db.session.commit()
    except Exception as e:
        logger.error(e)
        db.session.rollback()
        return jsonify({"message": "Internal server error"}), 500

    response = jsonify(quest.to_dict())
    return response, 201


@quests.route("/quests/<int:quest_id>", methods=["DELETE"])
@jwt_required
def delete_quest(quest_id):
    user_id = get_jwt_identity()
    try:
        quest = Quest.query.filter(
            Quest.user_id == user_id,
            Quest.id == quest_id,
        ).first()
        if quest is None:
            return jsonify({"message": "Quest not found"}), 404

        db.session.delete(quest)
        db.session.commit()
    except Exception as e:
        logger.error(e)
        db.session.rollback()
        return jsonify({"message": "Internal server error"}), 500

    return jsonify({}), 204


@quests.route("/quests/<int:quest_id>", methods=["PATCH"])
@jwt_required
def edit_quest(quest_id):
    user_id = get_jwt_identity()
    try:
        quest = Quest.query.filter(
            Quest.user_id == user_id, Quest.id == quest_id
        ).first()
        if quest is None:
            return jsonify({"message": "Quest not found"}), 404

        if request.json is None:
            return jsonify({"message": "Bad request error"}), 400
        payload = request.json
        name = payload.get("name")
        category = payload.get("category")
        description = payload.get("description")
        if name is None and category is None and description is None:
            return jsonify({"message": "Bad request error"}), 400

        if name is not None:
            quest.name = name
        if category is not None:
            quest.category = category
        if description is not None:
            quest.description = description
        db.session.commit()
    except Exception as e:
        logger.error(e)
        db.session.rollback()
        return jsonify({"message": "Internal server error"}), 500

    return jsonify(quest.to_dict()), 200
