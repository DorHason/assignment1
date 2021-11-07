from sqlalchemy.sql.expression import func

from models import db, Message


def get_random_messages(entries):
    return db.session.query(Message).filter(Message.is_modified == False).order_by(func.random()).limit(entries).all()


def get_modified_messages():
    return db.session.query(Message).filter(Message.is_modified).with_entities(Message.id).all()
