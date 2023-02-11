from app.db import SessionLocal
from app.clients.repository import ClientContractRepository


class ClientContractService:

    @staticmethod
    def create_client_contract(contract_code: str, start_date: str, end_date: str, client_id: int,
                               contract_description: str = None):
        try:
            with SessionLocal() as db:
                client_contact_repository = ClientContractRepository(db)
                return client_contact_repository.create_client_contract(contract_code=contract_code,
                                                                        start_date=start_date, end_date=end_date,
                                                                        client_id=client_id,
                                                                        contract_description=contract_description)
        except Exception as e:
            return e

    @staticmethod
    def read_all_client_contracts():
        try:
            with SessionLocal() as db:
                client_contracts = ClientContractRepository(db)
                return client_contracts.read_all_client_contracts()
        except Exception as e:
            raise e

    @staticmethod
    def read_client_contract_by_id(client_contract_id: int):
        try:
            with SessionLocal() as db:
                client_contract_repository = ClientContractRepository(db)
                return client_contract_repository.read_client_contract_by_id(client_contract_id=client_contract_id)
        except Exception as e:
            raise e

    @staticmethod
    def update_client_contract_by_id(client_contract_id: int, contract_code: str = None, start_date: str = None,
                                     contract_description: str = None,
                                     end_date: str = None, client_id: int = None):
        try:
            with SessionLocal() as db:
                client_contract_repository = ClientContractRepository(db)
                return client_contract_repository.update_client_contract_by_id(client_contract_id=client_contract_id,
                                                                               contract_code=contract_code,
                                                                               start_date=start_date,
                                                                               contract_description=contract_description,
                                                                               end_date=end_date, client_id=client_id)
        except Exception as e:
            raise e

    @staticmethod
    def delete_client_contract_by_id(client_contract_id: int):
        try:
            with SessionLocal() as db:
                client_contract_repository = ClientContractRepository(db)
                return client_contract_repository.delete_client_contract_by_id(client_contract_id=client_contract_id)
        except Exception as e:
            raise e
