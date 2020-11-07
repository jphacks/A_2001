from app.database import db
from sqlalchemy.dialects.mysql import INTEGER


class User(db.Model):
    __tablename__ = "users"
    id = db.Column(
        INTEGER(unsigned=True),
        primary_key=True,
        autoincrement=True,
    )
    uuid = db.Column(db.String(28), nullable=False)
    name = db.Column(db.String(255), nullable=False)
    level = db.Column(INTEGER(unsigned=True), default=0)
    title = db.Column(db.Text, nullable=False)
    done_cnt = db.Column(INTEGER(unsigned=True), default=0)
    created_at = db.Column(
        db.DateTime,
        server_default=db.func.current_timestamp(),
        server_onupdate=db.func.current_timestamp(),
        nullable=False,
    )
    updated_at = db.Column(
        db.DateTime,
        server_default=db.func.current_timestamp(),
        server_onupdate=db.func.current_timestamp(),
        nullable=False,
    )
    quests = db.relationship("Quest", backref="user", cascade="all")

    def __init__(self, uuid, name):
        self.uuid = uuid
        self.name = name
        self.title = ""

    def to_dict(self):
        return dict(
            name=self.name,
            title=self.title,
        )
