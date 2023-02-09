from app.db import SessionLocal
from app.users.repository import EmploymentContractRepository


class EmploymentContractService:

    @staticmethod
    def create_new_contract(start_date: str, contract_type: str, paycheck: float,
                            employee_id, end_date: str = None) -> EmploymentContractRepository:
        try:
            with SessionLocal() as db:
                contract = EmploymentContractRepository(db)
                return contract.create_new_contract(start_date=start_date, end_date=end_date,
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
    def update_employment_contract(employee_id: int, start_date: str = None, end_date: str = None, contract_type: str = None,
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
