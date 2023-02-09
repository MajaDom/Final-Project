from app.users.services import EmploymentContractService
from fastapi import HTTPException, Response
from app.users.exceptions import NoContractsForEmployeeException, NoActiveContractsForEmployeeException


class EmploymentContractController:

    @staticmethod
    def create_new_contract(start_date: str, contract_type: str, paycheck: float,
                            employee_id, end_date: str = None):
        try:
            return EmploymentContractService.create_new_contract(start_date=start_date, end_date=end_date,
                                                                 contract_type=contract_type,
                                                                 paycheck=paycheck, employee_id=employee_id)
        except Exception as e:
            raise HTTPException(status_code=500, detail=f"Unprocessed error: {str(e)}")

    @staticmethod
    def read_all_employment_contracts():
        try:
            return EmploymentContractService.read_all_employment_contracts()
        except Exception as e:
            raise HTTPException(status_code=500, detail=f"Unprocessed error: {str(e)}")

    @staticmethod
    def read_contract_by_employee_id(id_employee: int):
        try:
            contracts = EmploymentContractService.read_contract_by_employee_id(id_employee=id_employee)
            return contracts
        except NoContractsForEmployeeException as e:
            raise HTTPException(status_code=e.code, detail=e.message)
        except Exception as e:
            raise HTTPException(status_code=500, detail=f"Unprocessed error: {str(e)}")

    @staticmethod
    def update_employment_contract(employee_id: int, start_date: str = None, end_date: str = None,
                                   contract_type: str = None,
                                   paycheck: float = None):
        try:
            contract = EmploymentContractService.update_employment_contract(employee_id=employee_id,
                                                                            start_date=start_date, end_date=end_date,
                                                                            contract_type=contract_type,
                                                                            paycheck=paycheck)
            return contract
        except NoActiveContractsForEmployeeException as e:
            raise HTTPException(status_code=e.code, detail=e.message)
        except Exception as e:
            raise HTTPException(status_code=500, detail="Unknown error.")

    @staticmethod
    def archive_contract(employee_id):
        try:
            contract = EmploymentContractService.archive_contract(employee_id=employee_id)
            return contract
        except NoActiveContractsForEmployeeException as e:
            raise HTTPException(status_code=e.code, detail=e.message)
        except Exception as e:
            raise HTTPException(status_code=500, detail=f"Unknown error: {str(e)}")
