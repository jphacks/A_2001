from app.database import db
from sqlalchemy.dialects.mysql import INTEGER


class Quest(db.Model):
    __tablename__ = "quests"
    id = db.Column(
        INTEGER(unsigned=True),
        primary_key=True,
        autoincrement=True,
    )
    user_id = db.Column(
        INTEGER(unsigned=True),
        db.ForeignKey("users.id", ondelete="cascade", onupdate="cascade"),
        nullable=False,
    )
    name = db.Column(db.String(255), nullable=False)
    category = db.Column(db.String(255), nullable=False)
    description = db.Column(db.String(5000))
    exp = db.Column(INTEGER(unsigned=True), default=0)
    done = db.Column(db.Boolean, default=False)
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
    quests_shared = db.relationship("QuestShared", backref="quest", cascade="all")
    quests_exp = db.relationship("QuestExp", backref="quest", cascade="all")
    tasks = db.relationship("Task", backref="quest", cascade="all")

    def __init__(self, user_id, name, category, description=None):
        self.user_id = user_id
        self.name = name
        self.category = category
        self.description = description

    def to_dict(self):
        return dict(
            id=self.id,
            name=self.name,
            category=self.category,
            description="" if self.description is None else self.description,
        )
