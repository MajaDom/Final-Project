from fastapi import APIRouter
from app.users.controller import UserController
from app.users.schemas import UserSchema, UserSchemaIN

user_router = APIRouter(tags=["User"], prefix="/api/users")


@user_router.post("/create-new-user", response_model=UserSchema)
def create_user(user: UserSchemaIN):
    return UserController.create_user(user_name=user.user_name, email=user.email, password=user.password)


@user_router.get("/get-all-users", response_model=list[UserSchema])
def get_all_users():
    return UserController.get_all_users()


@user_router.get("/get-user-by-id", response_model=UserSchema)
def get_user_by_id(user_id: str):
    return UserController.update_user_by_id(user_id=user_id)


@user_router.put("/update-user-data", response_model=UserSchema)
def update_user_by_id(user_id: str, user: UserSchemaIN or None):
    return UserController.update_user_by_id(user_id=user_id, user_name=user.user_name, user_email=user.email,
                                            password=user.password)


@user_router.put("/update-user-is-admin", response_model=UserSchema)
def update_user_is_admin(user_name: str):
    return UserController.update_user_is_admin(user_name=user_name)


@user_router.delete("/delete-user-by-id")
def delete_user_by_id(user_id: str):
    return UserController.delete_user_by_id(user_id)

