import logging
from flask import Blueprint, jsonify, request
from flask_jwt_extended import get_jwt_identity, jwt_required
from ..models import Quest, Task, Subtask
from ..database import db

subtasks = Blueprint("subtasks", __name__)
logger = logging.getLogger("app")


def find_quest_task(user_id, quest_id, task_id):
    try:
        quest = Quest.query.filter(
            Quest.user_id == user_id,
            Quest.id == quest_id,
        ).first()
        if quest is None:
            raise ValueError("Quest not found")

        task = Task.query.filter(
            Task.quest_id == quest_id,
            Task.id == task_id,
        ).first()
        if task is None:
            raise ValueError("Task not found")
    except ValueError as ve:
        raise ve
    except Exception as e:
        logger.error(e)
        raise Exception("Internal server error")


@subtasks.route("/subtasks", methods=["POST"])
@jwt_required
def post_subtask(quest_id, task_id):
    user_id = get_jwt_identity()

    try:
        find_quest_task(user_id, quest_id, task_id)
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
        subtask = Subtask(task_id, content, description)
        db.session.add(subtask)
        db.session.commit()
    except Exception as e:
        logger.error(e)
        db.session.rollback()
        return jsonify({"message": "Internal server error"}), 500

    response = jsonify(subtask.to_dict())
    return response, 201


@subtasks.route("/subtasks/<int:subtask_id>", methods=["DELETE"])
@jwt_required
def delete_subtask(quest_id, task_id, subtask_id):
    user_id = get_jwt_identity()

    try:
        find_quest_task(user_id, quest_id, task_id)
    except ValueError as ve:
        return jsonify({"message": str(ve)}), 404
    except Exception as e:
        logger.error(e)
        return jsonify({"message": "Internal server error"}), 500

    try:
        subtask = Subtask.query.filter(
            Subtask.id == subtask_id, Subtask.task_id == task_id
        ).first()
        if subtask is None:
            return jsonify({"message": "Subtask not found"}), 404

        db.session.delete(subtask)
        db.session.commit()
    except Exception as e:
        logger.error(e)
        db.session.rollback()
        return jsonify({"message": "Internal server error"}), 500

    return jsonify({}), 204
