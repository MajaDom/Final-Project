# Routes for Suppliers
from fastapi import APIRouter, Depends
from app.suppliers.controller import SupplierController
from app.suppliers.schemas import SupplierSchema, SupplierSchemaUpdate, SupplierSchemaIN
from app.users.controller.user_auth_controller import JWTBearer

supplier_router = APIRouter(tags=["Supplier"], prefix="/api/supplier")


@supplier_router.post("/create-new-supplier",
                      response_model=SupplierSchema,
                      dependencies=[Depends(JWTBearer("super_user"))])
def create_supplier(supplier: SupplierSchemaIN):
    """
    - Method that creates new suppliers in the database.
    - **supplier_name**: mandatory field
    - **contact**: mandatory field
    """
    return SupplierController.create_supplier(supplier_name=supplier.supplier_name,
                                              contact=supplier.contact)


@supplier_router.get("/get-all-supplier")
def get_all_suppliers():
    """Method that reads all suppliers from the database."""
    return SupplierController.get_all_suppliers()


@supplier_router.get("/get-supplier-by-id")
def get_supplier_by_id(supplier_id: int):
    """
    - Method that reads a supplier based on supplier id.
    - **supplier_id**: mandatory parameter
    """
    return SupplierController.get_supplier_by_id(supplier_id=supplier_id)


@supplier_router.get("/get-supplier-by-name")
def get_supplier_by_name(supplier_name: str):
    """
    - Method that reads a supplier based on supplier name.
    - **supplier_name**: mandatory parameter
    """
    return SupplierController.get_supplier_by_name(supplier_name=supplier_name)


@supplier_router.put("/update-supplier-data", dependencies=[Depends(JWTBearer("super_user"))])
def update_supplier_by_id(supplier_id: int, supplier: SupplierSchemaUpdate):
    """
    - Method that allows data update of the supplier whose id has been provided.
    - **supplier_id**: not mandatory
    - **supplier_name**: not mandatory
    """
    return SupplierController.update_supplier_by_id(supplier_id=supplier_id, supplier_name=supplier.supplier_name,
                                                    contact=supplier.contact)


@supplier_router.delete("/delete-supplier-by-id", dependencies=[Depends(JWTBearer("super_user"))])
def delete_supplier_by_id(supplier_id: int):
    """
    - Method that allows data update of the supplier whose id has been provided.
    - **supplier_id**: mandatory parameter
    """
    return SupplierController.delete_supplier_id(supplier_id=supplier_id)
