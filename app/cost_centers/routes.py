# Routs for cost center
from fastapi import APIRouter, Depends
from app.users.controller.user_auth_controller import JWTBearer
from app.cost_centers.controller import CostCenterController
from app.cost_centers.schemas import CostCenterSchemaIN, CostCenterSchemaUpdate, CostCenterSchema

cost_center_router = APIRouter(tags=["Cost Center"], prefix="/api/cost_center")


@cost_center_router.post("/create-new-cost-center",
                         response_model=CostCenterSchema,
                         dependencies=[Depends(JWTBearer("super_user"))])
def create_cost_center(cost_center: CostCenterSchemaIN):
    """
    - Method that creates new cost center.
    - **center_name**: mandatory field, e.g. Obilaznica Nis
    - **center_code**: mandatory field, e.g. ON
    """
    return CostCenterController.create_cost_center(center_name=cost_center.center_name,
                                                   center_code=cost_center.center_code)


@cost_center_router.get("/get-all-cost-centers", response_model=list[CostCenterSchema])
def get_all_cost_centers():
    """Method that reads all cost centers from the database."""
    return CostCenterController.get_all_cost_centers()


@cost_center_router.get("/get-cost_center-by-id", response_model=CostCenterSchema)
def get_cost_center_by_id(cost_center_id: int):
    """
    - Method that reads a cost center based on cost center id.
    - **cost_center_id**: mandatory parameter
    """
    return CostCenterController.get_cost_center_by_id(cost_center_id=cost_center_id)


@cost_center_router.get("/get-cost_center-by-code", response_model=CostCenterSchema)
def get_cost_center_by_code(center_code: str):
    """
    - Method that reads a cost center based on cost center code.
    - **center_code**: mandatory parameter
    """
    return CostCenterController.get_cost_center_by_code(center_code=center_code)


@cost_center_router.put("/update-cost_center-data",
                        response_model=CostCenterSchema,
                        dependencies=[Depends(JWTBearer("super_user"))])
def update_cost_center_by_id(cost_center_id: int, cost_center: CostCenterSchemaUpdate):
    """
    - Method that allows data updates based on cost center id. If you do not want to update all values,
    you can erase that field, and it will not be updated in teh database.
    - **cost_center_id**: mandatory parameter
    - **center_name**: not mandatory
    - **center_code**: not mandatory
    """
    return CostCenterController.update_cost_center_by_id(cost_center_id=cost_center_id,
                                                         center_name=cost_center.center_name,
                                                         center_code=cost_center.center_code)


@cost_center_router.delete("/delete-cost_center-by-id", dependencies=[Depends(JWTBearer("super_user"))])
def delete_cost_center_by_id(cost_center_id: int):
    """
    - Method that deletes cost center from the database based on cost center id.
    - **cost_center_id**: mandatory parameter
    """
    return CostCenterController.delete_cost_center_id(cost_center_id=cost_center_id)
