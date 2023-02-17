from sqlalchemy.orm import Session
from app.equipment.models import Equipment
from app.equipment.exceptions import EquipmentDoesNotExistInTheDatabaseException


class EquipmentRepository:
    def __init__(self, db: Session):
        self.db = db

    def create_new_equipment(self, invoice_code: str, name: str, category: str, serial_number: str, net: float,
                             vat: float, date_of_purchase: str, shop_name: str,
                             date_of_transaction: str = None) -> Equipment:
        try:
            equipment = Equipment(invoice_code=invoice_code, name=name, category=category, serial_number=serial_number,
                                  net=net, vat=vat, date_of_purchase=date_of_purchase,
                                  date_of_transaction=date_of_transaction, shop_name=shop_name)
            self.db.add(equipment)
            self.db.commit()
            self.db.refresh(equipment)
            return equipment
        except Exception as e:
            raise e

    def read_all_equipment(self) -> list[Equipment]:
        equipment = self.db.query(Equipment).all()
        return equipment

    def read_equipment_by_id(self, equipment_id: int) -> Equipment:
        equipment = self.db.query(Equipment).filter(
            Equipment.equipment_id == equipment_id).first()
        if equipment is None:
            raise EquipmentDoesNotExistInTheDatabaseException(
                message=f'Equipment with id {equipment_id} does not exist in the database.',
                code=400)
        return equipment

    def read_equipment_by_category(self, category: str) -> list[Equipment]:
        equipment = self.db.query(Equipment).filter(Equipment.category.like(f"%{category}%")).all()
        if equipment is None:
            raise EquipmentDoesNotExistInTheDatabaseException(
                message=f'Category containing {category} does not exist in the database.',
                code=400)
        return equipment

    def read_equipment_by_name(self, name: str) -> list[Equipment]:
        equipment = self.db.query(Equipment).filter(Equipment.name.like(f"%{name}%")).all()
        if equipment is None:
            raise EquipmentDoesNotExistInTheDatabaseException(
                message=f'Name containing {name} does not exist in the database.',
                code=400)
        return equipment

    def update_equipment_by_id(self, equipment_id: int, invoice_code: str = None, name: str = None,
                               category: str = None, serial_number: str = None, net: float = None,
                               vat: float = None, date_of_purchase: str = None, shop_name: str = None,
                               date_of_transaction: str = None) -> Equipment:
        equipment = self.db.query(Equipment).filter(Equipment.equipment_id == equipment_id).first()

        if equipment is None:
            raise EquipmentDoesNotExistInTheDatabaseException(
                message=f'Equipment with id {equipment_id} not in the database.',
                code=400)
        if invoice_code is not None and invoice_code != "":
            equipment.invoice_code = invoice_code
        if name is not None and name != "":
            equipment.name = name
        if category is not None and category != "":
            equipment.category = category
        if serial_number is not None and serial_number != "":
            equipment.serial_number = serial_number
        if net is not None and net != "":
            equipment.net = net
        if vat is not None and vat != "":
            equipment.vat = vat
        if date_of_purchase is not None and date_of_purchase != "":
            equipment.date_of_purchase = date_of_purchase
        if shop_name is not None and shop_name != "":
            equipment.shop_name = shop_name
        if date_of_transaction is not None and date_of_transaction != "":
            equipment.date_of_transaction = date_of_transaction

        self.db.add(equipment)
        self.db.commit()
        self.db.refresh(equipment)
        return equipment

    def delete_equipment_by_id(self, equipment_id: int):
        equipment = self.db.query(Equipment).filter(
            Equipment.equipment_id == equipment_id).first()
        if equipment is None:
            raise EquipmentDoesNotExistInTheDatabaseException(
                message=f'Equipment with id {equipment_id} not in the database.',
                code=400)
        self.db.delete(equipment)
        self.db.commit()
        return True
