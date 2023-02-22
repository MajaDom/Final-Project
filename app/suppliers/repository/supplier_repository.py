# It's a class that contains methods that allow you to perform CRUD operations on the suppliers table in the database
from sqlalchemy.exc import IntegrityError
from sqlalchemy.orm import Session
from app.suppliers.exceptions import *
from app.suppliers.models import Supplier


class SupplierRepository:
    def __init__(self, db: Session):
        self.db = db

    def create_supplier(self, supplier_name: str, contact: str) -> Supplier:
        """Method that creates new suppliers in the database."""
        try:
            supplier = Supplier(supplier_name=supplier_name, contact=contact)
            self.db.add(supplier)
            self.db.commit()
            self.db.refresh(supplier)
            return supplier
        except IntegrityError as e:
            raise e
        except Exception as e:
            raise e

    def read_all_suppliers(self) -> list[Supplier]:
        """Method that reads all suppliers from the database."""
        suppliers = self.db.query(Supplier).all()
        return suppliers

    def read_supplier_by_id(self, supplier_id: int) -> Supplier:
        """Method that reads a supplier based on supplier id."""
        supplier = self.db.query(Supplier).filter(Supplier.supplier_id == supplier_id).first()
        if supplier is None:
            raise SupplierDoesNotExistInTheDatabaseException(
                message=f'Supplier with id {supplier_id} not in the database.',
                code=400)
        return supplier

    def read_supplier_by_name(self, supplier_name: str) -> Supplier:
        """Method that reads a supplier based on supplier name."""
        supplier = self.db.query(Supplier).filter(Supplier.supplier_name == supplier_name).first()
        if supplier is None:
            raise SupplierDoesNotExistInTheDatabaseException(
                message=f'Supplier with name {supplier_name} not in the database.',
                code=400)
        return supplier

    def update_supplier_by_id(self, supplier_id: int, supplier_name: str = None, contact: str = None) -> Supplier:
        """Method that allows data update of supplier whose id has been provided."""
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

    def delete_supplier_by_id(self, supplier_id: int) -> bool:
        """Method that deletes supplier from the database whose id has been provided."""
        supplier = self.db.query(Supplier).filter(Supplier.supplier_id == supplier_id).first()
        if supplier is None:
            raise SupplierDoesNotExistInTheDatabaseException(
                message=f'Supplier with id {supplier_id} not in the database.',
                code=400)
        self.db.delete(supplier)
        self.db.commit()
        return True
