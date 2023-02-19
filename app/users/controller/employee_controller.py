from app.users.services import EmployeeService
from app.users.services import EmploymentContractService
from app.equipment.services import AssignedEquipmentService
from app.users.exceptions import EmployeeNotFoundException, NoActiveContractsForEmployeeException
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
    def get_all_employees_containing_text_in_first_name(text: str):
        try:
            employees = EmployeeService.read_all_employees_containing_text_in_first_name(text=text)
            return employees
        except Exception as e:
            raise HTTPException(status_code=500, detail=f"Unprocessed error: {str(e)}")

    @staticmethod
    def get_employee_by_id(employee_id: int):
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
    def get_employee_by_last_name(last_name: str):
        try:
            employee = EmployeeService.read_employee_by_last_name(last_name=last_name)
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

    @staticmethod
    def deactivate_employee(employee_id):
        try:
            EmployeeService.deactivate_employee(employee_id=employee_id)
            return Response(content=f"Employee with id {employee_id} successfully deactivated.")
        except EmployeeNotFoundException as e:
            raise HTTPException(status_code=e.code, detail=e.message)
        except Exception as e:
            raise HTTPException(status_code=500, detail=f"Unprocessed error: {str(e)}")

    @staticmethod
    def deactivate_employee_if_conditions_are_met(employee_id: int):
        try:
            EmploymentContractService.archive_contract(employee_id=employee_id)
            EmployeeService.deactivate_employee(employee_id=employee_id)
            assigned_equipment = AssignedEquipmentService.read_currently_assigned_equipment_from_employee_by_id(
                employee_id=employee_id)
            if not assigned_equipment:
                return Response(content=f"Employee with id {employee_id} has no assigned equipment and has been fired.")
            return assigned_equipment
        except EmployeeNotFoundException as e:
            raise HTTPException(status_code=e.code, detail=e.message)
        except NoActiveContractsForEmployeeException as e:
            raise HTTPException(status_code=e.code, detail=e.message)
        except Exception as e:
            raise HTTPException(status_code=500, detail=f"Unprocessed error: {str(e)}")
