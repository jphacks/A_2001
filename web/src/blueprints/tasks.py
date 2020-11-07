import logging
import datetime
from flask import jsonify, Blueprint, request
from flask_jwt_extended import get_jwt_identity, jwt_required
from ..models import Quest, QuestExp, Task
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
        name = payload.get("name")
        description = payload.get("description")
        if name is None:
            raise ValueError("name is None")
    except Exception:
        return jsonify({"message": "Bad request error"}), 400

    try:
        task = Task(quest_id, name, description)
        db.session.add(task)
        db.session.commit()
    except Exception as e:
        logger.error(e)
        db.session.rollback()
        return jsonify({"message": "Internal server error"}), 500

    response = jsonify(task.to_dict())
    return response, 201


@tasks.route("/tasks/<int:task_id>", methods=["DELETE"])
@jwt_required
def delete_task(quest_id, task_id):
    user_id = get_jwt_identity()

    try:
        find_quest(user_id, quest_id)
    except ValueError as ve:
        return jsonify({"message": str(ve)}), 404
    except Exception as e:
        logger.error(e)
        return jsonify({"message": "Internal server error"}), 500

    task = Task.query.filter(
        Task.id == task_id,
        Task.quest_id == quest_id,
    ).first()

    if task is None:
        return jsonify({"message": "Task not found"}), 400

    try:
        db.session.delete(task)
        db.session.commit()
    except Exception as e:
        logger.error(e)
        db.session.rollback()
        return jsonify({"message": "Internal server error"}), 500

    return jsonify({}), 204


@tasks.route("/tasks/<int:task_id>", methods=["PATCH"])
@jwt_required
def edit_task(quest_id, task_id):
    user_id = get_jwt_identity()

    try:
        find_quest(user_id, quest_id)
    except ValueError as ve:
        return jsonify({"message": str(ve)}), 404
    except Exception as e:
        logger.error(e)
        return jsonify({"message": "Internal server error"}), 500

    try:
        task = Task.query.filter(
            Task.id == task_id,
            Task.quest_id == quest_id,
        ).first()
        if task is None:
            return jsonify({"message": "Task not found"}), 404

        # パラメータのバリデーション
        if request.json is None:
            return jsonify({"message": "Bad request error"}), 400

        payload = request.json
        name = payload.get("name")
        description = payload.get("description")
        if name is None and description is None:
            return jsonify({"message": "Bad request error"}), 400

        # タスクを更新する
        if name is not None:
            task.name = name
        if description is not None:
            task.description = description

        db.session.commit()
    except Exception as e:
        logger.error(e)
        db.session.rollback()
        return jsonify({"message": "Internal server error"}), 500

    return jsonify(task.to_dict()), 200


@tasks.route("/tasks/<int:task_id>/done", methods=["PUT", "DELETE"])
@jwt_required
def toggle_task(quest_id, task_id):
    user_id = get_jwt_identity()

    try:
        find_quest(user_id, quest_id)
    except ValueError as ve:
        return jsonify({"message": str(ve)}), 404
    except Exception as e:
        logger.error(e)
        return jsonify({"message": "Internal server error"}), 500

    try:
        task = Task.query.filter(
            Task.id == task_id,
            Task.quest_id == quest_id,
        ).first()
        if task is None:
            return jsonify({"message": "Task not found"}), 404

        task.done = request.method == "PUT"  # PUTならTrue, それ以外はFalse

        db.session.commit()
    except Exception as e:
        logger.error(e)
        db.session.rollback()
        return jsonify({"message": "Internal server error"}), 500

    return jsonify({}), 204


@tasks.route("/tasks/<int:task_id>/time", methods=["PUT"])
@jwt_required
def measure_task(quest_id, task_id):
    user_id = get_jwt_identity()

    try:
        find_quest(user_id, quest_id)
    except ValueError as ve:
        return jsonify({"message": str(ve)}), 404
    except Exception as e:
        logger.error(e)
        return jsonify({"message": "Internal server error"}), 500

    try:
        task = Task.query.filter(
            Task.id == task_id,
            Task.quest_id == quest_id,
        ).first()
        if task is None:
            return jsonify({"message": "Task not found"}), 404

        is_start = task.start is None
        if is_start:
            task.start = datetime.datetime.now()
        else:
            start_time = task.start
            now = datetime.datetime.now()
            diff = (now - start_time).total_seconds() // 60
            task.quest.exp += diff
            task.start = None

            quest_exp = QuestExp.query.filter(
                QuestExp.quest_id == quest_id, QuestExp.date == now.date()
            ).first()
            if quest_exp is None:
                quest_exp = QuestExp(quest_id, diff, now.date())
                db.session.add(quest_exp)
            else:
                quest_exp.exp += diff
        db.session.commit()
    except Exception as e:
        logger.error(e)
        db.session.rollback()
        return jsonify({"message": "Internal server error"}), 500

    if is_start:
        return jsonify({}), 204
    else:
        return jsonify({"time": diff}), 200
