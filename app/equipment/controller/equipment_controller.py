from fastapi import HTTPException, Response
from sqlalchemy.exc import IntegrityError
from app.equipment.services import EquipmentService
from app.equipment.exceptions import EquipmentDoesNotExistInTheDatabaseException, InvalidInputException


class EquipmentController:

    @staticmethod
    def create_equipment(invoice_code: str, name: str, category: str, serial_number: str, net: float,
                         vat: float, date_of_purchase: str, shop_name: str,
                         date_of_transaction: str = None):
        try:
            equipment_contract = EquipmentService.create_equipment(invoice_code=invoice_code, name=name,
                                                                   category=category, serial_number=serial_number,
                                                                   net=net, vat=vat,
                                                                   date_of_transaction=date_of_transaction,
                                                                   date_of_purchase=date_of_purchase,
                                                                   shop_name=shop_name)
            return equipment_contract
        except IntegrityError as e:
            raise HTTPException(status_code=400, detail=str(e))
        except InvalidInputException as e:
            raise HTTPException(status_code=e.code, detail=e.message)
        except Exception as e:
            raise HTTPException(status_code=500, detail=str(e))

    @staticmethod
    def get_all_equipment():
        try:
            equipment = EquipmentService.read_all_equipment()
            return equipment
        except Exception as e:
            raise HTTPException(status_code=500, detail=f"Unprocessed error: {str(e)}")

    @staticmethod
    def get_equipment_by_id(equipment_id: int):
        try:
            equipment = EquipmentService.read_equipment_by_id(equipment_id=equipment_id)
            return equipment
        except EquipmentDoesNotExistInTheDatabaseException as e:
            raise HTTPException(status_code=e.code, detail=e.message)
        except Exception as e:
            raise HTTPException(status_code=500, detail=f"Unprocessed error: {str(e)}")

    @staticmethod
    def get_equipment_by_category(category: str):
        try:
            equipment = EquipmentService.read_equipment_by_category(category=category)
            return equipment
        except EquipmentDoesNotExistInTheDatabaseException as e:
            raise HTTPException(status_code=e.code, detail=e.message)
        except Exception as e:
            raise HTTPException(status_code=500, detail=f"Unprocessed error: {str(e)}")

    @staticmethod
    def get_equipment_by_name(name: str):
        try:
            equipment = EquipmentService.read_equipment_by_name(name=name)
            return equipment
        except EquipmentDoesNotExistInTheDatabaseException as e:
            raise HTTPException(status_code=e.code, detail=e.message)
        except Exception as e:
            raise HTTPException(status_code=500, detail=f"Unprocessed error: {str(e)}")

    @staticmethod
    def update_equipment_by_id(equipment_id: int, invoice_code: str = None, name: str = None,
                               category: str = None, serial_number: str = None, net: float = None,
                               vat: float = None, date_of_purchase: str = None, shop_name: str = None,
                               date_of_transaction: str = None):
        try:
            equipment = EquipmentService.update_equipment_by_id(equipment_id=equipment_id, invoice_code=invoice_code,
                                                                name=name,
                                                                category=category, serial_number=serial_number, net=net,
                                                                vat=vat, date_of_purchase=date_of_purchase,
                                                                shop_name=shop_name,
                                                                date_of_transaction=date_of_transaction)
            return equipment
        except EquipmentDoesNotExistInTheDatabaseException as e:
            raise HTTPException(status_code=e.code, detail=e.message)
        except Exception as e:
            raise HTTPException(status_code=500, detail=f"Unprocessed error: {str(e)}")

    @staticmethod
    def delete_equipment_by_id(equipment_id: int):
        try:
            EquipmentService.delete_equipment_by_id(equipment_id=equipment_id)
            return Response(content=f"Equipment with id {equipment_id} successfully deleted.")
        except EquipmentDoesNotExistInTheDatabaseException as e:
            raise HTTPException(status_code=e.code, detail=e.message)
        except Exception as e:
            raise HTTPException(status_code=500, detail=f"Unprocessed error: {str(e)}")
