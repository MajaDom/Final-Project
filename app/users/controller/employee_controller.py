from app.users.services import EmployeeService
from app.users.exceptions import EmployeeNotFoundException
from fastapi import HTTPException, Response


class EmployeeController:

    @staticmethod
    def create_employee(first_name: str, last_name: str, contact: str, user_id: str = None):
        try:
            employee = EmployeeService.create_employee(first_name=first_name, last_name=last_name, contact=contact,
                                                       user_id=user_id)
            return employee
        except Exception as e:
            raise e

    @staticmethod
    def get_all_employees():
        try:
            employees = EmployeeService.read_all_employees()
            return employees
        except Exception as e:
            raise HTTPException(status_code=500, detail=f"Unprocessed error: {str(e)}")

    @staticmethod
    def get_employee_by_id(employee_id: str):
        try:
            employee = EmployeeService.read_employee_by_id(employee_id=employee_id)
            return employee
        except EmployeeNotFoundException as e:
            raise HTTPException(status_code=e.code, detail=e.message)
        except Exception as e:
            raise HTTPException(status_code=500, detail=f"Unprocessed error: {str(e)}")

    @staticmethod
    def get_employee_by_name(first_name: str):
        try:
            employee = EmployeeService.read_employee_by_name(first_name=first_name)
            return employee
        except EmployeeNotFoundException as e:
            raise HTTPException(status_code=e.code, detail=e.message)
        except Exception as e:
            raise HTTPException(status_code=500, detail=f"Unprocessed error: {str(e)}")

    @staticmethod
    def update_employee_by_id(employee_id, first_name: str = None, last_name: str = None, contact: str = None,
                              user_id: str = None):
        try:
            employee = EmployeeService.update_employee_by_id(employee_id=employee_id, first_name=first_name,
                                                             last_name=last_name,
                                                             contact=contact, user_id=user_id)
            return employee
        except EmployeeNotFoundException as e:
            raise HTTPException(status_code=e.code, detail=e.message)
        except Exception as e:
            raise HTTPException(status_code=500, detail=f"Unprocessed error: {str(e)}")

    @staticmethod
    def delete_employee_by_id(employee_id):
        try:
            EmployeeService.delete_employee_by_id(employee_id=employee_id)
            return Response(content=f"User with id {employee_id} successfully deleted.")
        except EmployeeNotFoundException as e:
            raise HTTPException(status_code=e.code, detail=e.message)
        except Exception as e:
            raise HTTPException(status_code=500, detail=f"Unprocessed error: {str(e)}")
