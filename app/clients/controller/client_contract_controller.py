from app.clients.services import ClientContractService
from app.clients.exceptions import ContractNotFoundException, InvalidInputException
from fastapi import HTTPException, Response
from sqlalchemy.exc import IntegrityError


class ClientContractController:

    @staticmethod
    def create_client_contract(contract_code: str, start_date: str, end_date: str, client_id: int,
                               contract_description: str = None):
        """Method that creates new client contract"""
        try:
            client_contract = ClientContractService.create_client_contract(contract_code=contract_code,
                                                                           start_date=start_date, end_date=end_date,
                                                                           client_id=client_id,
                                                                           contract_description=contract_description)
            return client_contract
        except IntegrityError as e:
            raise HTTPException(status_code=400, detail=f"Unprocessed error: {str(e)}")
        except InvalidInputException as e:
            raise HTTPException(status_code=e.code, detail=f"Unprocessed error: {e.message}")
        except Exception as e:
            raise e

    @staticmethod
    def get_all_client_contracts():
        """Method that shows all contracts from the database."""
        try:
            client_contracts = ClientContractService.read_all_client_contracts()
            return client_contracts
        except Exception as e:
            raise HTTPException(status_code=500, detail=f"Unprocessed error: {str(e)}")

    @staticmethod
    def get_client_contracts_by_id(client_contract_id: int):
        """"Method that retrieves a contract from the database based on contract id"""
        try:
            client_contracts = ClientContractService.read_client_contract_by_id(client_contract_id=client_contract_id)
            return client_contracts
        except ContractNotFoundException as e:
            raise HTTPException(status_code=e.code, detail=e.message)
        except Exception as e:
            raise HTTPException(status_code=500, detail=f"Unprocessed error: {str(e)}")

    @staticmethod
    def update_client_contract_by_id(client_contract_id: int, contract_code: str = None, start_date: str = None,
                                     contract_description: str = None,
                                     end_date: str = None, client_id: int = None):
        """Method that updates values in the database based on the contract id."""
        try:
            client_contract = ClientContractService.update_client_contract_by_id(
                client_contract_id=client_contract_id, contract_code=contract_code, start_date=start_date,
                contract_description=contract_description, end_date=end_date, client_id=client_id)
            return client_contract
        except ContractNotFoundException as e:
            raise HTTPException(status_code=e.code, detail=e.message)
        except Exception as e:
            raise HTTPException(status_code=500, detail=f"Unprocessed error: {str(e)}")

    @staticmethod
    def delete_client_contract_by_id(client_contract_id: int):
        """Method that deletes a contract from the database based on contract id"""
        try:
            ClientContractService.delete_client_contract_by_id(client_contract_id=client_contract_id)
            return Response(content=f"Client contract with id {client_contract_id} successfully deleted.")
        except ContractNotFoundException as e:
            raise HTTPException(status_code=e.code, detail=e.message)
        except Exception as e:
            raise HTTPException(status_code=500, detail=f"Unprocessed error: {str(e)}")
