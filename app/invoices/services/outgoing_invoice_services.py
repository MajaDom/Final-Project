from app.db import SessionLocal
from app.invoices.repository import OutgoingInvoiceRepository


class OutgoingInvoicesService:

    @staticmethod
    def create_outgoing_invoice(client_id, reference_code_invoice: str, start_date: str, date_of_transaction: str,
                                certified_invoice: str, net: float = None, vat: float = None, gross: float = None,
                                description_invoice: str = None, cost_center_id: int = None):
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
            return e

    @staticmethod
    def read_all_outgoing_invoices():
        try:
            with SessionLocal() as db:
                outgoing_invoices = OutgoingInvoiceRepository(db)
                return outgoing_invoices.read_all_outgoing_invoices()
        except Exception as e:
            raise e

    @staticmethod
    def read_outgoing_invoice_by_id(outgoing_invoice_id: int):
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
        try:
            with SessionLocal() as db:
                outgoing_invoice_repository = OutgoingInvoiceRepository(db)
                return outgoing_invoice_repository.delete_outgoing_invoice_by_id(outgoing_invoice_id=outgoing_invoice_id)
        except Exception as e:
            raise e
