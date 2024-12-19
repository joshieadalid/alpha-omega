from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

# Modelo para las minutas
class Minute(db.Model):
    __tablename__ = 'minutes'
    id = db.Column(db.Integer, primary_key=True)
    timestamp = db.Column(db.String(50), nullable=False)
    text = db.Column(db.Text, nullable=False)

# Servicio para operaciones con minutas
class MinuteService:
    @staticmethod
    def get_all_minutes():
        return Minute.query.all()

    @staticmethod
    def add_minute(timestamp, text):
        new_minute = Minute(timestamp=timestamp, text=text)
        db.session.add(new_minute)
        db.session.commit()
        return new_minute

    @staticmethod
    def get_minute_by_id(minute_id):
        return Minute.query.get(minute_id)

    @staticmethod
    def delete_minute(minute_id):
        minute = Minute.query.get(minute_id)
        if minute:
            db.session.delete(minute)
            db.session.commit()
            return True
        return False
