from fastapi import APIRouter
from app.suppliers.controller import SupplierController
from app.suppliers.schemas import SupplierSchema, SupplierSchemaUpdate, SupplierSchemaIN

supplier_router = APIRouter(tags=["Supplier"], prefix="/api/supplier")


@supplier_router.post("/create-new-supplier", response_model=SupplierSchema)
def create_cost_center(supplier: SupplierSchemaIN):
    return SupplierController.create_supplier(supplier_name=supplier.supplier_name,
                                              contact=supplier.contact)


@supplier_router.get("/get-all-supplier")
def get_all_supplier():
    return SupplierController.get_all_suppliers()


@supplier_router.get("/get-supplier-by-id")
def get_supplier_by_id(supplier_id: int):
    return SupplierController.get_supplier_by_id(supplier_id=supplier_id)


@supplier_router.get("/get-supplier-by-name")
def get_cost_center_by_name(supplier_name: str):
    return SupplierController.get_supplier_by_name(supplier_name=supplier_name)


@supplier_router.put("/update-supplier-data")
def update_supplier_by_id(supplier_id: int, supplier: SupplierSchemaUpdate):
    return SupplierController.update_supplier_by_id(supplier_id=supplier_id, supplier_name=supplier.supplier_name,
                                                    contact=supplier.contact)


@supplier_router.delete("/delete-supplier-by-id")
def delete_supplier_by_id(supplier_id: int):
    return SupplierController.delete_supplier_id(supplier_id=supplier_id)
