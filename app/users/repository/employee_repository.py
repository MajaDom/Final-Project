from sqlalchemy.orm import Session
from sqlalchemy.exc import IntegrityError
from app.users.models import Employee
from app.users.exceptions import EmployeeNotFoundException


class EmployeeRepository:
    def __init__(self, db: Session):
        self.db = db

    def create_employee(self, first_name: str, last_name: str, contact: str, user_id: str = None) -> Employee:
        """Method that creates new employee."""
        try:
            employee = Employee(first_name=first_name, last_name=last_name, contact=contact, user_id=user_id)
            self.db.add(employee)
            self.db.commit()
            self.db.refresh(employee)
            return employee
        except IntegrityError as e:
            raise e
        except Exception as e:
            raise e

    def read_all_employees(self) -> list[Employee]:
        """Method that returns all employees from the database."""
        employees = self.db.query(Employee).all()
        return employees

    def read_all_employees_containing_text_in_first_name(self, text: str) -> list[Employee]:
        """Method that returns employees whose names contain input characters."""
        employees = self.db.query(Employee).filter(Employee.first_name.like(f"%{text}%")).all()
        return employees

    def read_employee_by_id(self, employee_id: int) -> Employee:
        """Method that returns employee based on employee id."""
        employee = self.db.query(Employee).filter(Employee.id_employee == employee_id).first()
        if employee is None:
            raise EmployeeNotFoundException(message=f'Employee with id {employee_id} not in the database.', code=400)
        return employee

    def read_employee_by_name(self, first_name: str) -> list[Employee]:
        """Method that returns all employees filtered by first name."""
        employee = self.db.query(Employee).filter(Employee.first_name == first_name).all()
        if employee is None:
            raise EmployeeNotFoundException(message=f'No employees with name {first_name} in the database.', code=400)
        return employee

    def read_employee_by_last_name(self, last_name: str) -> list[Employee]:
        """Method that returns all employees filtered by last name."""
        employee = self.db.query(Employee).filter(Employee.last_name == last_name).all()
        if employee is None:
            raise EmployeeNotFoundException(message=f'No employees wih name {last_name} in the database.', code=400)
        return employee

    def update_employee_by_id(self, employee_id: int, first_name: str = None, last_name: str = None, contact: str = None,
                              user_id: str = None) -> Employee:
        """Method that updates existing values in the database based on employee id."""
        employee = self.db.query(Employee).filter(Employee.id_employee == employee_id).first()
        if employee is None:
            raise EmployeeNotFoundException(message=f'Employee with id {employee_id} not in the database.', code=400)
        if first_name is not None and first_name != "":
            employee.first_name = first_name
        if last_name is not None and last_name != "":
            employee.last_name = last_name
        if contact is not None and contact != "":
            employee.contact = contact
        if user_id is not None and user_id != "":
            employee.user_id = user_id
        self.db.add(employee)
        self.db.commit()
        self.db.refresh(employee)
        return employee

    def delete_employee_by_id(self, employee_id: int) -> bool:
        """Method that deletes employee based on employee id."""
        employee = self.db.query(Employee).filter(Employee.id_employee == employee_id).first()
        if employee is None:
            raise EmployeeNotFoundException(message=f'User with id {employee_id} not in the database.', code=400)
        self.db.delete(employee)
        self.db.commit()
        return True

    def deactivate_employee(self, employee_id: int) -> bool:
        """Method that deactivates employee based on employee id."""
        employee = self.db.query(Employee).filter(Employee.id_employee == employee_id).first()
        if employee is None:
            raise EmployeeNotFoundException(message=f'User with id {employee_id} does not have active contracts.',
                                            code=400)
        employee.is_active = False
        self.db.add(employee)
        self.db.commit()
        self.db.refresh(employee)
        return True
