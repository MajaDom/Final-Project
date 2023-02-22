# It's a class that contains methods that allow us to perform CRUD operations on the cost center table
from app.db import SessionLocal
from app.cost_centers.repository import CostCenterRepository


class CostCenterService:

    @staticmethod
    def create_cost_center(center_name: str, center_code: str):
        """Method that creates new cost center."""
        try:
            with SessionLocal() as db:
                cost_center_repository = CostCenterRepository(db)
                return cost_center_repository.create_cost_center(center_code=center_code, center_name=center_name)
        except Exception as e:
            raise e

    @staticmethod
    def read_all_cost_centers():
        """Method that reads all cost centers from the database."""
        try:
            with SessionLocal() as db:
                cost_center_repository = CostCenterRepository(db)
                return cost_center_repository.read_all_cost_centers()
        except Exception as e:
            raise e

    @staticmethod
    def read_cost_center_by_id(cost_center_id: int):
        """Method that reads a cost center based on cost center id."""
        try:
            with SessionLocal() as db:
                cost_center_repository = CostCenterRepository(db)
                return cost_center_repository.read_cost_centers_by_id(cost_center_id=cost_center_id)
        except Exception as e:
            raise e

    @staticmethod
    def read_cost_center_by_code(center_code: str):
        """Method that reads a cost center based on cost center code."""
        try:
            with SessionLocal() as db:
                cost_center_repository = CostCenterRepository(db)
                return cost_center_repository.read_cost_center_by_code(center_code=center_code)
        except Exception as e:
            raise e

    @staticmethod
    def update_cost_center_by_id(cost_center_id: int, center_name: str = None, center_code: str = None):
        """Method that allows data updates based on cost center id."""
        try:
            with SessionLocal() as db:
                cost_center_repository = CostCenterRepository(db)
                return cost_center_repository.update_cost_center_by_id(cost_center_id=cost_center_id,
                                                                       center_name=center_name,
                                                                       center_code=center_code)
        except Exception as e:
            raise e

    @staticmethod
    def delete_cost_center_by_id(cost_center_id: int):
        """Method that deletes cost center from the database based on cost center id."""
        try:
            with SessionLocal() as db:
                cost_center_repository = CostCenterRepository(db)
                return cost_center_repository.delete_cost_center_by_id(cost_center_id=cost_center_id)
        except Exception as e:
            raise e
