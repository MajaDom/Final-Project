from fastapi import APIRouter
from app.equipment.controller import EquipmentController
from app.equipment.schemas import *

equipment_router = APIRouter(tags=["Equipment"], prefix="/api/client")


@equipment_router.post("/create-new-equipment", response_model=EquipmentSchema)
def create_client(equipment: EquipmentSchemaSchemaIN):
    return EquipmentController.create_equipment(invoice_code=equipment.invoice_code, name=equipment.name,
                                                category=equipment.category, serial_number=equipment.serial_number,
                                                net=equipment.net, vat=equipment.vat,
                                                date_of_purchase=equipment.date_of_purchase,
                                                shop_name=equipment.shop_name,
                                                date_of_transaction=equipment.date_of_transaction)


@equipment_router.get("/get-all-equipment", response_model=list[EquipmentSchema])
def get_all_equipment():
    return EquipmentController.get_all_equipment()


@equipment_router.get("/get-equipment-by-id", response_model=EquipmentSchema)
def get_client_by_id(equipment_id: int):
    return EquipmentController.get_equipment_by_id(equipment_id=equipment_id)


@equipment_router.get("/get-equipment-by-category", response_model=list[EquipmentSchema])
def get_equipment_by_category(category: str):
    return EquipmentController.get_equipment_by_category(category=category)


@equipment_router.get("/get-equipment-by-name", response_model=list[EquipmentSchema])
def get_equipment_by_name(name: str):
    return EquipmentController.get_equipment_by_name(name=name)


@equipment_router.put("/update-equipment-data", response_model=EquipmentSchema)
def update_equipment_by_id(equipment_id: int, equipment: EquipmentSchemaUpdate):
    return EquipmentController.update_equipment_by_id(invoice_code=equipment.invoice_code, name=equipment.name,
                                                      category=equipment.category,
                                                      serial_number=equipment.serial_number,
                                                      net=equipment.net, vat=equipment.vat,
                                                      date_of_purchase=equipment.date_of_purchase,
                                                      shop_name=equipment.shop_name,
                                                      date_of_transaction=equipment.date_of_transaction,
                                                      equipment_id=equipment_id)


@equipment_router.delete("/delete-equipment-by-id")
def delete_equipment_by_id(equipment_id: int):
    return EquipmentController.delete_equipment_by_id(equipment_id)
