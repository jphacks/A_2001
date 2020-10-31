from flask import jsonify, Blueprint, request
import logging
from flask_jwt_extended import (
    jwt_required,
    create_access_token,
)
import os
import firebase_admin
from firebase_admin import auth as firebase_auth
from firebase_admin import credentials
import datetime
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
    exp = result["exp"]

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

    time_diff = datetime.datetime.fromtimestamp(exp) - datetime.datetime.now()
    access_token = create_access_token(
        identity=user.id,
        expires_delta=time_diff,
    )
    return jsonify({"token": access_token}), 200


@auth.route("/protected")
@jwt_required
def index():
    logger.warn("warn")
    logger.error("error")
    logger.critical("critical")
    return jsonify({"message": "auth_test"})
