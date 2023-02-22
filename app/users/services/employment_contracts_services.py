# This class is responsible for all the operations related to the employment contract.
from app.db import SessionLocal
from app.users.repository import EmploymentContractRepository, EmployeeRepository
from app.users.exceptions import EmployeeInactiveException, ExistingActiveContractException


class EmploymentContractService:

    @staticmethod
    def create_new_contract(start_date: str, contract_type: str, paycheck: float,
                            employee_id, end_date: str = None) -> EmploymentContractRepository:
        try:
            with SessionLocal() as db:
                employee = EmployeeRepository(db)
                if employee.read_employee_by_id(employee_id=employee_id).is_active == 0:
                    raise EmployeeInactiveException(message="Employee is fired, it is not possible to add new contract",
                                                    code=400)
                contract_repo = EmploymentContractRepository(db)
                active_contract = contract_repo.read_contract_by_employee_id(id_employee=employee_id)
                for contract in active_contract:
                    if contract.is_active == 1:
                        raise ExistingActiveContractException(
                            message="There is already an active contract in the database, deactivate existing.",
                            code=400)
                return contract_repo.create_new_contract(start_date=start_date, end_date=end_date,
                                                         contract_type=contract_type,
                                                         paycheck=paycheck, employee_id=employee_id)
        except Exception as e:
            raise e

    @staticmethod
    def read_contract_by_employee_id(id_employee: int):
        try:
            with SessionLocal() as db:
                contracts = EmploymentContractRepository(db)
                return contracts.read_contract_by_employee_id(id_employee=id_employee)
        except Exception as e:
            raise e

    @staticmethod
    def read_all_employment_contracts():
        try:
            with SessionLocal() as db:
                contracts = EmploymentContractRepository(db)
                return contracts.read_all_employment_contracts()
        except Exception as e:
            raise e

    @staticmethod
    def update_employment_contract(employee_id: int, start_date: str = None, end_date: str = None,
                                   contract_type: str = None,
                                   paycheck: float = None):
        try:
            with SessionLocal() as db:
                contract = EmploymentContractRepository(db)
                return contract.update_employment_contract(employee_id=employee_id, start_date=start_date,
                                                           end_date=end_date, contract_type=contract_type,
                                                           paycheck=paycheck)
        except Exception as e:
            raise e

    @staticmethod
    def archive_contract(employee_id):
        try:
            with SessionLocal() as db:
                contract = EmploymentContractRepository(db)
                return contract.archive_contract(employee_id=employee_id)
        except Exception as e:
            raise e

    @staticmethod
    def read_contracts_that_are_going_to_expire_in_15_days():
        try:
            with SessionLocal() as db:
                contracts = EmploymentContractRepository(db)
                return contracts.read_contracts_that_are_going_to_expire_in_15_days()
        except Exception as e:
            raise e
