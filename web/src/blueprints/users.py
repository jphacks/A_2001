import logging
from flask import Blueprint, jsonify, request
from flask_jwt_extended import get_jwt_identity, jwt_required
from ..models import Quest, User
from ..database import db

users = Blueprint("users", __name__)
logger = logging.getLogger("app")


@users.route("/users", methods=["GET"])
@jwt_required
def user_exp():
    user_id = get_jwt_identity()
    try:
        user_data = User.query.filter(User.id == user_id).first()
        if user_data is None:
            return jsonify({"message": "User data not found"}), 401

        level = user_data.level
        title = user_data.title
        quests = Quest.query.filter(Quest.user_id == user_id).all()

        d = {que.id: {"exp": que.exp, "name": que.name} for que in quests}

    except Exception as e:
        logger.error(e)
        return jsonify({"message": "Internal server error"}), 500

    return jsonify({"exps": d, "level": level, "title": title})


@users.route("/users", methods=["PATCH"])
@jwt_required
def edit_user():
    user_id = get_jwt_identity()

    try:
        payload = request.json
        name = payload.get("name")
        if name is None:
            raise ValueError("name is None")
    except Exception:
        return jsonify({"message": "Bad request error"}), 400

    user = User.query.filter(User.id == user_id).first()
    if user is None:
        return jsonify({"message": "Authorization failed"}), 401

    try:
        user.name = name
        db.session.commit()
    except Exception as e:
        logger.error(e)
        db.session.rollback()
        return jsonify({"message": "Internal server error"}), 500

    return jsonify(user.to_dict()), 200


@users.route("/users/test")
def index():
    logger.warn("warn")
    logger.error("error")
    logger.critical("critical")
    return jsonify({"message": "api_test"})
