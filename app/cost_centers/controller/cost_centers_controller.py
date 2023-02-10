from app.cost_centers.services import CostCenterService
from app.cost_centers.exceptions import CostCenterNotFoundException
from fastapi import HTTPException, Response


class CostCenterController:

    @staticmethod
    def create_cost_center(center_name: str, center_code: str):
        try:
            cost_center = CostCenterService.create_cost_center(center_name=center_name, center_code=center_code)
            return cost_center
        except Exception as e:
            raise e

    @staticmethod
    def get_all_cost_centers():
        try:
            cost_centers = CostCenterService.read_all_cost_centers()
            return cost_centers
        except Exception as e:
            raise HTTPException(status_code=500, detail=f"Unprocessed error: {str(e)}")

    @staticmethod
    def get_cost_center_by_id(cost_center_id: int):
        try:
            cost_center = CostCenterService.read_cost_center_by_id(cost_center_id=cost_center_id)
            return cost_center
        except CostCenterNotFoundException as e:
            raise HTTPException(status_code=e.code, detail=e.message)
        except Exception as e:
            raise HTTPException(status_code=500, detail=f"Unprocessed error: {str(e)}")

    @staticmethod
    def get_cost_center_by_name(center_name: str):  # todo check if this should be a list, or attribute name unique
        try:
            cost_center = CostCenterService.read_cost_center_by_name(center_name=center_name)
            return cost_center
        except CostCenterNotFoundException as e:
            raise HTTPException(status_code=e.code, detail=e.message)
        except Exception as e:
            raise HTTPException(status_code=500, detail=f"Unprocessed error: {str(e)}")

    @staticmethod
    def update_cost_center_by_id(cost_center_id, center_name: str = None, center_code: str = None):
        try:
            cost_center = CostCenterService.update_cost_center_by_id(cost_center_id=cost_center_id,
                                                                     center_name=center_name, center_code=center_code)
            return cost_center
        except CostCenterNotFoundException as e:
            raise HTTPException(status_code=e.code, detail=e.message)
        except Exception as e:
            raise HTTPException(status_code=500, detail=f"Unprocessed error: {str(e)}")

    @staticmethod
    def delete_cost_center_id(cost_center_id: int):
        try:
            CostCenterService.delete_cost_center_by_id(cost_center_id=cost_center_id)
            return Response(content=f"Cost Center with id {cost_center_id} successfully deleted.")
        except CostCenterNotFoundException as e:
            raise HTTPException(status_code=e.code, detail=e.message)
        except Exception as e:
            raise HTTPException(status_code=500, detail=f"Unprocessed error: {str(e)}")
