from sqlalchemy.orm import Session
from sqlalchemy.exc import IntegrityError

from app.users.exceptions import UserNotFoundException, UserMissingDataException
from app.users.models import User


class UserRepository:
    def __init__(self, db: Session):
        self.db = db

    def create_user(self, user_name: str, email: str, password: str, is_admin: bool = False) -> User:
        try:
            user = User(user_name=user_name, email=email, password=password, is_admin=is_admin)
            self.db.add(user)
            self.db.commit()
            self.db.refresh(user)
            return user
        except IntegrityError as e:
            raise e
        except Exception as e:
            raise e

    def create_admin_user(self, user_name: str, email: str, password: str, is_admin: bool = True) -> User:
        try:
            user = User(user_name=user_name, email=email, password=password, is_admin=is_admin)
            self.db.add(user)
            self.db.commit()
            self.db.refresh(user)
            return user
        except IntegrityError as e:
            raise e
        except Exception as e:
            raise e

    def read_all_users(self) -> list[User]:
        users = self.db.query(User).all()
        return users

    def read_user_by_id(self, user_id: str) -> User:
        user = self.db.query(User).filter(User.user_id == user_id).first()
        if user is None:
            raise UserNotFoundException(message=f'User with id {user_id} not in the database.', code=400)
        return user

    def read_user_by_name(self, user_name: str) -> User:
        user = self.db.query(User).filter(User.user_name == user_name).first()
        if user is None:
            raise UserNotFoundException(message=f'User with name {user_name} not in the database.', code=400)
        return user

    def update_user_by_id(self, user_id, user_name: str = None, user_email: str = None, password: str = None) -> User:
        user = self.db.query(User).filter(User.user_id == user_id).first()
        if user is None:
            raise UserNotFoundException(message=f'User with id {user_id} not in the database.', code=400)
        if user_name is not None:
            user.user_name = user_name
        if user_email is not None:
            user.email = user_email
        if password is not None:
            user.password = password
        self.db.add(user)
        self.db.commit()
        self.db.refresh(user)
        return user

    def update_user_is_admin(self, user_name: str) -> User:
        user = self.db.query(User).filter(User.user_name == user_name).first()
        if user is None:
            raise UserNotFoundException(message=f'User with name {user_name} not in the database.', code=400)
        user.is_admin = True
        self.db.add(user)
        self.db.commit()
        self.db.refresh(user)
        return user

    def delete_user_by_id(self, user_id: str) -> bool:
        user = self.db.query(User).filter(User.user_id == user_id).first()
        if user is None:
            raise UserNotFoundException(message=f'User with id {user_id} not in the database.', code=400)
        self.db.delete(user)
        self.db.commit()
        return True

    def deactivate_user(self, user_id: str) -> bool:
        user = self.db.query(User).filter(User.user_id == user_id).first()
        if user is None:
            raise UserNotFoundException(message=f'User with id {user_id} not in the database.', code=400)
        user.is_active = False
        self.db.add(user)
        self.db.commit()
        self.db.refresh(user)
        return True

    def activate_user(self, user_id: str) -> bool:
        user = self.db.query(User).filter(User.user_id == user_id).first()
        if user is None:
            raise UserNotFoundException(message=f'User with id {user_id} not in the database.', code=400)
        user.is_active = True
        self.db.add(user)
        self.db.commit()
        self.db.refresh(user)
        return True
