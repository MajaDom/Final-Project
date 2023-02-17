from app.db import SessionLocal
from app.equipment.repository import EquipmentRepository


class EquipmentService:

    @staticmethod
    def create_equipment(invoice_code: str, name: str, category: str, serial_number: str, net: float,
                         vat: float, date_of_purchase: str, shop_name: str,
                         date_of_transaction: str = None):
        try:
            with SessionLocal() as db:
                equipment_repository = EquipmentRepository(db)
                return equipment_repository.create_new_equipment(invoice_code=invoice_code, name=name,
                                                                 category=category, serial_number=serial_number,
                                                                 net=net, vat=vat, date_of_purchase=date_of_purchase,
                                                                 shop_name=shop_name,
                                                                 date_of_transaction=date_of_transaction)
        except Exception as e:
            return e

    @staticmethod
    def read_all_equipment():
        try:
            with SessionLocal() as db:
                equipment = EquipmentRepository(db)
                return equipment.read_all_equipment()
        except Exception as e:
            raise e

    @staticmethod
    def read_equipment_by_id(equipment_id: int):
        try:
            with SessionLocal() as db:
                equipment_repository = EquipmentRepository(db)
                return equipment_repository.read_equipment_by_id(equipment_id=equipment_id)
        except Exception as e:
            raise e

    @staticmethod
    def read_equipment_by_category(category: str):
        try:
            with SessionLocal() as db:
                equipment_repository = EquipmentRepository(db)
                return equipment_repository.read_equipment_by_category(category=category)
        except Exception as e:
            raise e

    @staticmethod
    def read_equipment_by_name(name: str):
        try:
            with SessionLocal() as db:
                equipment_repository = EquipmentRepository(db)
                return equipment_repository.read_equipment_by_name(name=name)
        except Exception as e:
            raise e

    @staticmethod
    def update_equipment_by_id(equipment_id: int, invoice_code: str = None, name: str = None,
                               category: str = None, serial_number: str = None, net: float = None,
                               vat: float = None, date_of_purchase: str = None, shop_name: str = None,
                               date_of_transaction: str = None):
        try:
            with SessionLocal() as db:
                equipment_repository = EquipmentRepository(db)
                return equipment_repository.update_equipment_by_id(equipment_id=equipment_id, invoice_code=invoice_code,
                                                                   name=name,
                                                                   category=category, serial_number=serial_number,
                                                                   net=net, vat=vat,
                                                                   date_of_purchase=date_of_purchase,
                                                                   date_of_transaction=date_of_transaction,
                                                                   shop_name=shop_name)
        except Exception as e:
            raise e

    @staticmethod
    def delete_equipment_by_id(equipment_id: int):
        try:
            with SessionLocal() as db:
                equipment_repository = EquipmentRepository(db)
                return equipment_repository.delete_equipment_by_id(equipment_id=equipment_id)
        except Exception as e:
            raise e
