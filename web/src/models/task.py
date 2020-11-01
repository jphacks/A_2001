from app.database import db
from sqlalchemy.dialects.mysql import INTEGER


class Task(db.Model):
    __tablename__ = "tasks"
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
    content = db.Column(db.String(255), nullable=False)
    description = db.Column(db.String(5000))
    start = db.Column(db.DateTime)
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
    subtasks = db.relationship("Subtask", backref="task", cascade="all")

    def __init__(self, quest_id, content, description=None):
        self.quest_id = quest_id
        self.content = content
        self.description = description

    def to_dict(self):
        return dict(
            id=self.id,
            content=self.content,
            description="" if self.description is None else self.description,
            subtasks=[subtask.to_dict() for subtask in self.subtasks],
        )
