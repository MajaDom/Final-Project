from app.outgoing_invoices.services import OutgoingInvoicesService
from app.outgoing_invoices.exceptions import OutgoingInvoiceDoesNotExistInTheDatabaseException
from fastapi import HTTPException, Response


class OutgoingInvoiceController:

    @staticmethod
    def create_outgoing_invoice(client_id: int, reference_code_invoice: str, start_date: str, date_of_transaction: str,
                                certified_invoice: str, net: float = None, vat: float = None, gross: float = None,
                                description_invoice: str = None, cost_center_id: int = None):
        try:
            outgoing_invoice = OutgoingInvoicesService.create_outgoing_invoice(
                reference_code_invoice=reference_code_invoice, client_id=client_id,
                start_date=start_date, date_of_transaction=date_of_transaction,
                certified_invoice=certified_invoice,
                net=net, vat=vat, gross=gross,
                description_invoice=description_invoice,
                cost_center_id=cost_center_id)
            return outgoing_invoice
        except Exception as e:
            raise e

    @staticmethod
    def get_all_outgoing_invoices():
        try:
            outgoing_invoices = OutgoingInvoicesService.read_all_outgoing_invoices()
            return outgoing_invoices
        except Exception as e:
            raise HTTPException(status_code=500, detail=f"Unprocessed error: {str(e)}")

    @staticmethod
    def get_outgoing_invoice_by_id(outgoing_invoice_id: int):
        try:
            outgoing_invoice = OutgoingInvoicesService.read_outgoing_invoice_by_id(
                outgoing_invoice_id=outgoing_invoice_id)
            return outgoing_invoice
        except OutgoingInvoiceDoesNotExistInTheDatabaseException as e:
            raise HTTPException(status_code=e.code, detail=e.message)
        except Exception as e:
            raise HTTPException(status_code=500, detail=f"Unprocessed error: {str(e)}")

    @staticmethod
    def update_outgoing_invoices_by_id(outgoing_invoice_id: int, client_id: int = None,
                                       reference_code_invoice: str = None,
                                       start_date: str = None, date_of_transaction: str = None,
                                       certified_invoice: str = None, net: float = None, vat: float = None,
                                       gross: float = None,
                                       description_invoice: str = None, cost_center_id: int = None):
        try:
            outgoing_invoice = OutgoingInvoicesService.update_outgoing_invoice_by_id(
                outgoing_invoice_id=outgoing_invoice_id,
                client_id=client_id, reference_code_invoice=reference_code_invoice,
                start_date=start_date, date_of_transaction=date_of_transaction,
                certified_invoice=certified_invoice, net=net, vat=vat,
                gross=gross, description_invoice=description_invoice, cost_center_id=cost_center_id)
            return outgoing_invoice
        except OutgoingInvoiceDoesNotExistInTheDatabaseException as e:
            raise HTTPException(status_code=e.code, detail=e.message)
        except Exception as e:
            raise HTTPException(status_code=500, detail=f"Unprocessed error: {str(e)}")

    @staticmethod
    def delete_outgoing_invoice_by_id(outgoing_invoice_id):
        try:
            OutgoingInvoicesService.delete_outgoing_invoice_by_id(outgoing_invoice_id=outgoing_invoice_id)
            return Response(content=f"Invoice with id {outgoing_invoice_id} successfully deleted.")
        except OutgoingInvoiceDoesNotExistInTheDatabaseException as e:
            raise HTTPException(status_code=e.code, detail=e.message)
        except Exception as e:
            raise HTTPException(status_code=500, detail=f"Unprocessed error: {str(e)}")

    @staticmethod
    def sum_outgoing_invoices_grouped_by_clients():
        try:
            outgoing_invoices = OutgoingInvoicesService.sum_outgoing_invoices_grouped_by_clients()
            return outgoing_invoices
        except Exception as e:
            raise HTTPException(status_code=500, detail=f"Unprocessed error: {str(e)}")

    @staticmethod
    def sum_outgoing_invoices_grouped_by_cost_centers():
        try:
            outgoing_invoices = OutgoingInvoicesService.sum_outgoing_invoices_grouped_by_cost_centers()
            return outgoing_invoices
        except Exception as e:
            raise HTTPException(status_code=500, detail=f"Unprocessed error: {str(e)}")

    @staticmethod
    def sum_outgoing_invoices_grouped_by_years_and_months():
        try:
            outgoing_invoices = OutgoingInvoicesService.sum_outgoing_invoices_by_years_and_months()
            return outgoing_invoices
        except Exception as e:
            raise HTTPException(status_code=500, detail=f"Unprocessed error: {str(e)}")