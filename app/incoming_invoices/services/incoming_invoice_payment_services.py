from app.db import SessionLocal
from app.incoming_invoices.repository import IncomingInvoicePaymentRepository


class IncomingInvoicePaymentService:

    @staticmethod
    def create_incoming_invoice_payment(payment_date: str, payment: float, incoming_invoice_id: int,
                                        payment_description: str = None) -> IncomingInvoicePaymentRepository:
        try:
            with SessionLocal() as db:
                incoming_invoice_payment_repository = IncomingInvoicePaymentRepository(db)
                return incoming_invoice_payment_repository.create_incoming_invoice_payment(
                    payment_date=payment_date,
                    payment=payment,
                    incoming_invoice_id=incoming_invoice_id,
                    payment_description=payment_description)
        except Exception as e:
            raise e

    @staticmethod
    def read_all_incoming_invoice_payments():
        try:
            with SessionLocal() as db:
                incoming_invoice_payments = IncomingInvoicePaymentRepository(db)
                return incoming_invoice_payments.read_all_incoming_invoices_payments()
        except Exception as e:
            raise e

    @staticmethod
    def read_incoming_invoice_payments_by_incoming_invoice_id(incoming_invoice_id: int):
        try:
            with SessionLocal() as db:
                incoming_invoice_payments_repository = IncomingInvoicePaymentRepository(db)
                return incoming_invoice_payments_repository.read_incoming_invoice_payments_by_incoming_invoice_id(
                    incoming_invoice_id=incoming_invoice_id)
        except Exception as e:
            raise e

    @staticmethod
    def update_incoming_invoice_payment_by_id(incoming_invoice_payment_id: int, payment_date: str = None,
                                              payment_description: str = None, payment: float = None,
                                              incoming_invoice_id: int = None):
        try:
            with SessionLocal() as db:
                incoming_invoice_payment_repository = IncomingInvoicePaymentRepository(db)
                return incoming_invoice_payment_repository.update_incoming_invoice_payment_by_id(
                    incoming_invoice_payment_id=incoming_invoice_payment_id, payment_date=payment_date,
                    payment_description=payment_description, payment=payment, incoming_invoice_id=incoming_invoice_id)
        except Exception as e:
            raise e

    @staticmethod
    def delete_incoming_invoice_payment_by_id(incoming_invoice_payment_id: int):
        try:
            with SessionLocal() as db:
                incoming_invoice_payment_repository = IncomingInvoicePaymentRepository(db)
                return incoming_invoice_payment_repository.delete_incoming_invoice_payment_by_id(
                    incoming_invoice_payment_id=incoming_invoice_payment_id)
        except Exception as e:
            raise e

    @staticmethod
    def sum_incoming_invoice_payments():
        try:
            with SessionLocal() as db:
                incoming_invoice_payment_repository = IncomingInvoicePaymentRepository(db)
                result = incoming_invoice_payment_repository.sum_incoming_invoice_payments()
                return result
        except Exception as e:
            raise e
