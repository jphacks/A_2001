from app.database import db
from sqlalchemy.dialects.mysql import INTEGER


class Subtask(db.Model):
    __tablename__ = "subtasks"
    id = db.Column(
        INTEGER(unsigned=True),
        primary_key=True,
        autoincrement=True,
    )
    task_id = db.Column(
        INTEGER(unsigned=True),
        db.ForeignKey("tasks.id", ondelete="cascade", onupdate="cascade"),
        nullable=False,
    )
    content = db.Column(db.String(255), nullable=False)
    description = db.Column(db.String(5000))
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

    def __init__(self, task_id, content, description=None):
        self.task_id = task_id
        self.content = content
        self.description = description

    def to_dict(self):
        return dict(
            id=self.id,
            content=self.content,
        )
