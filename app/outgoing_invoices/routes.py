from fastapi import APIRouter, Depends
from app.users.controller.user_auth_controller import JWTBearer
from app.outgoing_invoices.controller import OutgoingInvoicePaymentController, OutgoingInvoiceController
from app.outgoing_invoices.schemas import *

outgoing_invoice_router = APIRouter(tags=["Outgoing Invoices"], prefix="/api/outgoing-outgoing_invoices")


@outgoing_invoice_router.post("/create-new-outgoing-invoice", response_model=OutgoingInvoiceSchema)
def create_outgoing_invoice(outgoing_invoice: OutgoingInvoiceSchemaIN):
    """
    - Method that creates new outgoing invoice.
    - **reference_code_invoice**: mandatory field
    - **start_date**: mandatory field
    - **date_of_transaction**: mandatory field
    - **certified_invoice**: not mandatory
    - **net**: not mandatory
    - **vat**: not mandatory
    - **gross**: not mandatory
    - **description_invoice**: not mandatory
    - **cost_center_id**: mandatory field
    """
    return OutgoingInvoiceController.create_outgoing_invoice(
        reference_code_invoice=outgoing_invoice.reference_code_invoice,
        start_date=outgoing_invoice.start_date,
        date_of_transaction=outgoing_invoice.date_of_transaction,
        net=outgoing_invoice.net, vat=outgoing_invoice.vat,
        gross=outgoing_invoice.gross,
        description_invoice=outgoing_invoice.description_invoice,
        client_id=outgoing_invoice.client_id,
        cost_center_id=outgoing_invoice.cost_center_id,
        certified_invoice=outgoing_invoice.certified_invoice)


@outgoing_invoice_router.get("/get-all-outgoing_invoices",
                             response_model=list[OutgoingInvoiceSchema],
                             dependencies=[Depends(JWTBearer("super_user"))])
def get_all_outgoing_invoices():
    """Method that reads all outgoing invoices."""
    return OutgoingInvoiceController.get_all_outgoing_invoices()


@outgoing_invoice_router.get("/get-outgoing-invoice-by-id", response_model=OutgoingInvoiceSchema)
def get_outgoing_invoice_by_id(outgoing_invoice_id: int):
    """
    - Method that reads outgoing invoice by id.
    - **outgoing_invoice_id**: mandatory parameter
    """
    return OutgoingInvoiceController.get_outgoing_invoice_by_id(outgoing_invoice_id=outgoing_invoice_id)


@outgoing_invoice_router.put("/update-outgoing-invoice-data", response_model=OutgoingInvoiceSchema)
def update_outgoing_invoice_by_id(outgoing_invoice_id: int, outgoing_invoice: OutgoingInvoiceSchemaUpdate):
    """
    - Method that updates existing values in the database.
    - **reference_code_invoice**: not mandatory
    - **start_date**: not mandatory
    - **date_of_transaction**: not mandatory
    - **certified_invoice**: not mandatory
    - **net**: not mandatory
    - **vat**: not mandatory
    - **gross**: not mandatory
    - **description_invoice**: not mandatory
    - **cost_center_id**: not mandatory
    """
    return OutgoingInvoiceController.update_outgoing_invoices_by_id(
        outgoing_invoice_id=outgoing_invoice_id,
        reference_code_invoice=outgoing_invoice.reference_code_invoice,
        start_date=outgoing_invoice.start_date,
        date_of_transaction=outgoing_invoice.date_of_transaction,
        net=outgoing_invoice.net, vat=outgoing_invoice.vat,
        gross=outgoing_invoice.gross,
        description_invoice=outgoing_invoice.description_invoice,
        client_id=outgoing_invoice.client_id,
        cost_center_id=outgoing_invoice.cost_center_id)


@outgoing_invoice_router.delete("/delete-outgoing-invoice-by-id")
def delete_outgoing_invoice_by_id(outgoing_invoice_id: int):
    """
    - Method that deletes outgoing invoice by id.
    - **outgoing_invoice_id**: mandatory parameter
    """
    return OutgoingInvoiceController.delete_outgoing_invoice_by_id(outgoing_invoice_id)


@outgoing_invoice_router.get("/get-sum-outgoing_invoices-by-client",
                             dependencies=[Depends(JWTBearer("super_user"))])
def get_all_outgoing_invoices_grouped_by_clients():
    """Method that sums gross total grouped by clients."""
    return OutgoingInvoiceController.sum_outgoing_invoices_grouped_by_clients()


@outgoing_invoice_router.get("/get-sum-outgoing_invoices-by-cost-centers",
                             dependencies=[Depends(JWTBearer("super_user"))])
def get_all_outgoing_invoices_grouped_by_cost_centers():
    """Method that sums gross total grouped by cost center."""
    return OutgoingInvoiceController.sum_outgoing_invoices_grouped_by_cost_centers()


