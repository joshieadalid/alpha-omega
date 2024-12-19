from services.db_service import db

class Minute(db.Model):
    __tablename__ = 'minutes'
    id = db.Column(db.Integer, primary_key=True)
    timestamp = db.Column(db.String(50), nullable=False)
    text = db.Column(db.Text, nullable=False)

class MinuteService:
    @staticmethod
    def get_all_minutes():
        return Minute.query.all()

    @staticmethod
    def add_minute(timestamp, text):
        new_minute = Minute(timestamp=timestamp, text=text)
        db.session.add(new_minute)
        db.session.commit()
        print("Minuta registrada")
        return new_minute
