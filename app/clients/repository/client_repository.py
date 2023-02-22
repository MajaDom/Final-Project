# This class is a repository class that handles all the database operations for the client model
from sqlalchemy.orm import Session
from sqlalchemy.exc import IntegrityError
from app.clients.models import Client
from app.clients.exceptions import ClientWithIdDoesNotExistInTheDatabaseException


class ClientRepository:
    def __init__(self, db: Session):
        self.db = db

    def create_client(self, client_name: str, contact: str) -> Client:
        """Method that creates a new client."""
        try:
            client = Client(client_name=client_name, contact=contact)
            self.db.add(client)
            self.db.commit()
            self.db.refresh(client)
            return client
        except IntegrityError as e:
            raise e
        except Exception as e:
            raise e

    def read_all_clients(self) -> list[Client]:
        """Method that returns all clients from the database."""
        clients = self.db.query(Client).all()
        return clients

    def read_client_by_id(self, client_id: int) -> Client:
        """Method that returns client data based on client id."""
        client = self.db.query(Client).filter(Client.client_id == client_id).first()
        if client is None:
            raise ClientWithIdDoesNotExistInTheDatabaseException(
                message=f'Client with id {client_id} not in the database.', code=400)
        return client

    def read_client_by_name(self, client_name: str) -> Client:
        """Method that returns client base on name input."""
        client = self.db.query(Client).filter(Client.client_name == client_name).first()
        if client is None:
            raise ClientWithIdDoesNotExistInTheDatabaseException(
                message=f'Client with name {client_name} not in the database.', code=400)
        return client

    def update_client(self, client_id: int, client_name: str = None, contact: str = None) -> Client:
        """Method that allows updating client data based on client id."""
        client = self.db.query(Client).filter(Client.client_id == client_id).first()
        if client is None:
            raise ClientWithIdDoesNotExistInTheDatabaseException(
                message=f'Client with id {client_id} not in the database.', code=400)
        if client_name is not None and client_name != "":
            client.client_name = client_name
        if contact is not None and contact != "":
            client.contact = contact
        self.db.add(client)
        self.db.commit()
        self.db.refresh(client)
        return client

    def delete_client_by_id(self, client_id: int) -> bool:
        """Method that deletes client from the database based on client id."""
        client = self.db.query(Client).filter(Client.client_id == client_id).first()
        if client is None:
            raise ClientWithIdDoesNotExistInTheDatabaseException(
                message=f'Client with id {client_id} not in the database.', code=400)
        self.db.delete(client)
        self.db.commit()
        return True
