from authentication.repositories.user_repository import UserRepository
from werkzeug.security import generate_password_hash, check_password_hash


class UserService:
    """
    Servicio para manejar la lógica de negocio relacionada con usuarios.
    """

    def __init__(self, repository: UserRepository):
        self.repository = repository

    def get_user_by_id(self, user_id: int):
        """
        Obtiene un usuario por su ID.
        """
        return self.repository.get_by_id(user_id)

    def get_user_by_username(self, username: str):
        """
        Obtiene un usuario por su nombre de usuario.
        """
        return self.repository.get_by_username(username)

    def add_user(self, username: str, email: str, password: str):
        """Registra un nuevo usuario verificando duplicados."""
        if self.repository.get_by_email(email):
            raise ValueError("El correo electrónico ya está registrado.")
        if self.repository.get_by_username(username):
            raise ValueError("El nombre de usuario ya está registrado.")

        hashed_password = generate_password_hash(password)
        return self.repository.add(username, email, hashed_password)


    def authenticate_user(self, email: str, password: str):
        """Autentica al usuario por email."""
        user = self.repository.get_by_email(email)
        if not user or not check_password_hash(user.password, password):
            return None
        return user

    def delete_user(self, user_id: int):
        """
        Elimina un usuario por su ID.
        """
        user = self.repository.get_by_id(user_id)
        if not user:
            raise ValueError("Usuario no encontrado.")
        self.repository.delete(user)
