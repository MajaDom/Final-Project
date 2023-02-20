from sqlalchemy import func
from sqlalchemy.orm import Session
from app.outgoing_invoices.models import OutgoingInvoicePayment
from app.outgoing_invoices.exceptions import OutgoingInvoiceDoesNotExistInTheDatabaseException, \
    OutgoingInvoicePaymentDoesNotExistInTheDatabaseException, InvalidInputException
from datetime import datetime


class OutgoingInvoicePaymentRepository:
    def __init__(self, db: Session):
        self.db = db

    def create_outgoing_invoice_payment(self, payment_date: str, payment: float, outgoing_invoice_id: int,
                                        payment_description: str = None) -> OutgoingInvoicePayment:
        """Method that creates new outgoing invoice"""
        try:
            datetime.strptime(payment_date, "%Y-%m-%d")
            if payment < 0:
                raise InvalidInputException(code=400, message="Invalid Input.")
            outgoing_invoice_payment = OutgoingInvoicePayment(payment_date=payment_date, payment=payment,
                                                              outgoing_invoice_id=outgoing_invoice_id,
                                                              payment_description=payment_description)
            self.db.add(outgoing_invoice_payment)
            self.db.commit()
            self.db.refresh(outgoing_invoice_payment)
            return outgoing_invoice_payment
        except InvalidInputException as e:
            raise e
        except Exception as e:
            raise e

    def read_all_outgoing_invoices_payments(self) -> list[OutgoingInvoicePayment]:
        """Method that reads all outgoing invoice payments."""
        outgoing_invoices_payments = self.db.query(OutgoingInvoicePayment).all()
        return outgoing_invoices_payments

    def read_outgoing_invoice_payments_by_outgoing_invoice_id(self, outgoing_invoice_id: int) -> \
            list[OutgoingInvoicePayment]:
        """Method that reads outgoing invoice payment based on payment id."""
        outgoing_invoice_payments = self.db.query(OutgoingInvoicePayment).filter(
            OutgoingInvoicePayment.outgoing_invoice_id == outgoing_invoice_id).all()
        if outgoing_invoice_payments is None:
            raise OutgoingInvoiceDoesNotExistInTheDatabaseException(
                message=f'Invoice with id {outgoing_invoice_id} not in the database.',
                code=400)
        return outgoing_invoice_payments

    def update_outgoing_invoice_payment_by_id(self, outgoing_invoice_payment_id: int, payment_date: str = None,
                                              payment_description: str = None, payment: float = None,
                                              outgoing_invoice_id: int = None) -> OutgoingInvoicePayment:
        """Method that updates existing values in the database for payment whose id has been provided."""
        outgoing_invoice_payment = self.db.query(OutgoingInvoicePayment).filter(
            OutgoingInvoicePayment.outgoing_invoice_payment_id == outgoing_invoice_payment_id).first()

        if outgoing_invoice_payment is None:
            raise OutgoingInvoicePaymentDoesNotExistInTheDatabaseException(
                message=f'Payment with id {outgoing_invoice_payment_id} not in the database.',
                code=400)
        if payment_date is not None and payment_date != "":
            try:
                datetime.strptime(payment_date, "%Y-%m-%d")
                outgoing_invoice_payment.payment_date = payment_date
            except Exception as e:
                raise e
        if payment_description is not None and payment_description != "":
            outgoing_invoice_payment.payment_description = payment_description
        if payment is not None and payment != "":
            outgoing_invoice_payment.payment = payment
        if outgoing_invoice_id is not None and outgoing_invoice_id != "":
            outgoing_invoice_payment.outgoing_invoice_id = outgoing_invoice_id

        self.db.add(outgoing_invoice_payment)
        self.db.commit()
        self.db.refresh(outgoing_invoice_payment)
        return outgoing_invoice_payment

    def delete_outgoing_invoice_payment_by_id(self, outgoing_invoice_payment_id: int):
        """Method that deletes outgoing invoice based in payment id."""
        outgoing_invoice_payment = self.db.query(OutgoingInvoicePayment).filter(
            OutgoingInvoicePayment.outgoing_invoice_payment_id == outgoing_invoice_payment_id).first()
        if outgoing_invoice_payment is None:
            raise OutgoingInvoicePaymentDoesNotExistInTheDatabaseException(
                message=f'Payment with id {outgoing_invoice_payment_id} not in the database.',
                code=400)
        self.db.delete(outgoing_invoice_payment)
        self.db.commit()
        return True

    def sum_outgoing_invoice_payments(self):
        """Method that sums all invoice payments."""
        outgoing_invoices_payments = self.db.query(OutgoingInvoicePayment.outgoing_invoice_id,
                                                   func.sum(OutgoingInvoicePayment.payment)).group_by(
            OutgoingInvoicePayment.outgoing_invoice_id)
        response = []
        for row in outgoing_invoices_payments:
            dictionary = {row[0]: row[1]}
            response.append(dictionary)
        return response