@outgoing_invoice_router.get("/get-sum-outgoing_invoices-by-years-and-months",
                             dependencies=[Depends(JWTBearer("super_user"))])
def get_sum_outgoing_invoices_by_years_and_months():
    """Method that sums gross total grouped by years and months."""
    return OutgoingInvoiceController.sum_outgoing_invoices_grouped_by_years_and_months()


@outgoing_invoice_router.get("/get-difference-outgoing_invoices-gross-and-invoice-payments",
                             dependencies=[Depends(JWTBearer("super_user"))])
def get_difference_outgoing_invoice_gross_and_invoice_payments():
    """Method that shows gross income, payments and difference between the two."""
    return OutgoingInvoiceController.find_difference_outgoing_invoice_gross_and_invoice_payments()


outgoing_invoice_payments_router = APIRouter(tags=["Outgoing Invoice Payments"],
                                             prefix="/api/outgoing-invoice-payments")


@outgoing_invoice_payments_router.post("/create-new-outgoing-invoice-payments",
                                       response_model=OutgoingInvoicePaymentSchema,
                                       dependencies=[Depends(JWTBearer("super_user"))])
def create_outgoing_invoice_payment(outgoing_invoice_payment: OutgoingInvoicePaymentIN):
    """
    - Method that creates new outgoing invoice
    - **payment_date**: mandatory field
    - **payment_description**: not mandatory
    - **payment**: mandatory field
    - **outgoing_invoice_id**: mandatory field
    """
    return OutgoingInvoicePaymentController.create_outgoing_invoice_payment(
        payment_date=outgoing_invoice_payment.payment_date,
        payment_description=outgoing_invoice_payment.payment_description,
        payment=outgoing_invoice_payment.payment, outgoing_invoice_id=outgoing_invoice_payment.outgoing_invoice_id)


@outgoing_invoice_payments_router.get("/get-all-outgoing_invoices-payments",
                                      response_model=list[OutgoingInvoicePaymentSchema],
                                      dependencies=[Depends(JWTBearer("super_user"))])
def get_all_outgoing_invoices_payments():
    """Method that reads all outgoing invoice payments."""
    return OutgoingInvoicePaymentController.get_all_outgoing_invoices_payments()


@outgoing_invoice_payments_router.get("/get-outgoing-invoice-payments-by-outgoing-invoice-id",
                                      response_model=list[OutgoingInvoicePaymentSchema])
def get_outgoing_invoice_payments_by_outgoing_invoice_id(outgoing_invoice_id: int):
    """
    - Method that reads outgoing invoice payment based on payment id.
    - **outgoing_invoice_id**: mandatory parameter
    """
    return OutgoingInvoicePaymentController.get_outgoing_invoice_payments_by_outgoing_invoice_id(
        outgoing_invoice_id=outgoing_invoice_id)


@outgoing_invoice_payments_router.put("/update-outgoing-invoice-payment-by-id",
                                      response_model=OutgoingInvoicePaymentSchema)
def update_outgoing_invoice_payment_by_id(outgoing_invoice_payment_id: int,
                                          outgoing_invoice_payment: OutgoingInvoicePaymentUpdate):
    """
    - Method that updates existing values in the database for payment whose id has been provided.
    - **outgoing_invoice_payment_id**: mandatory parameter
    - **payment_date**: not mandatory
    - **payment_description**: not mandatory
    - **payment**: not mandatory
    - **outgoing_invoice_id**: not mandatory
    """
    return OutgoingInvoicePaymentController.update_outgoing_invoice_payment_by_id(
        outgoing_invoice_payment_id=outgoing_invoice_payment_id,
        payment_date=outgoing_invoice_payment.payment_date,
        payment_description=outgoing_invoice_payment.payment_description,
        payment=outgoing_invoice_payment.payment,
        outgoing_invoice_id=outgoing_invoice_payment.outgoing_invoice_id)


@outgoing_invoice_payments_router.delete("/delete-outgoing-invoice-payment-by-id",
                                         dependencies=[Depends(JWTBearer("super_user"))])
def delete_outgoing_invoice_payment_by_id(outgoing_invoice_payment_id: int):
    """
    - Method that deletes outgoing invoice based in payment id.
    - **outgoing_invoice_payment_id**: mandatory parameter
    """
    return OutgoingInvoicePaymentController.delete_outgoing_invoice_payment_by_id(
        outgoing_invoice_payment_id=outgoing_invoice_payment_id)


@outgoing_invoice_payments_router.get("/get-sum-outgoing-invoice-payments",
                                      dependencies=[Depends(JWTBearer("super_user"))])
def get_sum_outgoing_invoice_payments():
    """Method that sums all invoice payments."""
    return OutgoingInvoicePaymentController.sum_outgoing_invoice_payments()
