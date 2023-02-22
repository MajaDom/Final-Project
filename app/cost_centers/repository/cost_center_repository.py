# This class is a repository class that contains all the methods that
# are used to interact with the cost center table in the database
from sqlalchemy.orm import Session
from sqlalchemy.exc import IntegrityError
from app.cost_centers.models import CostCenter
from app.cost_centers.exceptions import CostCenterNotFoundException


class CostCenterRepository:
    def __init__(self, db: Session):
        self.db = db

    def create_cost_center(self, center_code: str, center_name: str) -> CostCenter:
        """Method that creates new cost center."""
        try:
            cost_center = CostCenter(center_code=center_code, center_name=center_name)
            self.db.add(cost_center)
            self.db.commit()
            self.db.refresh(cost_center)
            return cost_center
        except IntegrityError as e:
            raise e
        except Exception as e:
            raise e

    def read_all_cost_centers(self) -> list[CostCenter]:
        """Method that reads all cost centers from the database."""
        cost_centers = self.db.query(CostCenter).all()
        return cost_centers

    def read_cost_centers_by_id(self, cost_center_id: int) -> CostCenter:
        """Method that reads a cost center based on cost center id."""
        cost_center = self.db.query(CostCenter).filter(CostCenter.cost_center_id == cost_center_id).first()
        if cost_center is None:
            raise CostCenterNotFoundException(message=f'Cost Center with id {cost_center_id} not in the database.',
                                              code=400)
        return cost_center

    def read_cost_center_by_code(self, center_code: str) -> CostCenter:
        """Method that reads a cost center based on cost center code."""
        cost_center = self.db.query(CostCenter).filter(CostCenter.center_code == center_code).first()
        if cost_center is None:
            raise CostCenterNotFoundException(message=f'Cost Center with code {center_code} not in the database.',
                                              code=400)
        return cost_center

    def update_cost_center_by_id(self, cost_center_id: int, center_name: str = None,
                                 center_code: str = None) -> CostCenter:
        """Method that allows data updates based on cost center id."""
        cost_center = self.db.query(CostCenter).filter(CostCenter.cost_center_id == cost_center_id).first()
        if cost_center is None:
            raise CostCenterNotFoundException(message=f'Cost Center with id {cost_center_id} not in the database.',
                                              code=400)
        if center_name is not None and center_name != "":
            cost_center.center_name = center_name
        if center_code is not None and center_code != "":
            cost_center.center_code = center_code
        self.db.add(cost_center)
        self.db.commit()
        self.db.refresh(cost_center)
        return cost_center

    def delete_cost_center_by_id(self, cost_center_id: int) -> bool:
        """Method that deletes cost center from the database based on cost center id."""
        cost_center = self.db.query(CostCenter).filter(CostCenter.cost_center_id == cost_center_id).first()
        if cost_center is None:
            raise CostCenterNotFoundException(message=f'Cost Center with id {cost_center_id} not in the database.',
                                              code=400)
        self.db.delete(cost_center)
        self.db.commit()
        return True
