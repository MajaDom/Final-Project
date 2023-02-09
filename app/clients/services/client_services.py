from app.db import SessionLocal
from app.clients.repository import ClientRepository


class ClientService:

    @staticmethod
    def create_client(client_name: str, contact: str):
        try:
            with SessionLocal() as db:
                client_repository = ClientRepository(db)
                return client_repository.create_client(client_name=client_name, contact=contact)
        except Exception as e:
            return e

    @staticmethod
    def read_all_clients():
        try:
            with SessionLocal() as db:
                client_repository = ClientRepository(db)
                return client_repository.read_all_clients()
        except Exception as e:
            raise e

    @staticmethod
    def read_client_by_id(client_id: int):
        try:
            with SessionLocal() as db:
                client_repository = ClientRepository(db)
                return client_repository.read_client_by_id(client_id=client_id)
        except Exception as e:
            raise e

    @staticmethod
    def read_client_by_name(client_name: str):
        try:
            with SessionLocal() as db:
                client_repository = ClientRepository(db)
                return client_repository.read_client_by_name(client_name=client_name)
        except Exception as e:
            raise e

    @staticmethod
    def update_client_by_id(client_id: int, client_name: str = None, contact: str = None):
        try:
            with SessionLocal() as db:
                client_repository = ClientRepository(db)
                return client_repository.update_client(client_id=client_id, client_name=client_name, contact=contact)
        except Exception as e:
            raise e

    @staticmethod
    def delete_client_by_id(client_id):
        try:
            with SessionLocal() as db:
                client_repository = ClientRepository(db)
                return client_repository.delete_client_by_id(client_id=client_id)
        except Exception as e:
            raise e

