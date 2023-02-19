from datetime import datetime

from sqlalchemy.orm import Session
from sqlalchemy.exc import IntegrityError, NoForeignKeysError
from app.equipment.models import AssignedEquipment
from app.equipment.exceptions import *


class AssignedEquipmentRepository:
    def __init__(self, db: Session):
        self.db = db

    def create_new_assigned_equipment(self, start_date: str, id_employee: int, equipment_id: int,
                                      end_date: str = None) -> AssignedEquipment:

        try:
            assigned_equipment = AssignedEquipment(start_date=start_date, end_date=end_date, id_employee=id_employee,
                                                   equipment_id=equipment_id)
            self.db.add(assigned_equipment)
            self.db.commit()
            self.db.refresh(assigned_equipment)
            return assigned_equipment
        except IntegrityError as e:
            raise e
        except NoForeignKeysError as e:
            raise e
        except Exception as e:
            raise e

    def read_all_history_of_assigned_equipment(self) -> list[AssignedEquipment]:
        assigned_equipment = self.db.query(AssignedEquipment).filter(AssignedEquipment.end_date is not None).all()
        return assigned_equipment

    def read_all_currently_assigned_equipment(self) -> list[AssignedEquipment]:
        assigned_equipment = self.db.query(AssignedEquipment).filter(AssignedEquipment.end_date is None).all()
        return assigned_equipment

    def read_currently_assigned_equipment_by_id(self, assigned_equipment_id: int) -> AssignedEquipment:
        assigned_equipment = self.db.query(AssignedEquipment).filter(
            AssignedEquipment.assigned_equipment_id == assigned_equipment_id,
            AssignedEquipment.end_date is None).first()
        if assigned_equipment is None:
            raise AssignedEquipmentDoesNotExistInTheDatabaseException(
                message=f'Assigned Equipment with id {assigned_equipment_id} does not exist in the database.',
                code=400)
        return assigned_equipment

    def read_currently_assigned_equipment_from_employee_by_id(self, employee_id: int) -> list[AssignedEquipment]:
        assigned_equipment = self.db.query(AssignedEquipment).filter(
            AssignedEquipment.id_employee == employee_id, AssignedEquipment.end_date == None).all()
        if assigned_equipment is None:
            raise AssignedEquipmentDoesNotExistInTheDatabaseException(
                message=f'Employee with id {employee_id} does not have assigned equipment.',
                code=400)
        return assigned_equipment

    def update_assigned_equipment_by_id(self, assigned_equipment_id: int, start_date: str = None, end_date: str = None,
                                        id_employee: int = None, equipment_id: int = None) -> AssignedEquipment:
        assigned_equipment = self.db.query(AssignedEquipment).filter(
            AssignedEquipment.assigned_equipment_id == assigned_equipment_id).first()

        if assigned_equipment is None:
            raise AssignedEquipmentDoesNotExistInTheDatabaseException(
                message=f'Equipment with id {equipment_id} has never been assigned.',
                code=400)
        if start_date is not None and start_date != "":
            try:
                datetime.strptime(start_date, "%Y-%m-%d")
                assigned_equipment.start_date = start_date
            except Exception:
                raise NotAValidDateInputException(message="Not a valid date format.", code=400)
        if end_date is not None and end_date != "":
            try:
                datetime.strptime(end_date, "%Y-%m-%d")
                assigned_equipment.end_date = end_date
            except Exception:
                raise NotAValidDateInputException(message="Not a valid date format.", code=400)
        if id_employee is not None and id_employee != "":
            assigned_equipment.id_employee = id_employee
        if equipment_id is not None and equipment_id != "":
            assigned_equipment.equipment_id = equipment_id

        self.db.add(assigned_equipment)
        self.db.commit()
        self.db.refresh(assigned_equipment)
        return assigned_equipment

    def delete_assigned_equipment_by_id(self, assigned_equipment_id: int):
        assigned_equipment = self.db.query(AssignedEquipment).filter(
            AssignedEquipment.assigned_equipment_id == assigned_equipment_id).first()
        if assigned_equipment is None:
            raise EquipmentDoesNotExistInTheDatabaseException(
                message=f'Assigned Equipment with id {assigned_equipment_id} not in the database.',
                code=400)
        self.db.delete(assigned_equipment)
        self.db.commit()
        return True
