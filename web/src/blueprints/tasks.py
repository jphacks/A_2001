import logging
from flask import jsonify, Blueprint, request
from flask_jwt_extended import get_jwt_identity, jwt_required
from ..models import Quest, Task
from ..database import db

tasks = Blueprint("tasks", __name__)
logger = logging.getLogger("app")


def find_quest(user_id, quest_id):
    try:
        quest = Quest.query.filter(
            Quest.user_id == user_id,
            Quest.id == quest_id,
        ).first()
        if quest is None:
            raise ValueError("Quest not found")

    except ValueError as ve:
        raise ve
    except Exception as e:
        logger.error(e)
        raise Exception("Internal server error")


@tasks.route("/tasks", methods=["GET"])
@jwt_required
def get_task(quest_id):
    user_id = get_jwt_identity()

    try:
        find_quest(user_id, quest_id)
    except ValueError as ve:
        return jsonify({"message": str(ve)}), 404
    except Exception as e:
        logger.error(e)
        return jsonify({"message": "Internal server error"}), 500

    try:
        tasks = Task.query.filter(Task.quest_id == quest_id).all()
    except Exception as e:
        logger.error(e)
        return jsonify({"message": "Internal server error"}), 500

    return jsonify({"tasks": [task.to_dict() for task in tasks]}), 200


@tasks.route("/tasks", methods=["POST"])
@jwt_required
def post_task(quest_id):
    user_id = get_jwt_identity()

    try:
        find_quest(user_id, quest_id)
    except ValueError as ve:
        return jsonify({"message": str(ve)}), 404
    except Exception as e:
        logger.error(e)
        return jsonify({"message": "Internal server error"}), 500

    try:
        payload = request.json
        content = payload.get("content")
        description = payload.get("description")
        if content is None:
            raise ValueError("content is None")
    except Exception:
        return jsonify({"message": "Bad request error"}), 400

    try:
        task = Task(quest_id, content, description)
        db.session.add(task)
        db.session.commit()
    except Exception as e:
        logger.error(e)
        db.session.rollback()
        return jsonify({"message": "Internal server error"}), 500

    response = jsonify(task.to_dict())
    return response, 201


@tasks.route("/tasks/<int:task_id>", methods=["DELETE"])
def delete_task(task_id):
    task = Task.query.filter_by(id=task_id).first()
    if not task:
        return jsonify({"message": "task not found"}), 400

    try:
        db.session.delete(task)
        db.session.commit()
    except Exception as e:
        logger.error(e)
        db.session.rollback()
        return jsonify({"message": "Internal server error"}), 500

    return jsonify({"message": "Internal server error"}), 201
