from app.db import SessionLocal
from app.users.repository import EmployeeRepository


class EmployeeService:

    @staticmethod
    def create_employee(first_name: str, last_name: str, contact: str, user_id: str = None):
        try:
            with SessionLocal() as db:
                employee_repository = EmployeeRepository(db)
                return employee_repository.create_employee(first_name=first_name, last_name=last_name, contact=contact,
                                                           user_id=user_id)
        except Exception as e:
            return e

    @staticmethod
    def read_all_employees():
        try:
            with SessionLocal() as db:
                employees_repository = EmployeeRepository(db)
                return employees_repository.read_all_employees()
        except Exception as e:
            raise e

    @staticmethod
    def read_employee_by_id(employee_id: str):
        try:
            with SessionLocal() as db:
                employee_repository = EmployeeRepository(db)
                return employee_repository.read_employee_by_id(employee_id=employee_id)
        except Exception as e:
            raise e

    @staticmethod
    def read_employee_by_name(first_name: str):
        try:
            with SessionLocal() as db:
                employee_repository = EmployeeRepository(db)
                return employee_repository.read_employee_by_name(first_name=first_name)
        except Exception as e:
            raise e

    @staticmethod
    def update_employee_by_id(employee_id, first_name: str = None, last_name: str = None, contact: str = None,
                              user_id: str = None):
        try:
            with SessionLocal() as db:
                employee_repository = EmployeeRepository(db)
                return employee_repository.update_employee_by_id(employee_id=employee_id, first_name=first_name,
                                                                 last_name=last_name,
                                                                 contact=contact, user_id=user_id)
        except Exception as e:
            raise e

    @staticmethod
    def delete_employee_by_id(employee_id):
        try:
            with SessionLocal() as db:
                employee_repository = EmployeeRepository(db)
                return employee_repository.delete_employee_by_id(employee_id=employee_id)
        except Exception as e:
            raise e

