from app.equipment.services import AssignedEquipmentService
from app.equipment.exceptions import AssignedEquipmentDoesNotExistInTheDatabaseException, \
    EquipmentHasBeenAssignedException, InvalidInputException
from fastapi import HTTPException, Response


class AssignedEquipmentController:

    @staticmethod
    def create_assigned_equipment(start_date: str, id_employee: int, equipment_id: int,
                                  end_date: str = None):
        """Method that creates new assigned equipment."""
        try:
            assigned_equipment = AssignedEquipmentService.create_assigned_equipment(start_date=start_date,
                                                                                    id_employee=id_employee,
                                                                                    equipment_id=equipment_id,
                                                                                    end_date=end_date)
            return assigned_equipment
        except InvalidInputException as e:
            raise HTTPException(status_code=e.code, detail=e.message)
        except AssignedEquipmentDoesNotExistInTheDatabaseException as e:
            raise HTTPException(status_code=e.code, detail=e.message)
        except EquipmentHasBeenAssignedException as e:
            raise HTTPException(status_code=e.code, detail=e.message)
        except Exception as e:
            raise HTTPException(status_code=500, detail=str(e))

    @staticmethod
    def read_all_history_of_assigned_equipment():
        """Method that reads all assigned equipment in the database."""
        try:
            assigned_equipment = AssignedEquipmentService.read_all_history_of_assigned_equipment()
            return assigned_equipment
        except Exception as e:
            raise HTTPException(status_code=500, detail=f"Unprocessed error: {str(e)}")

    @staticmethod
    def read_all_currently_assigned_equipment():
        """Method that reads all currently assigned equipment in the database."""
        try:
            assigned_equipment = AssignedEquipmentService.read_all_currently_assigned_equipment()
            return assigned_equipment
        except Exception as e:
            raise HTTPException(status_code=500, detail=f"Unprocessed error: {str(e)}")

    @staticmethod
    def read_currently_assigned_equipment_by_id(equipment_id: int):
        """Read if equipment is currently assigned"""
        try:
            assigned_equipment = AssignedEquipmentService.read_currently_assigned_equipment_by_id(
                equipment_id=equipment_id)
            return assigned_equipment
        except AssignedEquipmentDoesNotExistInTheDatabaseException as e:
            raise HTTPException(status_code=e.code, detail=e.message)
        except Exception as e:
            raise HTTPException(status_code=500, detail=f"Unprocessed error: {str(e)}")

    @staticmethod
    def read_currently_assigned_equipment_from_employee_by_id(employee_id: int):
        """Read if there is any assigned equipment for certain employee"""
        try:
            assigned_equipment = AssignedEquipmentService.read_currently_assigned_equipment_from_employee_by_id(
                employee_id=employee_id)
            return assigned_equipment
        except AssignedEquipmentDoesNotExistInTheDatabaseException as e:
            raise HTTPException(status_code=e.code, detail=e.message)
        except Exception as e:
            raise HTTPException(status_code=500, detail=f"Unprocessed error: {str(e)}")

    @staticmethod
    def update_equipment_by_id(assigned_equipment_id: int, start_date: str = None, end_date: str = None,
                               id_employee: int = None, equipment_id: int = None):
        """Method that updates values existing assigned equipment."""
        try:
            assigned_equipment = AssignedEquipmentService.update_assigned_equipment_by_id(
                assigned_equipment_id=assigned_equipment_id,
                start_date=start_date, end_date=end_date,
                id_employee=id_employee, equipment_id=equipment_id)
            return assigned_equipment
        except AssignedEquipmentDoesNotExistInTheDatabaseException as e:
            raise HTTPException(status_code=e.code, detail=e.message)
        except Exception as e:
            raise HTTPException(status_code=500, detail=f"Unprocessed error: {str(e)}")

    @staticmethod
    def delete_assigned_equipment_by_id(assigned_equipment_id: int):
        """Method that deletes assigned equipment."""
        try:
            AssignedEquipmentService.delete_assigned_equipment_by_id(assigned_equipment_id=assigned_equipment_id)
            return Response(content=f"Assigned Equipment with id {assigned_equipment_id} successfully deleted.")
        except AssignedEquipmentDoesNotExistInTheDatabaseException as e:
            raise HTTPException(status_code=e.code, detail=e.message)
        except Exception as e:
            raise HTTPException(status_code=500, detail=f"Unprocessed error: {str(e)}")
