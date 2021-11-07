import flask_sqlalchemy

db = flask_sqlalchemy.SQLAlchemy()


# schema for the Messages table (as instructed)
class Message(db.Model):
    __tablename__ = 'messages'
    _id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    is_modified = db.Column(db.Boolean, default=False)
    status = db.Column(db.Integer)
    data = db.Column(db.String)
    timestamp = db.Column(db.Integer)

    @property
    def id(self):
        return self._id
