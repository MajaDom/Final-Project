import hashlib

from app.db import SessionLocal
from app.users.exceptions import UserInvalidPassword
from app.users.repository import UserRepository


class UserServices:

    @staticmethod
    def create_user(user_name: str, email: str, password: str, is_admin: bool = False):
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
        try:
            with SessionLocal() as db:
                users_repository = UserRepository(db)
                return users_repository.read_all_users()
        except Exception as e:
            raise e

    @staticmethod
    def read_user_by_id(user_id: str):
        try:
            with SessionLocal() as db:
                user_repository = UserRepository(db)
                return user_repository.read_user_by_id(user_id=user_id)
        except Exception as e:
            raise e

    @staticmethod
    def read_user_by_name(user_name: str):
        try:
            with SessionLocal() as db:
                user_repository = UserRepository(db)
                return user_repository.read_user_by_name(user_name=user_name)
        except Exception as e:
            raise e

    @staticmethod
    def update_user_by_id(user_id: str, user_name: str = None, user_email: str = None, password: str = None):
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
        try:
            with SessionLocal() as db:
                user_repository = UserRepository(db)
                return user_repository.update_user_is_admin(user_name=user_name)
        except Exception as e:
            raise e

    @staticmethod
    def delete_user_by_id(user_id: str):
        try:
            with SessionLocal() as db:
                user_repository = UserRepository(db)
                return user_repository.delete_user_by_id(user_id=user_id)
        except Exception as e:
            raise e

    @staticmethod
    def deactivate_user_by_id(user_id: str):
        try:
            with SessionLocal() as db:
                user_repository = UserRepository(db)
                return user_repository.deactivate_user(user_id=user_id)
        except Exception as e:
            raise e

    @staticmethod
    def activate_user_by_id(user_id: str):
        try:
            with SessionLocal() as db:
                user_repository = UserRepository(db)
                return user_repository.activate_user(user_id=user_id)
        except Exception as e:
            raise e

    @staticmethod
    def login_user(name: str, password: str):
        with SessionLocal() as db:
            try:
                user_repository = UserRepository(db)
                user = user_repository.read_user_by_name(user_name=name)
                if hashlib.sha256(bytes(password, "utf-8")).hexdigest() != user.password:
                    raise UserInvalidPassword(message="Invalid password for user", code=401)
                return user
            except Exception as e:
                raise e
