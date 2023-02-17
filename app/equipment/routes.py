from fastapi import APIRouter
from app.equipment.controller import EquipmentController, AssignedEquipmentController
from app.equipment.schemas import *

equipment_router = APIRouter(tags=["Equipment"], prefix="/api/equipment")


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


assigned_equipment_router = APIRouter(tags=["Assigned Equipment"], prefix="/api/assigned-equipment")


@assigned_equipment_router.post("/create-new-assigned-equipment", response_model=AssignedEquipmentSchema)
def create_client(assigned_equipment: AssignedEquipmentSchemaIN):
    return AssignedEquipmentController.create_assigned_equipment(start_date=assigned_equipment.start_date,
                                                                 id_employee=assigned_equipment.id_employee,
                                                                 equipment_id=assigned_equipment.equipment_id,
                                                                 end_date=assigned_equipment.end_date)


@assigned_equipment_router.get("/get-all-equipment-history-of-assigned-equipment",
                               response_model=list[AssignedEquipmentSchema])
def get_all_history_of_assigned_equipment():
    return AssignedEquipmentController.read_all_history_of_assigned_equipment()


@assigned_equipment_router.get("/get-all-currently-assigned-equipment",
                               response_model=list[AssignedEquipmentSchema])
def get_all_currently_assigned_equipment():
    return AssignedEquipmentController.read_all_currently_assigned_equipment()


@assigned_equipment_router.get("/get-currently-assigned-equipment-by-id", response_model=AssignedEquipmentSchema)
def get_currently_assigned_equipment_by_id(assigned_equipment_id: int):
    return AssignedEquipmentController.read_currently_assigned_equipment_by_id(
        assigned_equipment_id=assigned_equipment_id)


@assigned_equipment_router.put("/update-assigned-equipment-by-id", response_model=AssignedEquipmentSchema)
def update_equipment_by_id(assigned_equipment_id: int, assigned_equipment: AssignedEquipmentSchemaUpdate):
    return AssignedEquipmentController.update_equipment_by_id(assigned_equipment_id=assigned_equipment_id,
                                                              start_date=assigned_equipment.start_date,
                                                              end_date=assigned_equipment.end_date,
                                                              id_employee=assigned_equipment.id_employee,
                                                              equipment_id=assigned_equipment.equipment_id)


@assigned_equipment_router.delete("/delete-assigned-equipment-by-id")
def delete_assigned_equipment_by_id(assigned_equipment_id: int):
    return AssignedEquipmentController.delete_assigned_equipment_by_id(assigned_equipment_id=assigned_equipment_id)
