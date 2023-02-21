from sqlalchemy import func
from sqlalchemy.orm import Session
from app.incoming_invoices.models import IncomingInvoicePayment
from app.incoming_invoices.exceptions import IncomingInvoiceDoesNotExistInTheDatabaseException, \
    IncomingInvoicePaymentDoesNotExistInTheDatabaseException, InvalidInputException
from datetime import datetime


class IncomingInvoicePaymentRepository:
    def __init__(self, db: Session):
        self.db = db

    def create_incoming_invoice_payment(self, payment_date: str, payment: float, incoming_invoice_id: int,
                                        payment_description: str = None) -> IncomingInvoicePayment:
        """Method that creates new incoming invoice payment."""
        try:
            datetime.strptime(payment_date, "%Y-%m-%d")
            if payment < 0:
                raise InvalidInputException(code=400, message="Invalid Input.")
            incoming_invoice_payment = IncomingInvoicePayment(payment_date=payment_date, payment=payment,
                                                              incoming_invoice_id=incoming_invoice_id,
                                                              payment_description=payment_description)
            self.db.add(incoming_invoice_payment)
            self.db.commit()
            self.db.refresh(incoming_invoice_payment)
            return incoming_invoice_payment
        except InvalidInputException:
            raise InvalidInputException(code=400, message="Invalid Input.")
        except Exception as e:
            raise e

    def read_all_incoming_invoices_payments(self) -> list[IncomingInvoicePayment]:
        """Method that returns all incoming invoices."""
        incoming_invoices_payments = self.db.query(IncomingInvoicePayment).all()
        return incoming_invoices_payments

    def read_incoming_invoice_payments_by_incoming_invoice_id(self, incoming_invoice_id: int) -> \
            list[IncomingInvoicePayment]:
        """Method that returns specific invoice based on invoice id."""
        incoming_invoice_payments = self.db.query(IncomingInvoicePayment).filter(
            IncomingInvoicePayment.incoming_invoice_id == incoming_invoice_id).all()
        if incoming_invoice_payments is None:
            raise IncomingInvoiceDoesNotExistInTheDatabaseException(
                message=f'Invoice with id {incoming_invoice_id} not in the database.',
                code=400)
        return incoming_invoice_payments

    def update_incoming_invoice_payment_by_id(self, incoming_invoice_payment_id: int, payment_date: str = None,
                                              payment_description: str = None, payment: float = None,
                                              incoming_invoice_id: int = None) -> IncomingInvoicePayment:
        """Method that updates existing values."""
        incoming_invoice_payment = self.db.query(IncomingInvoicePayment).filter(
            IncomingInvoicePayment.incoming_invoice_payment_id == incoming_invoice_payment_id).first()

        if incoming_invoice_payment is None:
            raise IncomingInvoicePaymentDoesNotExistInTheDatabaseException(
                message=f'Payment with id {incoming_invoice_payment_id} not in the database.',
                code=400)
        if payment_date is not None and payment_date != "":
            try:
                datetime.strptime(payment_date, "%Y-%m-%d")
                incoming_invoice_payment.payment_date = payment_date
            except Exception:
                raise InvalidInputException(code=400, message="Invalid Input.")
        if payment_description is not None and payment_description != "":
            incoming_invoice_payment.payment_description = payment_description
        if payment is not None and payment != "":
            if payment < 0:
                raise InvalidInputException(code=400, message="Invalid Input.")
            incoming_invoice_payment.payment = payment
        if incoming_invoice_id is not None and incoming_invoice_id != "":
            incoming_invoice_payment.incoming_invoice_id = incoming_invoice_id

        self.db.add(incoming_invoice_payment)
        self.db.commit()
        self.db.refresh(incoming_invoice_payment)
        return incoming_invoice_payment

    def delete_incoming_invoice_payment_by_id(self, incoming_invoice_payment_id: int):
        """Method that deletes invoice payment from the database."""
        incoming_invoice_payment = self.db.query(IncomingInvoicePayment).filter(
            IncomingInvoicePayment.incoming_invoice_payment_id == incoming_invoice_payment_id).first()
        if incoming_invoice_payment is None:
            raise IncomingInvoicePaymentDoesNotExistInTheDatabaseException(
                message=f'Payment with id {incoming_invoice_payment_id} not in the database.',
                code=400)
        self.db.delete(incoming_invoice_payment)
        self.db.commit()
        return True

    def sum_incoming_invoice_payments(self):
        """Method that sums all invoice payments."""
        incoming_invoices_payments = self.db.query(IncomingInvoicePayment.incoming_invoice_id,
                                                   func.sum(IncomingInvoicePayment.payment)).group_by(
            IncomingInvoicePayment.incoming_invoice_id)
        response = []
        for row in incoming_invoices_payments:
            dictionary = {row[0]: row[1]}
            response.append(dictionary)
        return response
