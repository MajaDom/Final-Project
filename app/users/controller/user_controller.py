from app.users.services import UserServices
from fastapi import HTTPException, Response
from app.users.exceptions import *


class UserController:

    @staticmethod
    def create_user(user_name: str, email: str, password: str):
        try:
            user = UserServices.create_user(user_name=user_name, email=email, password=password)
            return user
        except UserMissingDataException as e:
            raise HTTPException(status_code=e.code, detail=e.message)
        except Exception as e:
            raise HTTPException(status_code=500, detail=f"Unprocessed error: {str(e)}")

    @staticmethod
    def get_all_users():
        try:
            users = UserServices.read_all_users()
            return users
        except Exception as e:
            raise HTTPException(status_code=500, detail=f"Unprocessed error: {str(e)}")

    @staticmethod
    def get_user_by_id(user_id: str):
        try:
            user = UserServices.read_user_by_id(user_id=user_id)
            return user
        except UserNotFoundException as e:
            raise HTTPException(status_code=e.code, detail=e.message)
        except Exception as e:
            raise HTTPException(status_code=500, detail=f"Unprocessed error: {str(e)}")

    @staticmethod
    def get_user_by_name(user_name: str):
        try:
            user = UserServices.read_user_by_name(user_name=user_name)
            return user
        except UserNotFoundException as e:
            raise HTTPException(status_code=e.code, detail=e.message)
        except Exception as e:
            raise HTTPException(status_code=500, detail=f"Unprocessed error: {str(e)}")

    @staticmethod
    def update_user_by_id(user_id, user_name: str = None, user_email: str = None, password: str = None):
        try:
            user = UserServices.update_user_by_id(user_id=user_id, user_name=user_name, user_email=user_email,
                                                  password=password)
            return user
        except UserNotFoundException as e:
            raise HTTPException(status_code=e.code, detail=e.message)
        except Exception as e:
            raise HTTPException(status_code=500, detail=f"Unprocessed error: {str(e)}")

    @staticmethod
    def update_user_is_admin(user_name):
        try:
            user = UserServices.update_user_is_admin(user_name=user_name)
            return user
        except UserNotFoundException as e:
            raise HTTPException(status_code=e.code, detail=e.message)
        except Exception as e:
            raise HTTPException(status_code=500, detail=f"Unprocessed error: {str(e)}")

    @staticmethod
    def delete_user_by_id(user_id):
        try:
            UserServices.delete_user_by_id(user_id=user_id)
            return Response(status_code=200, content=f"User with id {user_id} successfully deleted.")
        except UserNotFoundException as e:
            raise HTTPException(status_code=e.code, detail=e.message)
        except Exception as e:
            raise HTTPException(status_code=500, detail=f"Unprocessed error: {str(e)}")
