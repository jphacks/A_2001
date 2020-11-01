from flask import jsonify, Blueprint, request
from flask_jwt_extended import get_jwt_identity, jwt_required
from ..models import User
from ..database import db
import logging

user = Blueprint("user", __name__)
logger = logging.getLogger("app")


@user.route("/users", methods=["PATCH"])
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


@user.route("/users/test")
def index():
    logger.warn("warn")
    logger.error("error")
    logger.critical("critical")
    return jsonify({"message": "api_test"})
