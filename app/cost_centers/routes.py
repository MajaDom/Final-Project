from fastapi import APIRouter
from app.cost_centers.controller import CostCenterController
from app.cost_centers.schemas import CostCenterSchemaIN, CostCenterSchemaUpdate, CostCenterSchema

cost_center_router = APIRouter(tags=["Cost Center"], prefix="/api/cost_center")


@cost_center_router.post("/create-new-cost-center", response_model=CostCenterSchema)
def create_cost_center(cost_center: CostCenterSchemaIN):
    return CostCenterController.create_cost_center(center_name=cost_center.center_name,
                                                   center_code=cost_center.center_code)


@cost_center_router.get("/get-all-cost-centers", response_model=list[CostCenterSchema])
def get_all_cost_centers():
    return CostCenterController.get_all_cost_centers()


@cost_center_router.get("/get-cost_center-by-id", response_model=CostCenterSchema)
def get_cost_center_by_id(cost_center_id: int):
    return CostCenterController.get_cost_center_by_id(cost_center_id=cost_center_id)


@cost_center_router.get("/get-cost_center-by-name", response_model=CostCenterSchema)
def get_cost_center_by_name(center_name: str):
    return CostCenterController.get_cost_center_by_name(center_name=center_name)


@cost_center_router.put("/update-cost_center-data", response_model=CostCenterSchema)
def update_cost_center_by_id(cost_center_id: int, cost_center: CostCenterSchemaUpdate):
    return CostCenterController.update_cost_center_by_id(cost_center_id=cost_center_id,
                                                         center_name=cost_center.center_name,
                                                         center_code=cost_center.center_code)


@cost_center_router.delete("/delete-cost_center-by-id")
def delete_cost_center_by_id(cost_center_id: int):
    return CostCenterController.delete_cost_center_id(cost_center_id)
