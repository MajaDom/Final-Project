# It contains methods that perform CRUD operations on the database
from app.db import SessionLocal
from app.users.repository import EmployeeRepository


class EmployeeService:

    @staticmethod
    def create_employee(first_name: str, last_name: str, contact: str, user_id: str = None):
        """Method that creates new employee."""
        try:
            with SessionLocal() as db:
                employee_repository = EmployeeRepository(db)
                return employee_repository.create_employee(first_name=first_name, last_name=last_name, contact=contact,
                                                           user_id=user_id)
        except Exception as e:
            raise e

    @staticmethod
    def read_all_employees():
        """Method that returns all employees from the database."""
        try:
            with SessionLocal() as db:
                employees_repository = EmployeeRepository(db)
                return employees_repository.read_all_employees()
        except Exception as e:
            raise e

    @staticmethod
    def read_all_employees_containing_text_in_first_name(text: str):
        """Method that returns employees whose names contain input characters."""
        try:
            with SessionLocal() as db:
                employees_repository = EmployeeRepository(db)
                return employees_repository.read_all_employees_containing_text_in_first_name(text=text)
        except Exception as e:
            raise e

    @staticmethod
    def read_employee_by_id(employee_id: int):
        """Method that returns employee based on employee id."""
        try:
            with SessionLocal() as db:
                employee_repository = EmployeeRepository(db)
                return employee_repository.read_employee_by_id(employee_id=employee_id)
        except Exception as e:
            raise e

    @staticmethod
    def read_employee_by_name(first_name: str):
        """Method that returns all employees filtered by first name."""
        try:
            with SessionLocal() as db:
                employee_repository = EmployeeRepository(db)
                return employee_repository.read_employee_by_name(first_name=first_name)
        except Exception as e:
            raise e

    @staticmethod
    def read_employee_by_last_name(last_name: str):
        """Method that returns all employees filtered by last name."""
        try:
            with SessionLocal() as db:
                employee_repository = EmployeeRepository(db)
                return employee_repository.read_employee_by_last_name(last_name=last_name)
        except Exception as e:
            raise e

    @staticmethod
    def update_employee_by_id(employee_id, first_name: str = None, last_name: str = None, contact: str = None,
                              user_id: str = None):
        """Method that updates existing values in the database based on employee id."""
        try:
            with SessionLocal() as db:
                employee_repository = EmployeeRepository(db)
                return employee_repository.update_employee_by_id(employee_id=employee_id, first_name=first_name,
                                                                 last_name=last_name,
                                                                 contact=contact, user_id=user_id)
        except Exception as e:
            raise e

    @staticmethod
    def delete_employee_by_id(employee_id: int):
        """Method that deletes employee based on employee id."""
        try:
            with SessionLocal() as db:
                employee_repository = EmployeeRepository(db)
                return employee_repository.delete_employee_by_id(employee_id=employee_id)
        except Exception as e:
            raise e

    @staticmethod
    def deactivate_employee(employee_id: int):
        """Method that deactivates employee based on employee id."""
        try:
            with SessionLocal() as db:
                employee_repository = EmployeeRepository(db)
                return employee_repository.deactivate_employee(employee_id=employee_id)
        except Exception as e:
            raise e


