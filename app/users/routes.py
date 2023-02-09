from fastapi import APIRouter
from app.users.controller import UserController, EmployeeController, EmploymentContractController
from app.users.schemas import *

user_router = APIRouter(tags=["User"], prefix="/api/users")


@user_router.post("/create-new-user", response_model=UserSchema)
def create_user(user: UserSchemaIN):
    return UserController.create_user(user_name=user.user_name, email=user.email, password=user.password)


@user_router.get("/get-all-users", response_model=list[UserSchema])
def get_all_users():
    return UserController.get_all_users()


@user_router.get("/get-user-by-id", response_model=UserSchema)
def get_user_by_id(user_id: str):
    return UserController.get_user_by_id(user_id=user_id)


@user_router.get("/get-user-by-user-name", response_model=UserSchema)
def get_user_by_name(user_name: str):
    return UserController.get_user_by_name(user_name=user_name)


@user_router.put("/update-user-data", response_model=UserSchema)
def update_user_by_id(user_id: str, user: UserSchemaUpdate or None):
    return UserController.update_user_by_id(user_id=user_id, user_name=user.user_name, user_email=user.email,
                                            password=user.password)


@user_router.put("/update-user-is-admin", response_model=UserSchema)
def update_user_is_admin(user_name: str):
    return UserController.update_user_is_admin(user_name=user_name)


@user_router.delete("/delete-user-by-id")
def delete_user_by_id(user_id: str):
    return UserController.delete_user_by_id(user_id)


employee_router = APIRouter(tags=["Employee"], prefix="/api/employees")


@employee_router.post("/create-new-employee", response_model=EmployeeSchema)
def create_employee(employee: EmployeeSchemaIN):
    return EmployeeController.create_employee(first_name=employee.first_name, last_name=employee.last_name,
                                              contact=employee.contact, user_id=employee.user_id)


@employee_router.get("/get-all-employees", response_model=list[EmployeeSchema])
def get_all_employees():
    return EmployeeController.get_all_employees()


@employee_router.get("/get-employee-by-id", response_model=EmployeeSchema)
def get_employee_by_id(employee_id: str):
    return EmployeeController.get_employee_by_id(employee_id=employee_id)


@employee_router.get("/get-employee-by-first-name", response_model=EmployeeSchema)
def get_employee_by_name(first_name: str):
    return EmployeeController.get_employee_by_name(first_name=first_name)


@employee_router.put("/update-employee-data", response_model=EmployeeSchema)
def update_employee_by_id(employee_id: str, employee: EmployeeSchemaUpdate):
    return EmployeeController.update_employee_by_id(employee_id=employee_id, first_name=employee.first_name,
                                                    last_name=employee.last_name,
                                                    contact=employee.contact, user_id=employee.user_id)


@employee_router.delete("/delete-employee-by-id")
def delete_employee_by_id(employee_id: str):
    return EmployeeController.delete_employee_by_id(employee_id)


employment_contract_router = APIRouter(tags=["Employment Contracts"], prefix="/api/employment-contracts")


@employment_contract_router.post("/create-new-contract", response_model=EmploymentContractSchema)
def create_employment_contract(employment_contract: EmploymentContractSchemaIn):
    return EmploymentContractController.create_new_contract(start_date=employment_contract.start_date,
                                                            end_date=employment_contract.end_date,
                                                            contract_type=employment_contract.contract_type,
                                                            paycheck=employment_contract.paycheck,
                                                            employee_id=employment_contract.fk_employee_id)


@employment_contract_router.get("/get-all-contracts", response_model=list[EmploymentContractSchema])
def get_all_employment_contracts():
    return EmploymentContractController.read_all_employment_contracts()


@employment_contract_router.get("/get-all-contracts-for-employee-by-employee-id",
                                response_model=list[EmploymentContractSchema])
def get_all_employment_contracts_for_one_employee_by_id(employee_id: int):
    return EmploymentContractController.read_contract_by_employee_id(id_employee=employee_id)


@employment_contract_router.put("/update-active-contract-for-employee-by-employee-id",
                                response_model=EmploymentContractSchema)
def update_employment_contract(employee_id: int, employment_contract: EmploymentContractSchemaUpdate):
    return EmploymentContractController.update_employment_contract(employee_id=employee_id,
                                                                   start_date=employment_contract.start_date,
                                                                   end_date=employment_contract.end_date,
                                                                   contract_type=employment_contract.contract_type,
                                                                   paycheck=employment_contract.paycheck)


@employment_contract_router.put("/archive-contract", response_model=EmploymentContractSchema)
def archive_contract(employee_id: int):
    return EmploymentContractController.archive_contract(employee_id=employee_id)