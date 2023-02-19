from app.db import SessionLocal
from app.equipment.repository import AssignedEquipmentRepository, EquipmentRepository
from app.equipment.exceptions import EquipmentDoesNotExistInTheDatabaseException


class AssignedEquipmentService:

    @staticmethod
    def create_assigned_equipment(start_date: str, id_employee: int, equipment_id: int,
                                  end_date: str = None):
        try:

            with SessionLocal() as db:
                assigned_equipment_repository = AssignedEquipmentRepository(db)
                return assigned_equipment_repository.create_new_assigned_equipment(start_date=start_date,
                                                                                   id_employee=id_employee,
                                                                                   equipment_id=equipment_id,
                                                                                   end_date=end_date)
        except Exception as e:
            return e

    @staticmethod
    def read_all_history_of_assigned_equipment():
        try:
            with SessionLocal() as db:
                assigned_equipment = AssignedEquipmentRepository(db)
                return assigned_equipment.read_all_history_of_assigned_equipment()
        except Exception as e:
            raise e

    @staticmethod
    def read_all_currently_assigned_equipment():
        try:
            with SessionLocal() as db:
                assigned_equipment_repository = AssignedEquipmentRepository(db)
                return assigned_equipment_repository.read_all_currently_assigned_equipment()
        except Exception as e:
            raise e

    @staticmethod
    def read_currently_assigned_equipment_by_id(assigned_equipment_id: int):
        try:
            with SessionLocal() as db:
                assigned_equipment_repository = AssignedEquipmentRepository(db)
                return assigned_equipment_repository.read_currently_assigned_equipment_by_id(
                    assigned_equipment_id=assigned_equipment_id)
        except Exception as e:
            raise e

    @staticmethod
    def read_currently_assigned_equipment_from_employee_by_id(employee_id: int):
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
        try:
            with SessionLocal() as db:
                assigned_equipment_repository = AssignedEquipmentRepository(db)
                return assigned_equipment_repository.delete_assigned_equipment_by_id(
                    assigned_equipment_id=assigned_equipment_id)
        except Exception as e:
            raise e
