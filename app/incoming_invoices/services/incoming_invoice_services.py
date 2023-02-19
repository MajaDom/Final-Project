from app.db import SessionLocal
from app.incoming_invoices.repository import IncomingInvoiceRepository


class IncomingInvoiceService:

    @staticmethod
    def create_outgoing_invoice(reference_code_invoice: str, number_invoice: str, invoice_date: str,
                                supplier_id: int, net: float = None, vat: float = None, gross: float = None,
                                description_invoice: str = None, cost_center_id: int = None):
        try:
            with SessionLocal() as db:
                incoming_invoice_repository = IncomingInvoiceRepository(db)
                return incoming_invoice_repository.create_incoming_invoices(
                    reference_code_invoice=reference_code_invoice,
                    number_invoice=number_invoice, invoice_date=invoice_date, net=net,
                    vat=vat, gross=gross, description_invoice=description_invoice,
                    supplier_id=supplier_id, cost_center_id=cost_center_id)
        except Exception as e:
            return e

    @staticmethod
    def read_all_incoming_invoices():
        try:
            with SessionLocal() as db:
                incoming_invoices = IncomingInvoiceRepository(db)
                return incoming_invoices.read_all_incoming_invoices()
        except Exception as e:
            raise e

    @staticmethod
    def read_incoming_invoice_by_id(incoming_invoice_id: int):
        try:
            with SessionLocal() as db:
                incoming_invoice_repository = IncomingInvoiceRepository(db)
                return incoming_invoice_repository.read_incoming_invoice_by_id(incoming_invoice_id=incoming_invoice_id)
        except Exception as e:
            raise e

    @staticmethod
    def update_incoming_invoice_by_id(incoming_invoice_id: int, reference_code_invoice: str = None,
                                      number_invoice: str = None, invoice_date: str = None,
                                      supplier_id: int = None, net: float = None, vat: float = None,
                                      gross: float = None,
                                      description_invoice: str = None, cost_center_id: int = None):
        try:
            with SessionLocal() as db:
                incoming_invoice_repository = IncomingInvoiceRepository(db)
                return incoming_invoice_repository.update_incoming_invoice_by_id(
                    incoming_invoice_id=incoming_invoice_id, reference_code_invoice=reference_code_invoice,
                    number_invoice=number_invoice, invoice_date=invoice_date, supplier_id=supplier_id, net=net,
                    vat=vat, gross=gross, description_invoice=description_invoice, cost_center_id=cost_center_id)
        except Exception as e:
            raise e

    @staticmethod
    def delete_incoming_invoice_by_id(incoming_invoice_id: int):
        try:
            with SessionLocal() as db:
                incoming_invoice_repository = IncomingInvoiceRepository(db)
                return incoming_invoice_repository.delete_incoming_invoice_by_id(
                    incoming_invoice_id=incoming_invoice_id)
        except Exception as e:
            raise e

    @staticmethod
    def sum_incoming_invoices_grouped_by_suppliers():
        try:
            with SessionLocal() as db:
                incoming_invoices = IncomingInvoiceRepository(db)
                return incoming_invoices.sum_incoming_invoices_grouped_by_suppliers()
        except Exception as e:
            raise e

    @staticmethod
    def sum_incoming_invoices_grouped_by_cost_centers():
        try:
            with SessionLocal() as db:
                incoming_invoices = IncomingInvoiceRepository(db)
                return incoming_invoices.sum_incoming_invoices_grouped_by_cost_center()
        except Exception as e:
            raise e

    @staticmethod
    def sum_incoming_invoices_by_years_and_months():
        try:
            with SessionLocal() as db:
                incoming_invoices = IncomingInvoiceRepository(db)
                return incoming_invoices.sum_incoming_invoices_by_years_and_months()
        except Exception as e:
            raise e
