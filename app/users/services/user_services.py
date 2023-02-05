from app.db import SessionLocal
from app.users.repository import UserRepository


class UserServices:

    @staticmethod
    def create_user(user_name: str, email: str, password: str):
        try:
            with SessionLocal() as db:
                user_repository = UserRepository(db)
                return user_repository.create_user(user_name=user_name, email=email, password=password)
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
    def update_user_by_id(user_id, user_name: str = None, user_email: str = None, password: str = None):
        try:
            with SessionLocal() as db:
                user_repository = UserRepository(db)
                return user_repository.update_user_by_id(user_id=user_id, user_name=user_name, user_email=user_email,
                                                         password=password)
        except Exception as e:
            raise e

    @staticmethod
    def update_user_is_admin(user_name):
        try:
            with SessionLocal() as db:
                user_repository = UserRepository(db)
                return user_repository.update_user_is_admin(user_name=user_name)
        except Exception as e:
            raise e

    @staticmethod
    def delete_user_by_id(user_id):
        try:
            with SessionLocal() as db:
                user_repository = UserRepository(db)
                return user_repository.delete_user_by_id(user_id=user_id)
        except Exception as e:
            raise e
