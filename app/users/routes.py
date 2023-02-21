from fastapi import APIRouter, Depends
from app.users.controller import UserController, EmployeeController, EmploymentContractController
from app.users.schemas import *
from app.users.controller.user_auth_controller import JWTBearer

user_router = APIRouter(tags=["User"], prefix="/api/users")


@user_router.post("/create-new-user", response_model=UserSchema)
def create_user(user: UserSchemaIN):
    """
    - Method that activates user based on the user id provided.
    - **user_name**: mandatory field
    - **email**: mandatory field
    - **password**: mandatory field
    - **is_admin**: default value False (it can only be changed using another route)
    - **is_active**: default value True (it can only be changed using another route)
    """
    return UserController.create_user(user_name=user.user_name, email=user.email, password=user.password)


@user_router.post("/create-new-admin-user", response_model=UserSchema, dependencies=[Depends(JWTBearer("super_user"))])
def create_admin_user(user: UserSchemaIN):
    """
    - Method that activates user based on the user id provided.
    - **user_name**: mandatory field
    - **email**: mandatory field
    - **password**: mandatory field
    - **is_admin**: default value True (it can only be changed using another route)
    - **is_active**: default value True (it can only be changed using another route)
    """
    return UserController.create_admin_user(user_name=user.user_name, email=user.email, password=user.password)


@user_router.get("/get-all-users", response_model=list[UserSchema])
def get_all_users():
    """Method that returns all users in the database."""
    return UserController.get_all_users()


@user_router.get("/get-user-by-id", response_model=UserSchema)
def get_user_by_id(user_id: str):
    """
    - Method that selects user from the database based on user id.
    - **user_id**: mandatory field
    """
    return UserController.get_user_by_id(user_id=user_id)


@user_router.get("/get-user-by-user-name", response_model=UserSchema)
def get_user_by_name(user_name: str):
    """Method that selects user based on username (unique fields)."""
    return UserController.get_user_by_name(user_name=user_name)


@user_router.put("/update-user-data", response_model=UserSchema)
def update_user_by_id(user_id: str, user: UserSchemaUpdate or None):
    """Method that updates existing values in teh database based on user id."""
    return UserController.update_user_by_id(user_id=user_id, user_name=user.user_name, user_email=user.email,
                                            password=user.password)


@user_router.put("/update-user-is-admin", response_model=UserSchema)
def update_user_is_admin(user_name: str):
    """
    - Method that activates user based on the user id provided.
    - **user_name**: mandatory parameter
    - **user_name**: not mandatory
    - **email**: not mandatory
    - **password**: not mandatory
    """
    return UserController.update_user_is_admin(user_name=user_name)


@user_router.delete("/delete-user-by-id")
def delete_user_by_id(user_id: str):
    """
    - Method that deletes user based on user id provided.
    - **user_id**: mandatory parameter
    """
    return UserController.delete_user_by_id(user_id=user_id)


@user_router.put("/deactivate-user-by-id")
def deactivate_user_by_id(user_id: str):
    """
    - Method that deactivates user based on user id provided.
    - **user_id**: mandatory parameter
    """
    return UserController.deactivate_user_by_id(user_id=user_id)


@user_router.put("/activate-user-by-id")
def activate_user_by_id(user_id: str):
    """
    - Method that activates user based on the user id provided.
    - **user_id**: mandatory parameter
    """
    return UserController.activate_user_by_id(user_id=user_id)


@user_router.post("/login")
def login_user(user: UserSchemaLogin):
    """
    - Login method that provides token for authorization.
    - **name**: mandatory parameter
    - **password**: mandatory parameter
    """
    return UserController.login_user(name=user.user_name, password=user.password)


employee_router = APIRouter(tags=["Employee"], prefix="/api/employees")


@employee_router.post("/create-new-employee", response_model=EmployeeSchema)
def create_employee(employee: EmployeeSchemaIN):
    """
    - Method that creates new employee.
    - **first_name**: mandatory field
    - **last_name**: mandatory field
    - **contact**: mandatory field, unique field
    - **user_id**: not mandatory
    - **is_active**: efault value True (it can only be changed using another route)
    """
    return EmployeeController.create_employee(first_name=employee.first_name, last_name=employee.last_name,
                                              contact=employee.contact, user_id=employee.user_id)


@employee_router.get("/get-all-employees", response_model=list[EmployeeSchema])
def get_all_employees():
    """Method that returns all employees from the database."""
    return EmployeeController.get_all_employees()


@employee_router.get("/get-all-employees-containing-text-in-first-name", response_model=list[EmployeeSchema])
def get_all_employees_containing_text_in_first_name(text: str):
    """
    - Method that returns employees whose first name contain input characters.
    - **text**: mandatory parameter
    """
    return EmployeeController.get_all_employees_containing_text_in_first_name(text=text)


@employee_router.get("/get-employee-by-id", response_model=EmployeeSchema)
def get_employee_by_id(employee_id: int):
    """
    - Method that returns employee based on employee id.
    - **employee_id**: mandatory parameter
    """
    return EmployeeController.get_employee_by_id(employee_id=employee_id)


