from shared.extensions import db

class User(db.Model):
    __tablename__ = 'users'

    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(
        db.String(150),
        unique=True,
        nullable=False,
        index=True,
        name="uq_username"
    )
    email = db.Column(
        db.String(150),
        unique=True,
        nullable=False,
        name="uq_email"
    )
    password = db.Column(db.String(255), nullable=False)

    def to_dict(self):
        return {"id": self.id, "username": self.username, "email": self.email}
