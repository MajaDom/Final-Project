# routes for Equipment
from fastapi import APIRouter, Depends
from app.equipment.controller import EquipmentController, AssignedEquipmentController
from app.equipment.schemas import *
from app.users.controller.user_auth_controller import JWTBearer

equipment_router = APIRouter(tags=["Equipment"], prefix="/api/equipment")


@equipment_router.post("/create-new-equipment",
                       response_model=EquipmentSchema,
                       dependencies=[Depends(JWTBearer("super_user"))])
def create_new_equipment(equipment: EquipmentSchemaSchemaIN):
    """
    - Method that creates new equipment.
    - **invoice_code**: mandatory field
    - **name**: mandatory field
    - **category**: mandatory field
    - **serial_number**: mandatory field
    - **net**: mandatory field
    - **vat**: mandatory field
    - **date_of_purchase**: mandatory field
    - **date_of_transaction**: not mandatory
    - **shop_name**: mandatory field
    """
    return EquipmentController.create_equipment(invoice_code=equipment.invoice_code, name=equipment.name,
                                                category=equipment.category, serial_number=equipment.serial_number,
                                                net=equipment.net, vat=equipment.vat,
                                                date_of_purchase=equipment.date_of_purchase,
                                                shop_name=equipment.shop_name,
                                                date_of_transaction=equipment.date_of_transaction)


@equipment_router.get("/get-all-equipment", response_model=list[EquipmentSchema])
def get_all_equipment():
    """Method that returns all equipment from the database."""
    return EquipmentController.get_all_equipment()


@equipment_router.get("/get-equipment-by-id", response_model=EquipmentSchema)
def get_equipment_by_id(equipment_id: int):
    """
    - Method that returns equipment based on id.
    - **equipment_id**: mandatory parameter
    """
    return EquipmentController.get_equipment_by_id(equipment_id=equipment_id)


@equipment_router.get("/get-equipment-by-category", response_model=list[EquipmentSchema])
def get_equipment_by_category(category: str):
    """
    - Method that returns equipment based on category.
    - **category**: mandatory parameter
    """
    return EquipmentController.get_equipment_by_category(category=category)


@equipment_router.get("/get-equipment-by-name", response_model=list[EquipmentSchema])
def get_equipment_by_name(name: str):
    """
    - Method that returns equipment based on name.
    - **name**: mandatory parameter
    """
    return EquipmentController.get_equipment_by_name(name=name)


@equipment_router.put("/update-equipment-data",
                      response_model=EquipmentSchema,
                      dependencies=[Depends(JWTBearer("super_user"))])
def update_equipment_by_id(equipment_id: int, equipment: EquipmentSchemaUpdate):
    """Method that updates existing values from the database. No parameter is mandatory.
    - **invoice_code**: not mandatory
    - **name**: not mandatory
    - **category**: not mandatory
    - **serial_number**: not mandatory
    - **net**: not mandatory
    - **vat**: not mandatory
    - **date_of_purchase**: not mandatory
    - **date_of_transaction**: not mandatory
    - **shop_name**: not mandatory
    """
    return EquipmentController.update_equipment_by_id(invoice_code=equipment.invoice_code, name=equipment.name,
                                                      category=equipment.category,
                                                      serial_number=equipment.serial_number,
                                                      net=equipment.net, vat=equipment.vat,
                                                      date_of_purchase=equipment.date_of_purchase,
                                                      shop_name=equipment.shop_name,
                                                      date_of_transaction=equipment.date_of_transaction,
                                                      equipment_id=equipment_id)


@equipment_router.delete("/delete-equipment-by-id",dependencies=[Depends(JWTBearer("super_user"))])
def delete_equipment_by_id(equipment_id: int):
    """
    - Method that deletes equipment from the database based on equipment id.
    - **equipment_id**: mandatory parameter
    """
    return EquipmentController.delete_equipment_by_id(equipment_id)


assigned_equipment_router = APIRouter(tags=["Assigned Equipment"], prefix="/api/assigned-equipment")


@assigned_equipment_router.post("/create-new-assigned-equipment",
                                response_model=AssignedEquipmentSchema,
                                dependencies=[Depends(JWTBearer("super_user"))])
def assign_new_equipment(assigned_equipment: AssignedEquipmentSchemaIN):
    """
    - Method that creates new equipment and assigns it to an employee.
    - **start_date**: mandatory field
    - **id_employee**: mandatory field
    - **equipment_id**: mandatory field
    - **end_date**: not a mandatory field
    """
    return AssignedEquipmentController.create_assigned_equipment(start_date=assigned_equipment.start_date,
                                                                 id_employee=assigned_equipment.id_employee,
                                                                 equipment_id=assigned_equipment.equipment_id,
                                                                 end_date=assigned_equipment.end_date)


@assigned_equipment_router.get("/get-all-equipment-history-of-assigned-equipment",
                               response_model=list[AssignedEquipmentSchema])
def get_all_history_of_assigned_equipment():
    """Method that reads history of all assigned equipment in the database."""
    return AssignedEquipmentController.read_all_history_of_assigned_equipment()


@assigned_equipment_router.get("/get-all-currently-assigned-equipment",
                               response_model=list[AssignedEquipmentSchema])
def get_all_currently_assigned_equipment():
    """Method that returns all currently assigned equipment."""
    return AssignedEquipmentController.read_all_currently_assigned_equipment()


@assigned_equipment_router.get("/get-currently-assigned-equipment-by-id", response_model=AssignedEquipmentSchema)
def get_currently_assigned_equipment_by_id(equipment_id: int):
    """
    - Method that shows if equipment is available.
    - **assigned_equipment_id**:  mandatory parameter
    """
    return AssignedEquipmentController.read_currently_assigned_equipment_by_id(
        equipment_id=equipment_id)


@assigned_equipment_router.get("/get-currently-assigned-equipment-from-employee-by-id",
                               response_model=list[AssignedEquipmentSchema])
def get_currently_assigned_equipment_from_employee_by_id(employee_id: int):
    """
    - Method that reads if there is any assigned equipment for certain employee.
    - **employee_id**: mandatory parameter
    """
    return AssignedEquipmentController.read_currently_assigned_equipment_from_employee_by_id(
        employee_id=employee_id)


@assigned_equipment_router.put("/update-assigned-equipment-by-id",
                               response_model=AssignedEquipmentSchema,
                               dependencies=[Depends(JWTBearer("super_user"))])
def update_assigned_equipment_by_id(assigned_equipment_id: int, assigned_equipment: AssignedEquipmentSchemaUpdate):
    """
    - Method that updates values of existing assigned equipment.
    - **assigned_equipment_id**: mandatory parameter
    - **start_date**: not a mandatory field
    - **id_employee**: not a mandatory field
    - **equipment_id**: not a mandatory field
    - **end_date**: not a not a mandatory field
    """
    return AssignedEquipmentController.update_equipment_by_id(assigned_equipment_id=assigned_equipment_id,
                                                              start_date=assigned_equipment.start_date,
                                                              end_date=assigned_equipment.end_date,
                                                              id_employee=assigned_equipment.id_employee,
                                                              equipment_id=assigned_equipment.equipment_id)


@assigned_equipment_router.delete("/delete-assigned-equipment-by-id", dependencies=[Depends(JWTBearer("super_user"))])
def delete_assigned_equipment_by_id(assigned_equipment_id: int):
    """Method that deletes assigned equipment based on id."""
    return AssignedEquipmentController.delete_assigned_equipment_by_id(assigned_equipment_id=assigned_equipment_id)
