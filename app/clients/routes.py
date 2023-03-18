# Routes for Cilents
from fastapi import APIRouter, Depends
from app.clients.schemas import *
from app.clients.controller import ClientController
from app.clients.controller import ClientContractController
from app.users.controller.user_auth_controller import JWTBearer

client_router = APIRouter(tags=["Client"], prefix="/api/client")


@client_router.post("/create-new-client",
                    response_model=ClientSchema,
                    dependencies=[Depends(JWTBearer("super_user"))])
def create_client(client: ClientSchemaIN):
    """
    - Method that creates a new client.
    - **client_name**: mandatory field, also unique
    - **contact**: mandatory, unique field, could be a phone number or an email
    """
    return ClientController.create_client(client_name=client.client_name, contact=client.contact)


@client_router.get("/get-all-clients", response_model=list[ClientSchema])
def get_all_clients():
    """Method that returns all clients from the database."""
    return ClientController.get_all_clients()


@client_router.get("/get-client-by-id", response_model=ClientSchema)
def get_client_by_id(client_id: int):
    """
    - Method that returns all clients from the database.
    - **client_id**: mandatory parameter
    """
    return ClientController.get_client_by_id(client_id=client_id)


@client_router.get("/get-client-by-first-name", response_model=ClientSchema)
def get_client_by_name(client_name: str):
    """
    - Method that returns client base on name input.
    - **client_name**: mandatory parameter (client name is unique)
    """
    return ClientController.get_client_by_name(client_name=client_name)


@client_router.put("/update-client-data",
                   response_model=ClientSchema,
                   dependencies=[Depends(JWTBearer("super_user"))])
def update_client_by_id(client_id: int, client: ClientSchemaUpdate):
    """
    - Method that allows updating client data based on client id. It is not necessary to fill all the fields, they
    could be erased and data will not update.
    - **client_id**: mandatory parameter
    """
    return ClientController.update_client_by_id(client_id=client_id, client_name=client.client_name,
                                                contact=client.contact)


@client_router.delete("/delete-client-by-id", dependencies=[Depends(JWTBearer("super_user"))])
def delete_client_by_id(client_id: int):
    """
    Method that deletes client from the database based on client id.
    - **client_id**: mandatory parameter
    """
    return ClientController.delete_client_by_id(client_id)


client_contract_router = APIRouter(tags=["Client Contract"], prefix="/api/client-contract")


@client_contract_router.post("/create-new-client-contract",
                             response_model=ClientContractSchema,
                             dependencies=[Depends(JWTBearer("super_user"))])
def create_client_contract(client_contract: ClientContractSchemaIN):
    """
    - **contract_code**: each contract must have a code
    - **start_date**: each contract must have a start date, e.g. 2022-10-13
    - **contract_description**: contract description, not mandatory
    - **end_date**: end_date of contract, not mandatory, e.g. 2023-10-10
    """
    return ClientContractController.create_client_contract(contract_code=client_contract.contract_code,
                                                           start_date=client_contract.start_date,
                                                           end_date=client_contract.end_date,
                                                           client_id=client_contract.client_id,
                                                           contract_description=client_contract.contract_description)


@client_contract_router.get("/get-all-client-contracts",
                            response_model=list[ClientContractSchema],
                            dependencies=[Depends(JWTBearer("super_user"))])
def get_all_client_contracts():
    """Returns all contracts in the database."""
    return ClientContractController.get_all_client_contracts()


@client_contract_router.get("/get-client-contract-by-id",
                            response_model=ClientContractSchema,
                            dependencies=[Depends(JWTBearer("super_user"))])
def get_client_contract_by_id(client_contract_id: int):
    """
    - Method that retrieves a contract from the database based on contract id.
    - **client_contract_id**: mandatory parameter
    """
    return ClientContractController.get_client_contracts_by_id(client_contract_id=client_contract_id)


@client_contract_router.put("/update-client-contract-data",
                            response_model=ClientContractSchema,
                            dependencies=[Depends(JWTBearer("super_user"))])
def update_client_contract_by_id(client_contract_id: int, client_contract: ClientContractSchemaUpdate):
    """
    - Method that updates values in the database based on the contract id.
    - When updating it is not mandatory to write anything, field could be erased and values in the database will not
    update
    """
    return ClientContractController.update_client_contract_by_id(
        client_contract_id=client_contract_id,
        contract_code=client_contract.contract_code,
        start_date=client_contract.start_date,
        end_date=client_contract.end_date,
        client_id=client_contract.client_id,
        contract_description=client_contract.contract_description)


@client_contract_router.delete("/delete-client-contract-by-id", dependencies=[Depends(JWTBearer("super_user"))])
def delete_client_contract_by_id(client_contract_id: int):
    """
    - Method that deletes a contract from the database based on contract id
    - **client_contract_id**: mandatory parameter
    """
    return ClientContractController.delete_client_contract_by_id(client_contract_id)
