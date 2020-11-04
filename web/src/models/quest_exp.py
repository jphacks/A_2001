from app.database import db
from sqlalchemy.dialects.mysql import INTEGER


class QuestExp(db.Model):
    __tablename__ = "quests_exp"
    id = db.Column(
        INTEGER(unsigned=True),
        primary_key=True,
        autoincrement=True,
    )
    quest_id = db.Column(
        INTEGER(unsigned=True),
        db.ForeignKey("quests.id", ondelete="cascade", onupdate="cascade"),
        nullable=False,
    )
    exp = db.Column(INTEGER(unsigned=True), default=0)
    date = db.Column(db.Date)
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

    def __init__(self, quest_id, exp, date):
        self.quest_id = quest_id
        self.exp = exp
        self.date = date
