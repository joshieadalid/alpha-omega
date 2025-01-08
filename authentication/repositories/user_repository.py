from authentication.models.user import User
from shared.extensions import db


class UserRepository:
    """
    Repositorio para manejar operaciones de la base de datos relacionadas con 'User'.
    """

    @staticmethod
    def get_by_id(user_id: int):
        """
        Obtiene un usuario por su ID.
        """
        return User.query.get(user_id)

    @staticmethod
    def get_by_username(username: str):
        """Obtiene un usuario por su username."""
        return User.query.filter_by(username=username).first()

    @staticmethod
    def add(username: str, email: str, password: str):
        """Agrega un nuevo usuario."""
        try:
            user = User(username=username, email=email, password=password)
            db.session.add(user)
            db.session.commit()
            return user
        except Exception as e:
            db.session.rollback()
            raise ValueError(f"Error al agregar usuario: {e}")

    @staticmethod
    def delete(user: User):
        """
        Elimina un usuario de la base de datos.
        """
        try:
            db.session.delete(user)
            db.session.commit()
        except Exception as e:
            db.session.rollback()
            print(f"Error al eliminar el usuario: {e}")

    @staticmethod
    def get_by_email(email: str):
        """Obtiene un usuario por su email."""
        return User.query.filter_by(email=email).first()
