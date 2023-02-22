""" This class is responsible for handling all the business logic related to cost centers """
from fastapi import HTTPException, Response
from sqlalchemy.exc import IntegrityError
from app.cost_centers.services import CostCenterService
from app.cost_centers.exceptions import CostCenterNotFoundException
from app.incoming_invoices.services import IncomingInvoiceService
from app.outgoing_invoices.services import OutgoingInvoicesService


class CostCenterController:

    @staticmethod
    def create_cost_center(center_name: str, center_code: str):
        """Method that creates new cost center."""
        try:
            cost_center = CostCenterService.create_cost_center(center_name=center_name, center_code=center_code)
            return cost_center
        except IntegrityError as e:
            raise HTTPException(status_code=400, detail=str(e))
        except Exception as e:
            raise e

    @staticmethod
    def get_all_cost_centers():
        """Method that reads all cost centers from the database."""
        try:
            cost_centers = CostCenterService.read_all_cost_centers()
            return cost_centers
        except Exception as e:
            raise HTTPException(status_code=500, detail=f"Unprocessed error: {str(e)}")

    @staticmethod
    def get_cost_center_by_id(cost_center_id: int):
        """Method that reads a cost center based on cost center id."""
        try:
            cost_center = CostCenterService.read_cost_center_by_id(cost_center_id=cost_center_id)
            return cost_center
        except CostCenterNotFoundException as e:
            raise HTTPException(status_code=e.code, detail=e.message)
        except Exception as e:
            raise HTTPException(status_code=500, detail=f"Unprocessed error: {str(e)}")

    @staticmethod
    def get_cost_center_by_code(center_code: str):
        """Method that reads a cost center based on cost center code."""
        try:
            cost_center = CostCenterService.read_cost_center_by_code(center_code=center_code)
            return cost_center
        except CostCenterNotFoundException as e:
            raise HTTPException(status_code=e.code, detail=e.message)
        except Exception as e:
            raise HTTPException(status_code=500, detail=f"Unprocessed error: {str(e)}")

    @staticmethod
    def update_cost_center_by_id(cost_center_id, center_name: str = None, center_code: str = None):
        """Method that allows data updates based on cost center id."""
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
        """Method that deletes cost center from the database based on cost center id."""
        try:
            CostCenterService.delete_cost_center_by_id(cost_center_id=cost_center_id)
            return Response(content=f"Cost Center with id {cost_center_id} successfully deleted.")
        except CostCenterNotFoundException as e:
            raise HTTPException(status_code=e.code, detail=e.message)
        except Exception as e:
            raise HTTPException(status_code=500, detail=f"Unprocessed error: {str(e)}")

    @staticmethod
    def get_incoming_outgoing_invoice_difference_grouped_by_cost_centers():
        """This method is showing total difference in incoming and outgoing invoices for every cost center."""
        incoming_invoices = IncomingInvoiceService.sum_incoming_invoices_grouped_by_cost_centers()
        outgoing_invoices = OutgoingInvoicesService.sum_outgoing_invoices_grouped_by_cost_centers()
        difference = {}
        for outgoing in outgoing_invoices:
            for key, value in outgoing.items():
                difference[key] = {"Outgoing invoice": value}
            print(outgoing)
        for incoming in incoming_invoices:
            for key, value in incoming.items():
                difference[key]["Incoming invoice"] = value
        for item in difference:
            difference[item]["Difference"] = difference[item]["Outgoing invoice"] - difference[item]["Incoming invoice"]
        return difference
