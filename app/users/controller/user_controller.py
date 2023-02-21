from fastapi import HTTPException, Response
from app.users.services import UserServices, sign_jwt
from app.users.exceptions import *


class UserController:

    @staticmethod
    def create_user(user_name: str, email: str, password: str, is_admin: bool = False):
        """Method that creates new user."""
        try:
            user = UserServices.create_user(user_name=user_name, email=email, password=password, is_admin=is_admin)
            return user
        except UserMissingDataException as e:
            raise HTTPException(status_code=e.code, detail=e.message)
        except Exception as e:
            raise HTTPException(status_code=500, detail=f"Unprocessed error: {str(e)}")

    @staticmethod
    def create_admin_user(user_name: str, email: str, password: str, is_admin: bool = True):
        """Method that creates new admin user."""
        try:
            user = UserServices.create_admin_user(user_name=user_name, email=email, password=password, is_admin=is_admin)
            return user
        except UserMissingDataException as e:
            raise HTTPException(status_code=e.code, detail=e.message)
        except Exception as e:
            raise HTTPException(status_code=500, detail=f"Unprocessed error: {str(e)}")

    @staticmethod
    def get_all_users():
        """Method that returns all users in the database."""
        try:
            users = UserServices.read_all_users()
            return users
        except Exception as e:
            raise HTTPException(status_code=500, detail=f"Unprocessed error: {str(e)}")

    @staticmethod
    def get_user_by_id(user_id: str):
        """Method that selects user from the database based on user id."""
        try:
            user = UserServices.read_user_by_id(user_id=user_id)
            return user
        except UserNotFoundException as e:
            raise HTTPException(status_code=e.code, detail=e.message)
        except Exception as e:
            raise HTTPException(status_code=500, detail=f"Unprocessed error: {str(e)}")

    @staticmethod
    def get_user_by_name(user_name: str):
        """Method that selects user based on username (unique fields)."""
        try:
            user = UserServices.read_user_by_name(user_name=user_name)
            return user
        except UserNotFoundException as e:
            raise HTTPException(status_code=e.code, detail=e.message)
        except Exception as e:
            raise HTTPException(status_code=500, detail=f"Unprocessed error: {str(e)}")

    @staticmethod
    def update_user_by_id(user_id: str, user_name: str = None, user_email: str = None, password: str = None):
        """Method that updates existing values in teh database based on user id."""
        try:
            user = UserServices.update_user_by_id(user_id=user_id, user_name=user_name, user_email=user_email,
                                                  password=password)
            return user
        except UserNotFoundException as e:
            raise HTTPException(status_code=e.code, detail=e.message)
        except Exception as e:
            raise HTTPException(status_code=500, detail=f"Unprocessed error: {str(e)}")

    @staticmethod
    def update_user_is_admin(user_name: str):
        """Method that upgrades regular user to admin user."""
        try:
            user = UserServices.update_user_is_admin(user_name=user_name)
            return user
        except UserNotFoundException as e:
            raise HTTPException(status_code=e.code, detail=e.message)
        except Exception as e:
            raise HTTPException(status_code=500, detail=f"Unprocessed error: {str(e)}")

    @staticmethod
    def delete_user_by_id(user_id: str):
        """Method that deletes user based on user id provided."""
        try:
            UserServices.delete_user_by_id(user_id=user_id)
            return Response(status_code=200, content=f"User with id {user_id} successfully deleted.")
        except UserNotFoundException as e:
            raise HTTPException(status_code=e.code, detail=e.message)
        except Exception as e:
            raise HTTPException(status_code=500, detail=f"Unprocessed error: {str(e)}")

    @staticmethod
    def deactivate_user_by_id(user_id: str):
        """Method that deactivates user based on user id provided."""
        try:
            UserServices.deactivate_user_by_id(user_id=user_id)
            return Response(status_code=200, content=f"User with id {user_id} successfully deactivated.")
        except UserNotFoundException as e:
            raise HTTPException(status_code=e.code, detail=e.message)
        except Exception as e:
            raise HTTPException(status_code=500, detail=f"Unprocessed error: {str(e)}")

    @staticmethod
    def activate_user_by_id(user_id: str):
        """Method that activates user based on the user id provided."""
        try:
            UserServices.activate_user_by_id(user_id=user_id)
            return Response(status_code=200, content=f"User with id {user_id} successfully activated.")
        except UserNotFoundException as e:
            raise HTTPException(status_code=e.code, detail=e.message)
        except Exception as e:
            raise HTTPException(status_code=500, detail=f"Unprocessed error: {str(e)}")

    @staticmethod
    def login_user(name: str, password: str):
        """Login method that provides token for authorization."""
        try:
            user = UserServices.login_user(name=name, password=password)
            if user.is_admin:
                return sign_jwt(user.user_id, "super_user")
            return sign_jwt(user.user_id, "classic_user")
        except UserInvalidPassword as e:
            raise HTTPException(status_code=e.code, detail=e.message)
        except Exception as e:
            raise HTTPException(status_code=500, detail=str(e))
