from fastapi import HTTPException, Response
from sqlalchemy.exc import IntegrityError
from app.suppliers.services import SupplierService
from app.suppliers.exceptions import SupplierDoesNotExistInTheDatabaseException


class SupplierController:

    @staticmethod
    def create_supplier(supplier_name: str, contact: str):
        """Method that creates new suppliers in the database."""
        try:
            supplier = SupplierService.create_supplier(supplier_name=supplier_name, contact=contact)
            return supplier
        except IntegrityError as e:
            raise HTTPException(status_code=400, detail=str(e))
        except Exception as e:
            raise e

    @staticmethod
    def get_all_suppliers():
        """Method that reads all suppliers from the database."""
        try:
            suppliers = SupplierService.read_all_suppliers()
            return suppliers
        except Exception as e:
            raise HTTPException(status_code=500, detail=f"Unprocessed error: {str(e)}")

    @staticmethod
    def get_supplier_by_id(supplier_id: int):
        """Method that reads a supplier based on supplier id."""
        try:
            supplier = SupplierService.read_cost_center_by_id(supplier_id=supplier_id)
            return supplier
        except SupplierDoesNotExistInTheDatabaseException as e:
            raise HTTPException(status_code=e.code, detail=e.message)
        except Exception as e:
            raise HTTPException(status_code=500, detail=f"Unprocessed error: {str(e)}")

    @staticmethod
    def get_supplier_by_name(supplier_name: str):
        """Method that reads a supplier based on supplier name."""
        try:
            supplier = SupplierService.read_supplier_by_name(supplier_name=supplier_name)
            return supplier
        except SupplierDoesNotExistInTheDatabaseException as e:
            raise HTTPException(status_code=e.code, detail=e.message)
        except Exception as e:
            raise HTTPException(status_code=500, detail=f"Unprocessed error: {str(e)}")

    @staticmethod
    def update_supplier_by_id(supplier_id: int, supplier_name: str = None, contact: str = None):
        """Method that allows data update of supplier whose id has been provided."""
        try:
            supplier = SupplierService.update_supplier_by_id(supplier_id=supplier_id, supplier_name=supplier_name,
                                                             contact=contact)
            return supplier
        except SupplierDoesNotExistInTheDatabaseException as e:
            raise HTTPException(status_code=e.code, detail=e.message)
        except Exception as e:
            raise HTTPException(status_code=500, detail=f"Unprocessed error: {str(e)}")

    @staticmethod
    def delete_supplier_id(supplier_id: int):
        """Method that deletes supplier from the database whose id has been provided."""
        try:
            SupplierService.delete_supplier_by_id(supplier_id=supplier_id)
            return Response(content=f"Supplier with id {supplier_id} successfully deleted.")
        except SupplierDoesNotExistInTheDatabaseException as e:
            raise HTTPException(status_code=e.code, detail=e.message)
        except Exception as e:
            raise HTTPException(status_code=500, detail=f"Unprocessed error: {str(e)}")
