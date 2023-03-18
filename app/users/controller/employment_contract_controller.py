# It's a controller class that handles all the logic for the
# employment contract endpoints
from fastapi import HTTPException
from app.users.services import EmploymentContractService
from app.users.exceptions import EmployeeInactiveException, InvalidInputException, ExistingActiveContractException, \
    NoActiveContractsForEmployeeException, NoContractsForEmployeeException


class EmploymentContractController:

    @staticmethod
    def create_new_contract(start_date: str, contract_type: str, paycheck: float,
                            employee_id, end_date: str = None, termination_date: str = None,
                            description_contract: str = None):
        """Create new employee contract."""
        try:
            return EmploymentContractService.create_new_contract(start_date=start_date, end_date=end_date,
                                                                 contract_type=contract_type,
                                                                 paycheck=paycheck, employee_id=employee_id,
                                                                 termination_date=termination_date,
                                                                 description_contract=description_contract)
        except EmployeeInactiveException as e:
            raise HTTPException(status_code=e.code, detail=e.message)
        except ExistingActiveContractException as e:
            raise HTTPException(status_code=e.code, detail=e.message)
        except Exception as e:
            raise HTTPException(status_code=500, detail=f"Unprocessed error: {str(e)}")

    @staticmethod
    def read_all_employment_contracts():
        """Read all contracts."""
        try:
            return EmploymentContractService.read_all_employment_contracts()
        except Exception as e:
            raise HTTPException(status_code=500, detail=f"Unprocessed error: {str(e)}")

    @staticmethod
    def read_contract_by_employee_id(id_employee: int):
        """Read all contracts based on defined employee."""
        try:
            contracts = EmploymentContractService.read_contract_by_employee_id(id_employee=id_employee)
            return contracts
        except NoContractsForEmployeeException as e:
            raise HTTPException(status_code=e.code, detail=e.message)
        except Exception as e:
            raise HTTPException(status_code=500, detail=f"Unprocessed error: {str(e)}")

    @staticmethod
    def update_employment_contract(employee_id: int, start_date: str = None, end_date: str = None,
                                   contract_type: str = None, paycheck: float = None, termination_date: str = None,
                                   description_contract: str = None):
        """Method that updates values from the existing contracts. Only active contracts can be updated."""
        try:
            contract = EmploymentContractService.update_employment_contract(employee_id=employee_id,
                                                                            start_date=start_date, end_date=end_date,
                                                                            contract_type=contract_type,
                                                                            paycheck=paycheck,
                                                                            description_contract=description_contract,
                                                                            termination_date=termination_date)
            return contract
        except InvalidInputException as e:
            raise HTTPException(status_code=e.code, detail=e.message)
        except NoActiveContractsForEmployeeException as e:
            raise HTTPException(status_code=e.code, detail=e.message)
        except Exception as e:
            raise HTTPException(status_code=500, detail=f"Unknown error:{str(e)}")

    @staticmethod
    def archive_contract(employee_id):
        """Method that archives contract."""
        try:
            contract = EmploymentContractService.archive_contract(employee_id=employee_id)
            return contract
        except NoActiveContractsForEmployeeException as e:
            raise HTTPException(status_code=e.code, detail=e.message)
        except Exception as e:
            raise HTTPException(status_code=500, detail=f"Unknown error: {str(e)}")

    @staticmethod
    def read_contracts_that_are_going_to_expire_in_15_days():
        """Method that shows contracts that are going to expire in less than 15 days."""
        try:
            return EmploymentContractService.read_contracts_that_are_going_to_expire_in_15_days()
        except Exception as e:
            raise HTTPException(status_code=500, detail=f"Unprocessed error: {str(e)}")
