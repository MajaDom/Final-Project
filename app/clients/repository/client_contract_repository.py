from sqlalchemy.orm import Session
from app.clients.models import ClientContract
from app.clients.exceptions import ContractNotFoundException


class ClientContractRepository:
    def __init__(self, db: Session):
        self.db = db

    def create_client_contract(self, contract_code: str, start_date: str, client_id: int,
                               contract_description: str = None,end_date: str = None,) -> ClientContract:
        try:
            client_contract = ClientContract(contract_code=contract_code, start_date=start_date,
                                             contract_description=contract_description, end_date=end_date,
                                             client_id=client_id)
            self.db.add(client_contract)
            self.db.commit()
            self.db.refresh(client_contract)
            return client_contract
        except Exception as e:
            raise e

    def read_all_client_contracts(self) -> list[ClientContract]:
        client_contracts = self.db.query(ClientContract).all()
        return client_contracts

    def read_client_contract_by_id(self, client_contract_id: int) -> ClientContract:
        client_contract = self.db.query(ClientContract).filter(
            ClientContract.client_contract_id == client_contract_id).first()
        if client_contract is None:
            raise ContractNotFoundException(message=f'Contract with id {client_contract_id} not in the database.',
                                            code=400)
        return client_contract

    def update_client_contract_by_id(self, client_contract_id: int, contract_code: str = None, start_date: str = None,
                                     contract_description: str = None,
                                     end_date: str = None, client_id: int = None) -> ClientContract:
        client_contract = self.db.query(ClientContract).filter(
            ClientContract.client_contract_id == client_contract_id).first()

        if client_contract is None:
            raise ContractNotFoundException(message=f'Contract with id {client_contract_id} not in the database.',
                                            code=400)
        if contract_code is not None and contract_code != "":
            client_contract.contract_code = contract_code
        if start_date is not None and start_date != "":
            client_contract.start_date = start_date
        if contract_description is not None and contract_description != "":
            client_contract.contract_description = contract_description
        if end_date is not None and end_date != "":
            client_contract.end_date = end_date
        if client_id is not None and client_id != "":
            client_contract.client_id = client_id

        self.db.add(client_contract)
        self.db.commit()
        self.db.refresh(client_contract)
        return client_contract

    def delete_client_contract_by_id(self, client_contract_id: int):
        client_contract = self.db.query(ClientContract).filter(
            ClientContract.client_contract_id == client_contract_id).first()
        if client_contract is None:
            raise ContractNotFoundException(message=f'Contract with id {client_contract_id} not in the database.',
                                            code=400)
        self.db.delete(client_contract)
        self.db.commit()
        return True
