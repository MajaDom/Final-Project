from app.db import SessionLocal
from app.outgoing_invoices.repository import OutgoingInvoicePaymentRepository


class OutgoingInvoicePaymentService:

    @staticmethod
    def create_outgoing_invoice_payment(payment_date: str, payment: float, outgoing_invoice_id: int,
                                        payment_description: str = None) -> OutgoingInvoicePaymentRepository:
        """Method that creates new outgoing invoice"""
        try:
            with SessionLocal() as db:
                outgoing_invoice_payment_repository = OutgoingInvoicePaymentRepository(db)
                return outgoing_invoice_payment_repository.create_outgoing_invoice_payment(
                    payment_date=payment_date,
                    payment=payment,
                    outgoing_invoice_id=outgoing_invoice_id,
                    payment_description=payment_description)
        except Exception as e:
            raise e

    @staticmethod
    def read_all_outgoing_invoice_payments():
        """Method that reads all outgoing invoice payments."""
        try:
            with SessionLocal() as db:
                outgoing_invoice_payments = OutgoingInvoicePaymentRepository(db)
                return outgoing_invoice_payments.read_all_outgoing_invoices_payments()
        except Exception as e:
            raise e

    @staticmethod
    def read_outgoing_invoice_payments_by_outgoing_invoice_id(outgoing_invoice_id: int):
        """Method that reads outgoing invoice payment based on payment id."""
        try:
            with SessionLocal() as db:
                outgoing_invoice_payments_repository = OutgoingInvoicePaymentRepository(db)
                return outgoing_invoice_payments_repository.read_outgoing_invoice_payments_by_outgoing_invoice_id(
                    outgoing_invoice_id=outgoing_invoice_id)
        except Exception as e:
            raise e

    @staticmethod
    def update_outgoing_invoice_payment_by_id(outgoing_invoice_payment_id: int, payment_date: str = None,
                                              payment_description: str = None, payment: float = None,
                                              outgoing_invoice_id: int = None):
        """Method that updates existing values in the database for payment whose id has been provided."""
        try:
            with SessionLocal() as db:
                outgoing_invoice_payment_repository = OutgoingInvoicePaymentRepository(db)
                return outgoing_invoice_payment_repository.update_outgoing_invoice_payment_by_id(
                    outgoing_invoice_payment_id=outgoing_invoice_payment_id, payment_date=payment_date,
                    payment_description=payment_description, payment=payment, outgoing_invoice_id=outgoing_invoice_id)
        except Exception as e:
            raise e

    @staticmethod
    def delete_outgoing_invoice_payment_by_id(outgoing_invoice_payment_id: int):
        """Method that deletes outgoing invoice based in payment id."""
        try:
            with SessionLocal() as db:
                outgoing_invoice_payment_repository = OutgoingInvoicePaymentRepository(db)
                return outgoing_invoice_payment_repository.delete_outgoing_invoice_payment_by_id(
                    outgoing_invoice_payment_id=outgoing_invoice_payment_id)
        except Exception as e:
            raise e

    @staticmethod
    def sum_outgoing_invoice_payments():
        """Method that sums all invoice payments."""
        try:
            with SessionLocal() as db:
                outgoing_invoice_payment_repository = OutgoingInvoicePaymentRepository(db)
                result = outgoing_invoice_payment_repository.sum_outgoing_invoice_payments()
                return result
        except Exception as e:
            raise e
