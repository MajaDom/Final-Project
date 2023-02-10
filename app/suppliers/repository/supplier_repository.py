from sqlalchemy.orm import Session
from app.suppliers.exceptions import *

from app.suppliers.models import Supplier


class SupplierRepository:
    def __init__(self, db: Session):
        self.db = db

    def create_supplier(self, supplier_name: str, contact: str):
        try:
            supplier = Supplier(supplier_name=supplier_name, contact=contact)
            self.db.add(supplier)
            self.db.commit()
            self.db.refresh(supplier)
            return supplier
        except Exception as e:
            raise e

    def read_all_suppliers(self) -> list[Supplier]:
        suppliers = self.db.query(Supplier).all()
        return suppliers

    def read_supplier_by_id(self, supplier_id: int) -> Supplier:
        supplier = self.db.query(Supplier).filter(Supplier.supplier_id == supplier_id).first()
        if supplier is None:
            raise SupplierDoesNotExistInTheDatabaseException(
                message=f'Supplier with id {supplier_id} not in the database.',
                code=400)
        return supplier

    def read_supplier_by_name(self, supplier_name: str) -> Supplier:
        supplier = self.db.query(Supplier).filter(Supplier.supplier_name == supplier_name).first()
        if supplier is None:
            raise SupplierDoesNotExistInTheDatabaseException(
                message=f'Supplier with name {supplier_name} not in the database.',
                code=400)
        return supplier

    def update_supplier_by_id(self, supplier_id: int, supplier_name: str = None,
                              contact: str = None) -> Supplier:
        supplier = self.db.query(Supplier).filter(Supplier.supplier_id == supplier_id).first()
        if supplier is None:
            raise SupplierDoesNotExistInTheDatabaseException(
                message=f'Supplier with id {supplier_id} not in the database.',
                code=400)
        if supplier_name is not None and supplier_name != "":
            supplier.supplier_name = supplier_name
        if contact is not None and contact != "":
            supplier.contact = contact
        self.db.add(supplier)
        self.db.commit()
        self.db.refresh(supplier)
        return supplier

    def delete_supplier_by_id(self, supplier_id: int):
        supplier = self.db.query(Supplier).filter(Supplier.supplier_id == supplier_id).first()
        if supplier is None:
            raise SupplierDoesNotExistInTheDatabaseException(
                message=f'Supplier with id {supplier_id} not in the database.',
                code=400)
        self.db.delete(supplier)
        self.db.commit()
        return True
