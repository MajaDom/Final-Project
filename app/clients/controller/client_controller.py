from app.clients.services import ClientService
from app.clients.exceptions import ClientWithIdDoesNotExistInTheDatabaseException
from fastapi import HTTPException, Response


class ClientController:

    @staticmethod
    def create_client(client_name: str, contact: str):
        try:
            client = ClientService.create_client(client_name=client_name, contact=contact)
            return client
        except Exception as e:
            raise e

    @staticmethod
    def get_all_clients():
        try:
            clients = ClientService.read_all_clients()
            return clients
        except Exception as e:
            raise HTTPException(status_code=500, detail=f"Unprocessed error: {str(e)}")

    @staticmethod
    def get_client_by_id(client_id: int):
        try:
            client = ClientService.read_client_by_id(client_id=client_id)
            return client
        except ClientWithIdDoesNotExistInTheDatabaseException as e:
            raise HTTPException(status_code=e.code, detail=e.message)
        except Exception as e:
            raise HTTPException(status_code=500, detail=f"Unprocessed error: {str(e)}")

    @staticmethod
    def get_client_by_name(client_name: str):
        try:
            client = ClientService.read_client_by_name(client_name=client_name)
            return client
        except ClientWithIdDoesNotExistInTheDatabaseException as e:
            raise HTTPException(status_code=e.code, detail=e.message)
        except Exception as e:
            raise HTTPException(status_code=500, detail=f"Unprocessed error: {str(e)}")

    @staticmethod
    def update_client_by_id(client_id: int, client_name: str = None, contact: str = None):
        try:
            client = ClientService.update_client_by_id(client_id=client_id, client_name=client_name, contact=contact)
            return client
        except ClientWithIdDoesNotExistInTheDatabaseException as e:
            raise HTTPException(status_code=e.code, detail=e.message)
        except Exception as e:
            raise HTTPException(status_code=500, detail=f"Unprocessed error: {str(e)}")

    @staticmethod
    def delete_client_by_id(client_id):
        try:
            ClientService.delete_client_by_id(client_id=client_id)
            return Response(content=f"Client with id {client_id} successfully deleted.")
        except ClientWithIdDoesNotExistInTheDatabaseException as e:
            raise HTTPException(status_code=e.code, detail=e.message)
        except Exception as e:
            raise HTTPException(status_code=500, detail=f"Unprocessed error: {str(e)}")

