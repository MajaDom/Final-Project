from sqlalchemy.orm import Session
from app.users.models import EmploymentContract
from app.users.exceptions import NoActiveContractsForEmployeeException


class EmploymentContractRepository:
    def __init__(self, db: Session):
        self.db = db

    def create_new_contract(self, start_date: str, contract_type: str, paycheck: float,
                            employee_id: int, end_date: str = None) -> EmploymentContract:
        """"Create new employee contract"""
        try:
            employment_contract = EmploymentContract(start_date=start_date, end_date=end_date,
                                                     contract_type=contract_type, paycheck=paycheck,
                                                     fk_employee_id=employee_id, is_active=True)
            self.db.add(employment_contract)
            self.db.commit()
            self.db.refresh(employment_contract)
            return employment_contract
        except Exception as e:
            raise e

    def read_contract_by_employee_id(self, id_employee: int) -> list[EmploymentContract]:
        """"Read all contracts based on defined employee"""
        employment_contract = self.db.query(EmploymentContract).filter(
            EmploymentContract.fk_employee_id == id_employee).all()
        if employment_contract is None:
            raise NoActiveContractsForEmployeeException(
                message=f"No active or archived contract for employee with id {id_employee} in the database",
                code=400)  # todo try raise an error
        return employment_contract

    def read_all_employment_contracts(self) -> list[EmploymentContract]:
        """"Read all contracts"""
        return self.db.query(EmploymentContract).all()

    def update_employment_contract(self, employee_id: int, start_date: str = None, end_date: str = None,
                                   contract_type: str = None,
                                   paycheck: float = None) -> EmploymentContract:
        employment_contract = self.db.query(EmploymentContract).filter(
            EmploymentContract.fk_employee_id == employee_id, EmploymentContract.is_active == 1).first()
        if employment_contract is None:
            raise NoActiveContractsForEmployeeException(code=400,
                                                        message=f"No active contract for the employee with id "
                                                                f"{employee_id}, and archived contracts can not be "
                                                                f"changed")
        if start_date is not None and start_date != "":
            employment_contract.start_date = start_date
        if end_date is not None and end_date != "":
            employment_contract.end_date = end_date
        if contract_type is not None and contract_type != "":
            employment_contract.contract_type = contract_type
        if paycheck is not None and paycheck != "":
            employment_contract.paycheck = paycheck
        self.db.add(employment_contract)
        self.db.commit()
        self.db.refresh(employment_contract)
        return employment_contract

    def archive_contract(self, employee_id) -> EmploymentContract:
        employment_contract = self.db.query(EmploymentContract).filter(EmploymentContract.fk_employee_id == employee_id,
                                                                       EmploymentContract.is_active == 1).first()
        if employment_contract is None:
            raise NoActiveContractsForEmployeeException(code=400,
                                                        message=f"No active contract for the employee with id "
                                                                f"{employee_id}, and archived contracts can not be "
                                                                f"changed")
        employment_contract.is_active = False
        self.db.add(employment_contract)
        self.db.commit()
        self.db.refresh(employment_contract)
        return employment_contract
