from app.outgoing_invoices.services import OutgoingInvoicePaymentService
from app.outgoing_invoices.exceptions import OutgoingInvoiceDoesNotExistInTheDatabaseException, \
    OutgoingInvoicePaymentDoesNotExistInTheDatabaseException
from fastapi import HTTPException, Response


class OutgoingInvoicePaymentController:

    @staticmethod
    def create_outgoing_invoice_payment(payment_date: str, payment: float, outgoing_invoice_id: int,
                                        payment_description: str = None):
        try:
            outgoing_invoice_payment = OutgoingInvoicePaymentService.create_outgoing_invoice_payment(
                payment_date=payment_date, payment=payment, outgoing_invoice_id=outgoing_invoice_id,
                payment_description=payment_description)
            return outgoing_invoice_payment
        except Exception as e:
            raise e

    @staticmethod
    def get_all_outgoing_invoices_payments():
        try:
            outgoing_invoices_payments = OutgoingInvoicePaymentService.read_all_outgoing_invoice_payments()
            return outgoing_invoices_payments
        except Exception as e:
            raise HTTPException(status_code=500, detail=f"Unprocessed error: {str(e)}")

    @staticmethod
    def get_outgoing_invoice_payments_by_outgoing_invoice_id(outgoing_invoice_id: int):
        try:
            outgoing_invoice_payments = OutgoingInvoicePaymentService.read_outgoing_invoice_payments_by_outgoing_invoice_id(
                outgoing_invoice_id=outgoing_invoice_id)
            return outgoing_invoice_payments
        except OutgoingInvoiceDoesNotExistInTheDatabaseException as e:
            raise HTTPException(status_code=e.code, detail=e.message)
        except Exception as e:
            raise HTTPException(status_code=500, detail=f"Unprocessed error: {str(e)}")

    @staticmethod
    def update_outgoing_invoice_payment_by_id(outgoing_invoice_payment_id: int, payment_date: str = None,
                                              payment_description: str = None, payment: float = None,
                                              outgoing_invoice_id: int = None):
        try:
            outgoing_invoice_payment = OutgoingInvoicePaymentService.update_outgoing_invoice_payment_by_id(
                outgoing_invoice_payment_id=outgoing_invoice_payment_id,
                payment_date=payment_date, payment_description=payment_description,
                payment=payment, outgoing_invoice_id=outgoing_invoice_id)
            return outgoing_invoice_payment
        except OutgoingInvoicePaymentDoesNotExistInTheDatabaseException as e:
            raise HTTPException(status_code=e.code, detail=e.message)
        except Exception as e:
            raise HTTPException(status_code=500, detail=f"Unprocessed error: {str(e)}")

    @staticmethod
    def delete_outgoing_invoice_payment_by_id(outgoing_invoice_payment_id: int):
        try:
            OutgoingInvoicePaymentService.delete_outgoing_invoice_payment_by_id(
                outgoing_invoice_payment_id=outgoing_invoice_payment_id)
            return Response(content=f"Payment with id {outgoing_invoice_payment_id} successfully deleted.")
        except OutgoingInvoiceDoesNotExistInTheDatabaseException as e:
            raise HTTPException(status_code=e.code, detail=e.message)
        except Exception as e:
            raise HTTPException(status_code=500, detail=f"Unprocessed error: {str(e)}")

    @staticmethod
    def sum_outgoing_invoice_payments():
        try:
            return OutgoingInvoicePaymentService.sum_outgoing_invoice_payments()
        except Exception as e:
            raise HTTPException(status_code=500, detail=f"Unprocessed error: {str(e)}")