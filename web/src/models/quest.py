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
    content = db.Column(db.String(255), nullable=False)
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

    def __init__(self, user_id, content, category):
        self.user_id = user_id
        self.content = content
        self.category = category
