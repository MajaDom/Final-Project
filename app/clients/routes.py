from fastapi import APIRouter
from app.clients.controller import ClientController
from app.clients.schemas import ClientSchema, ClientSchemaUpdate, ClientSchemaIN

client_router = APIRouter(tags=["Client"], prefix="/api/client")


@client_router.post("/create-new-client", response_model=ClientSchema)
def create_client(client: ClientSchemaIN):
    return ClientController.create_client(client_name=client.client_name, contact=client.contact)


@client_router.get("/get-all-clients", response_model=list[ClientSchema])
def get_all_clients():
    return ClientController.get_all_clients()


@client_router.get("/get-client-by-id", response_model=ClientSchema)
def get_client_by_id(client_id: int):
    return ClientController.get_client_by_id(client_id=client_id)


@client_router.get("/get-client-by-first-name", response_model=ClientSchema)
def get_client_by_name(client_name: str):
    return ClientController.get_client_by_name(client_name=client_name)


@client_router.put("/update-client-data", response_model=ClientSchema)
def update_client_by_id(client_id: int, client: ClientSchemaUpdate):
    return ClientController.update_client_by_id(client_id=client_id, client_name=client.client_name,
                                                contact=client.contact)


@client_router.delete("/delete-client-by-id")
def delete_client_by_id(client_id: int):
    return ClientController.delete_client_by_id(client_id)
