from app.incoming_invoices.services import IncomingInvoiceService
from app.incoming_invoices.exceptions import IncomingInvoiceDoesNotExistInTheDatabaseException
from fastapi import HTTPException, Response


class IncomingInvoiceController:

    @staticmethod
    def create_incoming_invoice(reference_code_invoice: str, number_invoice: str, invoice_date: str,
                                supplier_id: int, net: float = None, vat: float = None, gross: float = None,
                                description_invoice: str = None, cost_center_id: int = None):
        try:
            incoming_invoice = IncomingInvoiceService.create_outgoing_invoice(
                reference_code_invoice=reference_code_invoice,
                number_invoice=number_invoice, invoice_date=invoice_date,
                supplier_id=supplier_id, net=net, vat=vat,
                gross=gross, description_invoice=description_invoice,
                cost_center_id=cost_center_id)
            return incoming_invoice
        except Exception as e:
            raise e

    @staticmethod
    def get_all_incoming_invoices():
        try:
            incoming_invoices = IncomingInvoiceService.read_all_incoming_invoices()
            return incoming_invoices
        except Exception as e:
            raise HTTPException(status_code=500, detail=f"Unprocessed error: {str(e)}")

    @staticmethod
    def get_incoming_invoice_by_id(incoming_invoice_id: int):
        try:
            incoming_invoice = IncomingInvoiceService.read_incoming_invoice_by_id(
                incoming_invoice_id=incoming_invoice_id)
            return incoming_invoice
        except IncomingInvoiceDoesNotExistInTheDatabaseException as e:
            raise HTTPException(status_code=e.code, detail=e.message)
        except Exception as e:
            raise HTTPException(status_code=500, detail=f"Unprocessed error: {str(e)}")

    @staticmethod
    def update_incoming_invoices_by_id(incoming_invoice_id: int, reference_code_invoice: str = None,
                                       number_invoice: str = None, invoice_date: str = None,
                                       supplier_id: int = None, net: float = None, vat: float = None,
                                       gross: float = None,
                                       description_invoice: str = None, cost_center_id: int = None):
        try:
            incoming_invoice = IncomingInvoiceService.update_incoming_invoice_by_id(
                incoming_invoice_id=incoming_invoice_id,
                reference_code_invoice=reference_code_invoice,
                number_invoice=number_invoice, invoice_date=invoice_date,
                supplier_id=supplier_id, net=net,
                vat=vat, gross=gross,
                description_invoice=description_invoice,
                cost_center_id=cost_center_id)
            return incoming_invoice

        except IncomingInvoiceDoesNotExistInTheDatabaseException as e:
            raise HTTPException(status_code=e.code, detail=e.message)
        except Exception as e:
            raise HTTPException(status_code=500, detail=f"Unprocessed error: {str(e)}")

    @staticmethod
    def delete_incoming_invoice_by_id(incoming_invoice_id: int):
        try:
            IncomingInvoiceService.delete_incoming_invoice_by_id(incoming_invoice_id=incoming_invoice_id)
            return Response(content=f"Invoice with id {incoming_invoice_id} successfully deleted.")
        except IncomingInvoiceDoesNotExistInTheDatabaseException as e:
            raise HTTPException(status_code=e.code, detail=e.message)
        except Exception as e:
            raise HTTPException(status_code=500, detail=f"Unprocessed error: {str(e)}")

    @staticmethod
    def sum_incoming_invoices_grouped_by_suppliers():
        try:
            incoming_invoices = IncomingInvoiceService.sum_incoming_invoices_grouped_by_suppliers()
            return incoming_invoices
        except Exception as e:
            raise HTTPException(status_code=500, detail=f"Unprocessed error: {str(e)}")

    @staticmethod
    def sum_incoming_invoices_grouped_by_cost_centers():
        try:
            incoming_invoices = IncomingInvoiceService.sum_incoming_invoices_grouped_by_cost_centers()
            return incoming_invoices
        except Exception as e:
            raise HTTPException(status_code=500, detail=f"Unprocessed error: {str(e)}")

    @staticmethod
    def sum_incoming_invoices_grouped_by_years_and_months():
        try:
            incoming_invoices = IncomingInvoiceService.sum_incoming_invoices_by_years_and_months()
            return incoming_invoices
        except Exception as e:
            raise HTTPException(status_code=500, detail=f"Unprocessed error: {str(e)}")

    @staticmethod
    def find_difference_incoming_invoice_gross_and_invoice_payments():
        try:
            incoming_invoices = IncomingInvoiceService.find_difference_incoming_invoice_gross_and_invoice_payments()
            return incoming_invoices
        except Exception as e:
            raise HTTPException(status_code=500, detail=f"Unprocessed error: {str(e)}")