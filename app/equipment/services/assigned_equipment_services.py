from app.db import SessionLocal
from app.equipment.repository import AssignedEquipmentRepository
from app.equipment.exceptions import EquipmentHasBeenAssignedException, AssignedEquipmentDoesNotExistInTheDatabaseException


class AssignedEquipmentService:

    @staticmethod
    def create_assigned_equipment(start_date: str, id_employee: int, equipment_id: int,
                                  end_date: str = None):
        """Method that creates new assigned equipment."""
        try:
            with SessionLocal() as db:
                assigned_equipment_repository = AssignedEquipmentRepository(db)
                check_availability = assigned_equipment_repository.read_currently_assigned_equipment_by_id(equipment_id)
                if check_availability:
                    raise EquipmentHasBeenAssignedException(code=400,
                                                            message=f"Equipment with id {equipment_id} is currently "
                                                                    f"assigned")
                return assigned_equipment_repository.create_new_assigned_equipment(start_date=start_date,
                                                                                   id_employee=id_employee,
                                                                                   equipment_id=equipment_id,
                                                                                   end_date=end_date)
        except Exception as e:
            raise e

    @staticmethod
    def read_all_history_of_assigned_equipment():
        """Method that reads all assigned equipment in the database"""
        try:
            with SessionLocal() as db:
                assigned_equipment = AssignedEquipmentRepository(db)
                return assigned_equipment.read_all_history_of_assigned_equipment()
        except Exception as e:
            raise e

    @staticmethod
    def read_all_currently_assigned_equipment():
        """Method that reads all currently assigned equipment in the database"""
        try:
            with SessionLocal() as db:
                assigned_equipment_repository = AssignedEquipmentRepository(db)
                return assigned_equipment_repository.read_all_currently_assigned_equipment()
        except Exception as e:
            raise e

    @staticmethod
    def read_currently_assigned_equipment_by_id(equipment_id: int):
        """Read if equipment is currently assigned"""
        try:
            with SessionLocal() as db:
                assigned_equipment_repository = AssignedEquipmentRepository(db)
                assigned_equipment = assigned_equipment_repository.read_currently_assigned_equipment_by_id(equipment_id)
                if not assigned_equipment:
                    raise AssignedEquipmentDoesNotExistInTheDatabaseException(
                        message=f'Equipment with id {equipment_id} is not assigned.',
                        code=400)
                return assigned_equipment_repository.read_currently_assigned_equipment_by_id(
                    equipment_id=equipment_id)
        except Exception as e:
            raise e

    @staticmethod
    def read_currently_assigned_equipment_from_employee_by_id(employee_id: int):
        """Read if there is any assigned equipment for certain employee"""
        try:
            with SessionLocal() as db:
                assigned_equipment_repository = AssignedEquipmentRepository(db)
                return assigned_equipment_repository.read_currently_assigned_equipment_from_employee_by_id(
                    employee_id=employee_id)
        except Exception as e:
            raise e

    @staticmethod
    def update_assigned_equipment_by_id(assigned_equipment_id: int, start_date: str = None, end_date: str = None,
                                        id_employee: int = None, equipment_id: int = None):
        """Method that updates values existing assigned equipment."""
        try:
            with SessionLocal() as db:
                assigned_equipment_repository = AssignedEquipmentRepository(db)
                return assigned_equipment_repository.update_assigned_equipment_by_id(
                    assigned_equipment_id=assigned_equipment_id,
                    start_date=start_date, end_date=end_date,
                    id_employee=id_employee, equipment_id=equipment_id)
        except Exception as e:
            raise e

    @staticmethod
    def delete_assigned_equipment_by_id(assigned_equipment_id: int):
        """Method that deletes assigned equipment."""
        try:
            with SessionLocal() as db:
                assigned_equipment_repository = AssignedEquipmentRepository(db)
                return assigned_equipment_repository.delete_assigned_equipment_by_id(
                    assigned_equipment_id=assigned_equipment_id)
        except Exception as e:
            raise e
