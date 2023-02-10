from app.suppliers.services import SupplierService
from app.suppliers.exceptions import SupplierDoesNotExistInTheDatabaseException
from fastapi import HTTPException, Response


class SupplierController:

    @staticmethod
    def create_supplier(supplier_name: str, contact: str):
        try:
            supplier = SupplierService.create_supplier(supplier_name=supplier_name, contact=contact)
            return supplier
        except Exception as e:
            raise e

    @staticmethod
    def get_all_suppliers():
        try:
            suppliers = SupplierService.read_all_suppliers()
            return suppliers
        except Exception as e:
            raise HTTPException(status_code=500, detail=f"Unprocessed error: {str(e)}")

    @staticmethod
    def get_supplier_by_id(supplier_id: int):
        try:
            supplier = SupplierService.read_cost_center_by_id(supplier_id=supplier_id)
            return supplier
        except SupplierDoesNotExistInTheDatabaseException as e:
            raise HTTPException(status_code=e.code, detail=e.message)
        except Exception as e:
            raise HTTPException(status_code=500, detail=f"Unprocessed error: {str(e)}")

    @staticmethod
    def get_supplier_by_name(supplier_name: str):  # todo check if this should be a list, or attribute name unique
        try:
            supplier = SupplierService.read_supplier_by_name(supplier_name=supplier_name)
            return supplier
        except SupplierDoesNotExistInTheDatabaseException as e:
            raise HTTPException(status_code=e.code, detail=e.message)
        except Exception as e:
            raise HTTPException(status_code=500, detail=f"Unprocessed error: {str(e)}")

    @staticmethod
    def update_supplier_by_id(supplier_id: int, supplier_name: str = None, contact: str = None):
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
        try:
            SupplierService.delete_supplier_by_id(supplier_id=supplier_id)
            return Response(content=f"Supplier with id {supplier_id} successfully deleted.")
        except SupplierDoesNotExistInTheDatabaseException as e:
            raise HTTPException(status_code=e.code, detail=e.message)
        except Exception as e:
            raise HTTPException(status_code=500, detail=f"Unprocessed error: {str(e)}")
