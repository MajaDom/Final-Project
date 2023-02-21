from fastapi import HTTPException, Response
from sqlalchemy.exc import IntegrityError
from app.clients.services import ClientService
from app.clients.exceptions import ClientWithIdDoesNotExistInTheDatabaseException


class ClientController:

    @staticmethod
    def create_client(client_name: str, contact: str):
        """Method that creates a new client."""
        try:
            client = ClientService.create_client(client_name=client_name, contact=contact)
            return client
        except IntegrityError as e:
            raise HTTPException(status_code=400, detail=str(e))
        except Exception as e:
            raise HTTPException(status_code=500, detail=f"Unprocessed error: {str(e)}")

    @staticmethod
    def get_all_clients():
        """Method that returns all clients from the database."""
        try:
            clients = ClientService.read_all_clients()
            return clients
        except Exception as e:
            raise HTTPException(status_code=500, detail=f"Unprocessed error: {str(e)}")

    @staticmethod
    def get_client_by_id(client_id: int):
        """Method that returns client data based on client id."""
        try:
            client = ClientService.read_client_by_id(client_id=client_id)
            return client
        except ClientWithIdDoesNotExistInTheDatabaseException as e:
            raise HTTPException(status_code=e.code, detail=e.message)
        except Exception as e:
            raise HTTPException(status_code=500, detail=f"Unprocessed error: {str(e)}")

    @staticmethod
    def get_client_by_name(client_name: str):
        """Method that returns client base on name input."""
        try:
            client = ClientService.read_client_by_name(client_name=client_name)
            return client
        except ClientWithIdDoesNotExistInTheDatabaseException as e:
            raise HTTPException(status_code=e.code, detail=e.message)
        except Exception as e:
            raise HTTPException(status_code=500, detail=f"Unprocessed error: {str(e)}")

    @staticmethod
    def update_client_by_id(client_id: int, client_name: str = None, contact: str = None):
        """Method that allows updating client data based on client id."""
        try:
            client = ClientService.update_client_by_id(client_id=client_id, client_name=client_name, contact=contact)
            return client
        except ClientWithIdDoesNotExistInTheDatabaseException as e:
            raise HTTPException(status_code=e.code, detail=e.message)
        except Exception as e:
            raise HTTPException(status_code=500, detail=f"Unprocessed error: {str(e)}")

    @staticmethod
    def delete_client_by_id(client_id: int):
        """Method that deletes client from the database based on client id."""
        try:
            ClientService.delete_client_by_id(client_id=client_id)
            return Response(content=f"Client with id {client_id} successfully deleted.")
        except ClientWithIdDoesNotExistInTheDatabaseException as e:
            raise HTTPException(status_code=e.code, detail=e.message)
        except Exception as e:
            raise HTTPException(status_code=500, detail=f"Unprocessed error: {str(e)}")
