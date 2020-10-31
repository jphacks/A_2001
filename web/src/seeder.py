import click
from flask.cli import with_appcontext
from .models import User, Quest, QuestShared, Task, Subtask
from .database import db
import string
import random


@click.command("seed")
@click.argument("arg")
@with_appcontext
def seed(arg):
    if arg == "all":
        seed_user()
        seed_quest()
        seed_task()
        seed_subtask()
        seed_quest_shared()

    if arg == "user":
        seed_user()
    if arg == "quest":
        seed_quest()
    if arg == "task":
        seed_task()
    if arg == "subtask":
        seed_subtask()
    if arg == "quest_shared":
        seed_quest_shared()


def commit_all(objects):
    try:
        db.session.add_all(objects)
        db.session.commit()
    except Exception as e:
        print(e)
        db.session.rollback()


def seed_user():
    users = [
        User(
            uuid="".join(
                random.choices(string.ascii_letters + string.digits, k=28),
            ),
            name=f"sample{i}",
        )
        for i in range(10)
    ]
    commit_all(users)


def seed_quest():
    quests = [
        Quest(
            content=f"quest_content{i}",
            category=f"category{i}",
            user_id=i % 10 + 1,
            description=f"quest_description{i}",
        )
        for i in range(20)
    ]
    commit_all(quests)


def seed_task():
    tasks = [
        Task(
            content=f"task_content{i}",
            description=f"task_description{i}",
            quest_id=i % 20 + 1,
        )
        for i in range(40)
    ]
    commit_all(tasks)


def seed_subtask():
    subtasks = [
        Subtask(
            content=f"subtask_content{i}",
            description=f"subtask_description{i}",
            task_id=i % 40 + 1,
        )
        for i in range(100)
    ]
    commit_all(subtasks)


def seed_quest_shared():
    quest_shareds = [
        QuestShared(
            quest_id=i % 20 + 1,
        )
        for i in range(20)
    ]
    commit_all(quest_shareds)


def register_command(app):
    app.cli.add_command(seed)
