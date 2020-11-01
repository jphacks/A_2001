from flask import jsonify, Blueprint, request
import logging
from flask_jwt_extended import (
    jwt_required,
    jwt_refresh_token_required,
    get_jwt_identity,
    create_access_token,
    create_refresh_token,
)
import os
import firebase_admin
from firebase_admin import auth as firebase_auth
from firebase_admin import credentials
from ..models import User
from ..database import db

auth = Blueprint("auth", __name__)
logger = logging.getLogger("app")
cred = credentials.Certificate(os.environ["SECRET_KEY"])
firebase_app = firebase_admin.initialize_app(cred)


@auth.route("/auth", methods=["GET"])
def authentification():
    firebase_token = request.args.get("token", type=str)
    if firebase_token is None:
        return jsonify({"message": "Parameter is invalid"}), 400
    try:
        result = firebase_auth.verify_id_token(firebase_token, firebase_app)
        logger.warn(result)
    except Exception:
        return jsonify({"message": "Token is invalid"}), 401

    uid = result["uid"]
    name = result["name"]

    user = db.session.query(User).filter_by(uuid=uid).first()
    # 新規登録
    if not user:
        try:
            user = User(uid, name)
            db.session.add(user)
            db.session.commit()
        except Exception as e:
            logger.warn(e)
            db.session.rollback()
            return jsonify({"message": "Internal server error"}), 500

    access_token = create_access_token(identity=user.id)
    refresh_token = create_refresh_token(identity=user.id)
    return (
        jsonify(
            {
                "access_token": access_token,
                "refresh_token": refresh_token,
            }
        ),
        200,
    )


@auth.route("/auth/refresh", methods=["POST"])
@jwt_refresh_token_required
def refresh():
    current_user = get_jwt_identity()
    ret = {"access_token": create_access_token(identity=current_user)}
    return jsonify(ret), 200


@auth.route("/protected")
@jwt_required
def index():
    logger.warn("warn")
    logger.error("error")
    logger.critical("critical")
    return jsonify({"message": "auth_test"})
