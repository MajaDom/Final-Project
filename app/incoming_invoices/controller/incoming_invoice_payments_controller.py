from fastapi import HTTPException, Response
from app.incoming_invoices.services import IncomingInvoicePaymentService
from app.incoming_invoices.exceptions import IncomingInvoiceDoesNotExistInTheDatabaseException, \
    IncomingInvoicePaymentDoesNotExistInTheDatabaseException, InvalidInputException


class IncomingInvoicePaymentController:

    @staticmethod
    def create_incoming_invoice_payment(payment_date: str, payment: float, incoming_invoice_id: int,
                                        payment_description: str = None):
        try:
            incoming_invoice_payment = IncomingInvoicePaymentService.create_incoming_invoice_payment(
                payment_date=payment_date, payment=payment, incoming_invoice_id=incoming_invoice_id,
                payment_description=payment_description)
            return incoming_invoice_payment
        except InvalidInputException as e:
            raise HTTPException(status_code=e.code, detail=e.message)
        except Exception as e:
            raise HTTPException(status_code=500, detail=f"Unprocessed error: {str(e)}")

    @staticmethod
    def get_all_incoming_invoices_payments():
        try:
            incoming_invoices_payments = IncomingInvoicePaymentService.read_all_incoming_invoice_payments()
            return incoming_invoices_payments
        except Exception as e:
            raise HTTPException(status_code=500, detail=f"Unprocessed error: {str(e)}")

    @staticmethod
    def get_incoming_invoice_payments_by_incoming_invoice_id(incoming_invoice_id: int):
        try:
            incoming_invoice_payments = IncomingInvoicePaymentService.read_incoming_invoice_payments_by_incoming_invoice_id(
                incoming_invoice_id=incoming_invoice_id)
            return incoming_invoice_payments
        except IncomingInvoiceDoesNotExistInTheDatabaseException as e:
            raise HTTPException(status_code=e.code, detail=e.message)
        except Exception as e:
            raise HTTPException(status_code=500, detail=f"Unprocessed error: {str(e)}")

    @staticmethod
    def update_incoming_invoice_payment_by_id(incoming_invoice_payment_id: int, payment_date: str = None,
                                              payment_description: str = None, payment: float = None,
                                              incoming_invoice_id: int = None):
        try:
            incoming_invoice_payment = IncomingInvoicePaymentService.update_incoming_invoice_payment_by_id(
                incoming_invoice_payment_id=incoming_invoice_payment_id,
                payment_date=payment_date, payment_description=payment_description,
                payment=payment, incoming_invoice_id=incoming_invoice_id)
            return incoming_invoice_payment
        except InvalidInputException as e:
            raise HTTPException(status_code=e.code, detail=e.message)
        except IncomingInvoicePaymentDoesNotExistInTheDatabaseException as e:
            raise HTTPException(status_code=e.code, detail=e.message)
        except Exception as e:
            raise HTTPException(status_code=500, detail=f"Unprocessed error: {str(e)}")

    @staticmethod
    def delete_incoming_invoice_payment_by_id(incoming_invoice_payment_id: int):
        try:
            IncomingInvoicePaymentService.delete_incoming_invoice_payment_by_id(
                incoming_invoice_payment_id=incoming_invoice_payment_id)
            return Response(content=f"Payment with id {incoming_invoice_payment_id} successfully deleted.")
        except IncomingInvoicePaymentDoesNotExistInTheDatabaseException as e:
            raise HTTPException(status_code=e.code, detail=e.message)
        except Exception as e:
            raise HTTPException(status_code=500, detail=f"Unprocessed error: {str(e)}")

    @staticmethod
    def sum_incoming_invoice_payments():
        try:
            return IncomingInvoicePaymentService.sum_incoming_invoice_payments()
        except Exception as e:
            raise HTTPException(status_code=500, detail=f"Unprocessed error: {str(e)}")
