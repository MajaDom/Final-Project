from sqlalchemy.orm import Session
from app.users.models import Employee
from app.users.exceptions import EmployeeNotFoundException


class EmployeeRepository:
    def __init__(self, db: Session):
        self.db = db

    def create_employee(self, first_name: str, last_name: str, contact: str, user_id: str = None):
        try:
            employee = Employee(first_name=first_name, last_name=last_name, contact=contact, user_id=user_id)
            self.db.add(employee)
            self.db.commit()
            self.db.refresh(employee)
            return employee
        except Exception as e:
            raise e

    def read_all_employees(self) -> list[Employee]:
        employees = self.db.query(Employee).all()
        return employees

    def read_employee_by_id(self, employee_id: str) -> Employee:
        employee = self.db.query(Employee).filter(Employee.id_employee == employee_id).first()
        if employee is None:
            raise EmployeeNotFoundException(message=f'Employee with id {employee_id} not in the database.', code=400)
        return employee

    def read_employee_by_name(self, first_name: str) -> Employee:
        employee = self.db.query(Employee).filter(Employee.first_name == first_name).first()
        if employee is None:
            raise EmployeeNotFoundException(message=f'Employee with name {first_name} not in the database.', code=400)
        return employee

    def update_employee_by_id(self, employee_id, first_name: str = None, last_name: str = None, contact: str = None,
                              user_id: str = None) -> Employee:
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

    def delete_employee_by_id(self, employee_id: str):
        employee = self.db.query(Employee).filter(Employee.id_employee == employee_id).first()
        if employee is None:
            raise EmployeeNotFoundException(message=f'User with id {employee_id} not in the database.', code=400)
        self.db.delete(employee)
        self.db.commit()
        return True
