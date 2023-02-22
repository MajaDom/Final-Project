# It provides methods for creating, reading, updating, deleting and
# logging in users.
import hashlib
from app.db import SessionLocal
from app.users.exceptions import UserInvalidPassword
from app.users.repository import UserRepository


class UserServices:

    @staticmethod
    def create_user(user_name: str, email: str, password: str, is_admin: bool = False):
        """Method that creates new user."""
        try:
            with SessionLocal() as db:
                user_repository = UserRepository(db)
                hashed_password = hashlib.sha256(bytes(password, "utf-8")).hexdigest()
                return user_repository.create_user(user_name=user_name, email=email, password=hashed_password,
                                                   is_admin=is_admin)
        except Exception as e:
            raise e

    @staticmethod
    def create_admin_user(user_name: str, email: str, password: str, is_admin: bool = True):
        """Method that creates new admin user."""
        try:
            with SessionLocal() as db:
                user_repository = UserRepository(db)
                hashed_password = hashlib.sha256(bytes(password, "utf-8")).hexdigest()
                return user_repository.create_admin_user(user_name=user_name, email=email, password=hashed_password,
                                                         is_admin=is_admin)
        except Exception as e:
            raise e

    @staticmethod
    def read_all_users():
        """Method that returns all users in the database."""
        try:
            with SessionLocal() as db:
                users_repository = UserRepository(db)
                return users_repository.read_all_users()
        except Exception as e:
            raise e

    @staticmethod
    def read_user_by_id(user_id: str):
        """Method that selects user from the database based on user id."""
        try:
            with SessionLocal() as db:
                user_repository = UserRepository(db)
                return user_repository.read_user_by_id(user_id=user_id)
        except Exception as e:
            raise e

    @staticmethod
    def read_user_by_name(user_name: str):
        """Method that selects user based on username (unique fields)."""
        try:
            with SessionLocal() as db:
                user_repository = UserRepository(db)
                return user_repository.read_user_by_name(user_name=user_name)
        except Exception as e:
            raise e

    @staticmethod
    def update_user_by_id(user_id: str, user_name: str = None, user_email: str = None, password: str = None):
        """Method that updates existing values in teh database based on user id."""
        try:
            with SessionLocal() as db:
                user_repository = UserRepository(db)
                hashed_password = hashlib.sha256(bytes(password, "utf-8")).hexdigest()
                return user_repository.update_user_by_id(user_id=user_id, user_name=user_name, user_email=user_email,
                                                         password=hashed_password)
        except Exception as e:
            raise e

    @staticmethod
    def update_user_is_admin(user_name: str):
        """Method that upgrades regular user to admin user."""
        try:
            with SessionLocal() as db:
                user_repository = UserRepository(db)
                return user_repository.update_user_is_admin(user_name=user_name)
        except Exception as e:
            raise e

    @staticmethod
    def delete_user_by_id(user_id: str):
        """Method that deletes user based on user id provided."""
        try:
            with SessionLocal() as db:
                user_repository = UserRepository(db)
                return user_repository.delete_user_by_id(user_id=user_id)
        except Exception as e:
            raise e

    @staticmethod
    def deactivate_user_by_id(user_id: str):
        """Method that deactivates user based on user id provided."""
        try:
            with SessionLocal() as db:
                user_repository = UserRepository(db)
                return user_repository.deactivate_user(user_id=user_id)
        except Exception as e:
            raise e

    @staticmethod
    def activate_user_by_id(user_id: str):
        """Method that activates user based on the user id provided."""
        try:
            with SessionLocal() as db:
                user_repository = UserRepository(db)
                return user_repository.activate_user(user_id=user_id)
        except Exception as e:
            raise e

    @staticmethod
    def login_user(name: str, password: str):
        """Login method that provides token for authorization."""
        with SessionLocal() as db:
            try:
                user_repository = UserRepository(db)
                user = user_repository.read_user_by_name(user_name=name)
                if hashlib.sha256(bytes(password, "utf-8")).hexdigest() != user.password:
                    raise UserInvalidPassword(message="Invalid password for user", code=401)
                return user
            except Exception as e:
                raise e