@employee_router.get("/get-employees-by-first-name", response_model=list[EmployeeSchema])
def get_employees_by_name(first_name: str):
    """
    - Method that returns all employees filtered by first name.
    - **first_name**: mandatory parameter
    """
    return EmployeeController.get_employee_by_name(first_name=first_name)


@employee_router.get("/get-employees-by-last-name", response_model=list[EmployeeSchema])
def get_employees_by_last_name(last_name: str):
    """
    - Method that returns all employees filtered by last name.
    - **last_name**: mandatory parameter
    """
    return EmployeeController.get_employee_by_last_name(last_name=last_name)


@employee_router.put("/update-employee-data", response_model=EmployeeSchema)
def update_employee_by_id(employee_id: int, employee: EmployeeSchemaUpdate):
    """
    - Method that updates existing values in the database based on employee id.
    - **first_name**: mandatory field
    - **last_name**: mandatory field
    - **contact**: mandatory field, unique field
    - **user_id**: not mandatory
    - **is_active**: efault value True (it can only be changed using another route)
    """
    return EmployeeController.update_employee_by_id(employee_id=employee_id, first_name=employee.first_name,
                                                    last_name=employee.last_name,
                                                    contact=employee.contact, user_id=employee.user_id)


@employee_router.delete("/delete-employee-by-id")
def delete_employee_by_id(employee_id: int):
    """
    - Method that deletes employee based on employee id.
    - **employee_id**: mandatory parameter
    """
    return EmployeeController.delete_employee_by_id(employee_id)


@employee_router.put("/deactivate-employee-by-id")
def deactivate_employee_by_id(employee_id: int):
    """
    - Method that deactivates employee based on employee id.
    - **employee_id**: mandatory parameter
    """
    return EmployeeController.deactivate_employee(employee_id=employee_id)


@employee_router.put("/deactivate-employee-if-conditions-are-met")
def deactivate_employee_if_conditions_are_met(employee_id: int):
    """
    - Method that deactivates (fires) employee, and returns a list of currently assigned equipment if there is any.
    - **employee_id**: mandatory parameter
    """
    return EmployeeController.deactivate_employee_if_conditions_are_met(employee_id=employee_id)


employment_contract_router = APIRouter(tags=["Employment Contracts"], prefix="/api/employment-contracts")


@employment_contract_router.post("/create-new-contract", response_model=EmploymentContractSchema)
def create_employment_contract(employment_contract: EmploymentContractSchemaIn):
    """
    - Create new employee contract.
    - **start_date**: mandatory field
    - **contract_type**: mandatory field
    - **paycheck**: mandatory field
    - **employee_id**: mandatory field
    - **end_date**: not mandatory
    """
    return EmploymentContractController.create_new_contract(start_date=employment_contract.start_date,
                                                            end_date=employment_contract.end_date,
                                                            contract_type=employment_contract.contract_type,
                                                            paycheck=employment_contract.paycheck,
                                                            employee_id=employment_contract.fk_employee_id)


@employment_contract_router.get("/get-all-contracts", response_model=list[EmploymentContractSchema])
def get_all_employment_contracts():
    """Read all contracts."""
    return EmploymentContractController.read_all_employment_contracts()


@employment_contract_router.get("/get-all-contracts-for-employee-by-employee-id",
                                response_model=list[EmploymentContractSchema])
def get_all_employment_contracts_for_one_employee_by_id(employee_id: int):
    """
    - Read all contracts based on defined employee.
    - **employee_id**: mandatory parameter
    """
    return EmploymentContractController.read_contract_by_employee_id(id_employee=employee_id)


@employment_contract_router.put("/update-active-contract-for-employee-by-employee-id",
                                response_model=EmploymentContractSchema)
def update_employment_contract(employee_id: int, employment_contract: EmploymentContractSchemaUpdate):
    """
    - Method that updates values from the existing contracts. Only active contracts can be updated.
    - **start_date**: mandatory field
    - **contract_type**: mandatory field
    - **paycheck**: mandatory field
    - **employee_id**: mandatory field
    - **end_date**: not mandatory
    """
    return EmploymentContractController.update_employment_contract(employee_id=employee_id,
                                                                   start_date=employment_contract.start_date,
                                                                   end_date=employment_contract.end_date,
                                                                   contract_type=employment_contract.contract_type,
                                                                   paycheck=employment_contract.paycheck)


@employment_contract_router.put("/archive-contract", response_model=EmploymentContractSchema)
def archive_contract(employee_id: int):
    """
    - Method that archives contract.
    - **employee_id**: mandatory parameter
    """
    return EmploymentContractController.archive_contract(employee_id=employee_id)


@employment_contract_router.get("/get-all-contracts-that-are-going-to-expire-in-less-than-15-days",
                                response_model=list[EmploymentContractSchema])
def get_contracts_that_are_going_to_expire_in_15_days():
    """Method that shows contracts that are going to expire in less than 15 days."""
    return EmploymentContractController.read_contracts_that_are_going_to_expire_in_15_days()
