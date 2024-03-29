# It's a class that contains methods that are used to create, read, update and delete incoming invoices
from app.db import SessionLocal
from app.incoming_invoices.repository import IncomingInvoiceRepository, IncomingInvoicePaymentRepository


class IncomingInvoiceService:

    @staticmethod
    def create_outgoing_invoice(reference_code_invoice: str, number_invoice: str, invoice_date: str,
                                supplier_id: int, net: float = None, vat: float = None, gross: float = None,
                                description_invoice: str = None, cost_center_id: int = None):
        """Method that creates new incoming invoice."""
        try:
            with SessionLocal() as db:
                incoming_invoice_repository = IncomingInvoiceRepository(db)
                return incoming_invoice_repository.create_incoming_invoices(
                    reference_code_invoice=reference_code_invoice,
                    number_invoice=number_invoice, invoice_date=invoice_date, net=net,
                    vat=vat, gross=gross, description_invoice=description_invoice,
                    supplier_id=supplier_id, cost_center_id=cost_center_id)
        except Exception as e:
            raise e

    @staticmethod
    def read_all_incoming_invoices():
        """Method that shows all incoming invoices."""
        try:
            with SessionLocal() as db:
                incoming_invoices = IncomingInvoiceRepository(db)
                return incoming_invoices.read_all_incoming_invoices()
        except Exception as e:
            raise e

    @staticmethod
    def read_incoming_invoice_by_id(incoming_invoice_id: int):
        """Method that reads specific invoice based on invoice id."""
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
        """Method that updates values in the database based on invoice id."""
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
        """Method that deletes incoming invoice by id."""
        try:
            with SessionLocal() as db:
                incoming_invoice_repository = IncomingInvoiceRepository(db)
                return incoming_invoice_repository.delete_incoming_invoice_by_id(
                    incoming_invoice_id=incoming_invoice_id)
        except Exception as e:
            raise e

    @staticmethod
    def sum_incoming_invoices_grouped_by_suppliers():
        """Method that shows sum of incoming invoices grouped by suppliers."""
        try:
            with SessionLocal() as db:
                incoming_invoices = IncomingInvoiceRepository(db)
                return incoming_invoices.sum_incoming_invoices_grouped_by_suppliers()
        except Exception as e:
            raise e

    @staticmethod
    def sum_incoming_invoices_grouped_by_cost_centers():
        """Method that shows sum of incoming invoices grouped by cost centers."""
        try:
            with SessionLocal() as db:
                incoming_invoices = IncomingInvoiceRepository(db)
                return incoming_invoices.sum_incoming_invoices_grouped_by_cost_center()
        except Exception as e:
            raise e

    @staticmethod
    def sum_incoming_invoices_by_years_and_months():
        """Method that shows sum of incoming invoices grouped by years and months."""
        try:
            with SessionLocal() as db:
                incoming_invoices = IncomingInvoiceRepository(db)
                return incoming_invoices.sum_incoming_invoices_by_years_and_months()
        except Exception as e:
            raise e

    @staticmethod
    def find_difference_incoming_invoice_gross_and_invoice_payments() -> list[dict]:
        """Method that shows gross income, payments and difference between the two."""
        try:
            with SessionLocal() as db:
                incoming_invoices_repository = IncomingInvoiceRepository(db)
                all_incoming_invoices = incoming_invoices_repository.read_all_incoming_invoices()
                incoming_invoice_payments_repository = IncomingInvoicePaymentRepository(db)
                incoming_invoice_payments = incoming_invoice_payments_repository.sum_incoming_invoice_payments()
                ids = [list(x.keys())[0] for x in incoming_invoice_payments]
                difference = []
                for row in all_incoming_invoices:
                    if row.incoming_invoice_id not in ids:
                        diff = {row.incoming_invoice_id: {"gross": row.gross,
                                                          "payments": 0,
                                                          "difference": row.gross}}
                        difference.append(diff)
                    else:
                        for invoice in incoming_invoice_payments:
                            if row.incoming_invoice_id == list(invoice.keys())[0]:
                                diff = {row.incoming_invoice_id: {"gross": row.gross,
                                                                  "payments": list(invoice.values())[0],
                                                                  "difference": row.gross - list(invoice.values())[0]}}
                                difference.append(diff)

                return difference
        except Exception as e:
            raise e
