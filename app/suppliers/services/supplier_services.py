from app.db import SessionLocal
from app.suppliers.repository import SupplierRepository


class SupplierService:

    @staticmethod
    def create_supplier(supplier_name: str, contact: str):
        try:
            with SessionLocal() as db:
                suppliers_repository = SupplierRepository(db)
                return suppliers_repository.create_supplier(supplier_name=supplier_name, contact=contact)
        except Exception as e:
            return e

    @staticmethod
    def read_all_suppliers():
        try:
            with SessionLocal() as db:
                suppliers_repository = SupplierRepository(db)
                return suppliers_repository.read_all_suppliers()
        except Exception as e:
            raise e

    @staticmethod
    def read_cost_center_by_id(supplier_id: int):
        try:
            with SessionLocal() as db:
                suppliers_repository = SupplierRepository(db)
                return suppliers_repository.read_supplier_by_id(supplier_id=supplier_id)
        except Exception as e:
            raise e

    @staticmethod
    def read_supplier_by_name(supplier_name: str):
        try:
            with SessionLocal() as db:
                suppliers_repository = SupplierRepository(db)
                return suppliers_repository.read_supplier_by_name(supplier_name=supplier_name)
        except Exception as e:
            raise e

    @staticmethod
    def update_supplier_by_id(supplier_id: int, supplier_name: str = None, contact: str = None):
        try:
            with SessionLocal() as db:
                suppliers_repository = SupplierRepository(db)
                return suppliers_repository.update_supplier_by_id(supplier_id=supplier_id, supplier_name=supplier_name,
                                                                  contact=contact)
        except Exception as e:
            raise e

    @staticmethod
    def delete_supplier_by_id(supplier_id: int):
        try:
            with SessionLocal() as db:
                supplier_repository = SupplierRepository(db)
                return supplier_repository.delete_supplier_by_id(supplier_id=supplier_id)
        except Exception as e:
            raise e
