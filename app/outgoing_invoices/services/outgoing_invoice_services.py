from app.db import SessionLocal
from app.outgoing_invoices.repository import OutgoingInvoiceRepository, OutgoingInvoicePaymentRepository


class OutgoingInvoicesService:

    @staticmethod
    def create_outgoing_invoice(client_id, reference_code_invoice: str, start_date: str, date_of_transaction: str,
                                certified_invoice: str, net: float = None, vat: float = None, gross: float = None,
                                description_invoice: str = None, cost_center_id: int = None):
        """Method that creates new outgoing invoice."""
        try:
            with SessionLocal() as db:
                outgoing_invoice_repository = OutgoingInvoiceRepository(db)
                return outgoing_invoice_repository.create_outgoing_invoices(
                    reference_code_invoice=reference_code_invoice, client_id=client_id,
                    start_date=start_date,
                    date_of_transaction=date_of_transaction, certified_invoice=certified_invoice,
                    net=net, vat=vat, gross=gross, description_invoice=description_invoice,
                    cost_center_id=cost_center_id)
        except Exception as e:
            raise e

    @staticmethod
    def read_all_outgoing_invoices():
        """Method that reads all outgoing invoices."""
        try:
            with SessionLocal() as db:
                outgoing_invoices = OutgoingInvoiceRepository(db)
                return outgoing_invoices.read_all_outgoing_invoices()
        except Exception as e:
            raise e

    @staticmethod
    def read_outgoing_invoice_by_id(outgoing_invoice_id: int):
        """Method that reads outgoing invoice by id."""
        try:
            with SessionLocal() as db:
                outgoing_invoice_repository = OutgoingInvoiceRepository(db)
                return outgoing_invoice_repository.read_outgoing_invoice_by_id(outgoing_invoice_id=outgoing_invoice_id)
        except Exception as e:
            raise e

    @staticmethod
    def update_outgoing_invoice_by_id(outgoing_invoice_id: int, client_id: int = None,
                                      reference_code_invoice: str = None,
                                      start_date: str = None, date_of_transaction: str = None,
                                      certified_invoice: str = None, net: float = None, vat: float = None,
                                      gross: float = None,
                                      description_invoice: str = None, cost_center_id: int = None):
        """Method that updates existing values in the database."""
        try:
            with SessionLocal() as db:
                outgoing_invoice_repository = OutgoingInvoiceRepository(db)
                return outgoing_invoice_repository.update_outgoing_invoice_by_id(
                    outgoing_invoice_id=outgoing_invoice_id, client_id=client_id,
                    reference_code_invoice=reference_code_invoice,
                    start_date=start_date, date_of_transaction=date_of_transaction,
                    certified_invoice=certified_invoice, net=net,
                    vat=vat, gross=gross, description_invoice=description_invoice,
                    cost_center_id=cost_center_id)
        except Exception as e:
            raise e

    @staticmethod
    def delete_outgoing_invoice_by_id(outgoing_invoice_id: int):
        """Method that deletes outgoing invoice by id."""
        try:
            with SessionLocal() as db:
                outgoing_invoice_repository = OutgoingInvoiceRepository(db)
                return outgoing_invoice_repository.delete_outgoing_invoice_by_id(
                    outgoing_invoice_id=outgoing_invoice_id)
        except Exception as e:
            raise e

    @staticmethod
    def sum_outgoing_invoices_grouped_by_clients():
        """Method that sums gross total grouped by clients."""
        try:
            with SessionLocal() as db:
                outgoing_invoices = OutgoingInvoiceRepository(db)
                return outgoing_invoices.sum_outgoing_invoices_grouped_by_clients()
        except Exception as e:
            raise e

    @staticmethod
    def sum_outgoing_invoices_grouped_by_cost_centers():
        """Method that sums gross total grouped by cost center."""
        try:
            with SessionLocal() as db:
                outgoing_invoices = OutgoingInvoiceRepository(db)
                return outgoing_invoices.sum_outgoing_invoices_grouped_by_cost_centers()
        except Exception as e:
            raise e

    @staticmethod
    def sum_outgoing_invoices_by_years_and_months():
        """Method that sums gross total grouped by years and months."""
        try:
            with SessionLocal() as db:
                outgoing_invoices = OutgoingInvoiceRepository(db)
                return outgoing_invoices.sum_outgoing_invoices_by_years_and_months()
        except Exception as e:
            raise e

    @staticmethod
    def find_difference_outgoing_invoice_gross_and_invoice_payments():
        """Method that shows gross income, payments and difference between the two."""
        try:
            with SessionLocal() as db:
                outgoing_invoices_repository = OutgoingInvoiceRepository(db)
                all_outgoing_invoices = outgoing_invoices_repository.read_all_outgoing_invoices()
                outgoing_invoice_payments_repository = OutgoingInvoicePaymentRepository(db)
                outgoing_invoice_payments = outgoing_invoice_payments_repository.sum_outgoing_invoice_payments()
                ids = [list(x.keys())[0] for x in outgoing_invoice_payments]
                difference = []
                for row in all_outgoing_invoices:
                    if row.outgoing_invoice_id not in ids:
                        diff = {row.outgoing_invoice_id: {"gross": row.gross,
                                                          "payments": 0,
                                                          "difference": row.gross}}
                        difference.append(diff)
                    else:
                        for invoice in outgoing_invoice_payments:
                            if row.outgoing_invoice_id == list(invoice.keys())[0]:
                                diff = {row.outgoing_invoice_id: {"gross": row.gross,
                                                                  "payments": list(invoice.values())[0],
                                                                  "difference": row.gross - list(invoice.values())[0]}}
                                difference.append(diff)

                return difference
        except Exception as e:
            raise e
