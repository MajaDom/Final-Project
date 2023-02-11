from app.clients.services import ClientContractService
from app.clients.exceptions import ContractNotFoundException
from fastapi import HTTPException, Response


class ClientContractController:

    @staticmethod
    def create_client_contract(contract_code: str, start_date: str, end_date: str, client_id: int,
                               contract_description: str = None):
        try:
            client_contract = ClientContractService.create_client_contract(contract_code=contract_code,
                                                                           start_date=start_date, end_date=end_date,
                                                                           client_id=client_id,
                                                                           contract_description=contract_description)
            return client_contract
        except Exception as e:
            raise e

    @staticmethod
    def get_all_client_contracts():
        try:
            client_contracts = ClientContractService.read_all_client_contracts()
            return client_contracts
        except Exception as e:
            raise HTTPException(status_code=500, detail=f"Unprocessed error: {str(e)}")

    @staticmethod
    def get_client_contracts_by_id(client_contract_id: int):
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
    def delete_client_contract_by_id(client_contract_id):
        try:
            ClientContractService.delete_client_contract_by_id(client_contract_id=client_contract_id)
            return Response(content=f"Client contract with id {client_contract_id} successfully deleted.")
        except ContractNotFoundException as e:
            raise HTTPException(status_code=e.code, detail=e.message)
        except Exception as e:
            raise HTTPException(status_code=500, detail=f"Unprocessed error: {str(e)}")
