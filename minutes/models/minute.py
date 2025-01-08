from shared.extensions import db

class Minute(db.Model):
    """
    Modelo para representar la tabla 'minutes' en la base de datos.
    """
    __tablename__ = 'minutes'

    id = db.Column(db.Integer, primary_key=True)
    timestamp = db.Column(db.DateTime, nullable=False)
    text = db.Column(db.Text, nullable=False)

    def to_dict(self):
        return {
            "id": self.id,
            "timestamp": self.timestamp.isoformat(),
            "text": self.text,
        }
