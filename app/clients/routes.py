from fastapi import APIRouter
from app.clients.controller import ClientController
from app.clients.controller import ClientContractController
from app.clients.schemas import *

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


client_contract_router = APIRouter(tags=["Client Contract"], prefix="/api/client-contract")


@client_contract_router.post("/create-new-client-contract", response_model=ClientContractSchema)
def create_client_contract(client_contract: ClientContractSchemaIN):
    return ClientContractController.create_client_contract(contract_code=client_contract.contract_code,
                                                           start_date=client_contract.start_date,
                                                           end_date=client_contract.end_date,
                                                           client_id=client_contract.client_id,
                                                           contract_description=client_contract.contract_description)


@client_contract_router.get("/get-all-client-contracts", response_model=list[ClientContractSchema])
def get_all_client_contracts():
    return ClientContractController.get_all_client_contracts()


@client_contract_router.get("/get-client-contract-by-id", response_model=ClientContractSchema)
def get_client_by_id(client_contract_id: int):
    return ClientContractController.get_client_contracts_by_id(client_contract_id=client_contract_id)


@client_contract_router.put("/update-client-contract-data", response_model=ClientContractSchema)
def update_client_contract_by_id(client_contract_id: int, client_contract: ClientContractSchemaUpdate):
    return ClientContractController.update_client_contract_by_id(client_contract_id=client_contract_id,
                                                                 contract_code=client_contract.contract_code,
                                                                 start_date=client_contract.start_date,
                                                                 end_date=client_contract.end_date,
                                                                 client_id=client_contract.client_id,
                                                                 contract_description=client_contract.contract_description)


@client_contract_router.delete("/delete-client-contract-by-id")
def delete_client_contract_by_id(client_contract_id: int):
    return ClientContractController.delete_client_contract_by_id(client_contract_id)
