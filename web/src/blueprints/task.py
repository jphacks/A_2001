import logging
from flask import jsonify, Blueprint,request
from ..models import Task
from ..database import db

task = Blueprint('task', __name__)
logger = logging.getLogger('app')


@task.route("/tasks",method=["GET"])
def get_task():
    quest_id = 1
    tasks = Task.query.filter(Task.quest_id == quest_id).all()
    return jsonify({"tasks":[task.to_dict() for task in tasks]})

@task.route("/tasks",method=["POST"])
def post_task():
    quest_id = 1
    try:
        payload = request.json
        content = payload.get("content")
        if content is None:
            raise ValueError("content or category is None")
    except Exception as e:
        logger.error(e)
        return jsonify({"message": "Bad request error"}), 400

    try:
        task = Task(quest_id, content)
        db.session.add(task)
        db.session.commit()
    except Exception as e:
        logger.error(e)
        db.session.rollback()
        return jsonify({"message": "Internal server error"}), 500

    response = jsonify(task.to_dict())
    return response, 201

@task.route("/tasks",method=["DELETE"])
def delete_task(task_id):
    task = Task.query.filter_by(id = task_id).first()
    if not task:
        return jsonify ({'message': 'task not found'}), 400


    try:
        db.session.delete(task)
        db.session.commit()
    except Exception as e:
        logger.error(e)
        db.session.rollback()
        return jsonify({"message": "Internal server error"}), 500


    response = jsonify(task.to_dict())
    return response, 201