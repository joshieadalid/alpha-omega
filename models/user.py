# models/user.py
from injector import inject
from services.database_manager import db_manager

@inject
class User(db_manager.Model):
    __tablename__ = 'users'
    id = db_manager.Column(db_manager.Integer, primary_key=True)
    username = db_manager.Column(db_manager.String(150), unique=True, nullable=False)
    password = db_manager.Column(db_manager.String(255), nullable=False)

    def to_dict(self):
        return {"id": self.id, "username": self.username}
