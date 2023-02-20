from fastapi import APIRouter, Depends
from app.incoming_invoices.controller import IncomingInvoiceController, IncomingInvoicePaymentController
from app.incoming_invoices.schemas import *
from app.users.controller.user_auth_controller import JWTBearer

incoming_invoice_router = APIRouter(tags=["Incoming Invoices"], prefix="/api/incoming-incoming_invoices")


@incoming_invoice_router.post("/create-new-incoming-invoice",
                              response_model=IncomingInvoiceSchema)
def create_incoming_invoice(incoming_invoice: IncomingInvoiceSchemaIN):
    """
    - Method that creates new incoming invoice.
    -**reference_code_invoice**: mandatory field, but not unique
    -**number_invoice**: mandatory field, but not unique
    -**invoice_date**: mandatory field
    -**net**: not mandatory, but values can not be less than 0
    -**vat**: not mandatory, but values can not be less than 0
    -**gross**: not mandatory, but values can not be less than 0
    -**description_invoice**: not mandatory
    -**supplier_id**: mandatory field
    -**cost_center_id**: mandatory field
    """
    return IncomingInvoiceController.create_incoming_invoice(
        reference_code_invoice=incoming_invoice.reference_code_invoice,
        number_invoice=incoming_invoice.number_invoice, invoice_date=incoming_invoice.invoice_date,
        supplier_id=incoming_invoice.supplier_id, net=incoming_invoice.net, vat=incoming_invoice.vat,
        gross=incoming_invoice.gross, description_invoice=incoming_invoice.description_invoice,
        cost_center_id=incoming_invoice.cost_center_id)


@incoming_invoice_router.get("/get-all-incoming_invoices",
                             response_model=list[IncomingInvoiceSchema],
                             dependencies=[Depends(JWTBearer("super_user"))])
def get_all_incoming_invoices():
    """Method that shows all incoming invoices."""
    return IncomingInvoiceController.get_all_incoming_invoices()


@incoming_invoice_router.get("/get-incoming-invoice-by-id", response_model=IncomingInvoiceSchema)
def get_incoming_invoice_by_id(incoming_invoice_id: int):
    """
    - Method that reads specific invoice based on invoice id.
    - **incoming_invoice_id**: mandatory parameter
    """
    return IncomingInvoiceController.get_incoming_invoice_by_id(incoming_invoice_id=incoming_invoice_id)


@incoming_invoice_router.put("/update-incoming-invoice-data", response_model=IncomingInvoiceSchema)
def update_incoming_invoice_by_id(incoming_invoice_id: int, incoming_invoice: IncomingInvoiceSchemaUpdate):
    """
    - Method that updates values in the database based on invoice id.
    - **incoming_invoice_id**: mandatory parameter
    """
    return IncomingInvoiceController.update_incoming_invoices_by_id(
        incoming_invoice_id=incoming_invoice_id,
        reference_code_invoice=incoming_invoice.reference_code_invoice,
        number_invoice=incoming_invoice.number_invoice, invoice_date=incoming_invoice.invoice_date,
        supplier_id=incoming_invoice.supplier_id, net=incoming_invoice.net,
        vat=incoming_invoice.vat, gross=incoming_invoice.gross,
        description_invoice=incoming_invoice.description_invoice,
        cost_center_id=incoming_invoice.cost_center_id)


@incoming_invoice_router.delete("/delete-incoming-invoice-by-id", dependencies=[Depends(JWTBearer("super_user"))])
def delete_incoming_invoice_by_id(incoming_invoice_id: int):
    """
    - Method that deletes incoming invoice by id.
    - **incoming_invoice_id**: mandatory parameter
    """
    return IncomingInvoiceController.delete_incoming_invoice_by_id(incoming_invoice_id=incoming_invoice_id)


@incoming_invoice_router.get("/get-sum-of-incoming-invoices-grouped-by-supplier",
                             dependencies=[Depends(JWTBearer("super_user"))])
def sum_incoming_invoices_grouped_by_suppliers():
    """Method that shows sum of incoming invoices grouped by suppliers."""
    return IncomingInvoiceController.sum_incoming_invoices_grouped_by_suppliers()


@incoming_invoice_router.get("/get-sum-of-incoming-invoices-grouped-by-cost-centers",
                             dependencies=[Depends(JWTBearer("super_user"))])
def sum_incoming_invoices_grouped_by_cost_centers():
    """Method that shows sum of incoming invoices grouped by cost centers."""
    return IncomingInvoiceController.sum_incoming_invoices_grouped_by_cost_centers()


@incoming_invoice_router.get("/get-sum-incoming-invoices-by-years-and-months",
                             dependencies=[Depends(JWTBearer("super_user"))])
def get_sum_incoming_invoices_by_years_and_months():
    """Method that shows sum of incoming invoices grouped by years and months."""
    return IncomingInvoiceController.sum_incoming_invoices_grouped_by_years_and_months()


@incoming_invoice_router.get("/get-difference-incoming-invoice-gross-and-invoice-payments",
                             dependencies=[Depends(JWTBearer("super_user"))])
def find_difference_incoming_invoice_gross_and_invoice_payments():
    """Method that shows gross income, payments and difference between the two."""
    return IncomingInvoiceController.find_difference_incoming_invoice_gross_and_invoice_payments()


incoming_invoice_payments_router = APIRouter(tags=["Incoming Invoice Payments"],
                                             prefix="/api/incoming-invoice-payments")


@incoming_invoice_payments_router.post("/create-new-incoming-invoice-payments",
                                       response_model=IncomingInvoicePaymentSchema)
def create_incoming_invoice_payment(incoming_invoice_payment: IncomingInvoicePaymentIN):
    return IncomingInvoicePaymentController.create_incoming_invoice_payment(
        payment_date=incoming_invoice_payment.payment_date,
        payment_description=incoming_invoice_payment.payment_description,
        payment=incoming_invoice_payment.payment, incoming_invoice_id=incoming_invoice_payment.incoming_invoice_id)


@incoming_invoice_payments_router.get("/get-all-incoming_invoices-payments",
                                      response_model=list[IncomingInvoicePaymentSchema])
def get_all_incoming_invoices_payments():
    return IncomingInvoicePaymentController.get_all_incoming_invoices_payments()


@incoming_invoice_payments_router.get("/get-incoming-invoice-payments-by-incoming-invoice-id",
                                      response_model=list[IncomingInvoicePaymentSchema])
def get_incoming_invoice_payments_by_incoming_invoice_id(incoming_invoice_id: int):
    return IncomingInvoicePaymentController.get_incoming_invoice_payments_by_incoming_invoice_id(
        incoming_invoice_id=incoming_invoice_id)


@incoming_invoice_payments_router.put("/update-incoming-invoice-payment-by-id",
                                      response_model=IncomingInvoicePaymentSchema)
def update_incoming_invoice_payment_by_id(incoming_invoice_payment_id: int,
                                          incoming_invoice_payment: IncomingInvoicePaymentUpdate):
    return IncomingInvoicePaymentController.update_incoming_invoice_payment_by_id(
        incoming_invoice_payment_id=incoming_invoice_payment_id,
        payment_date=incoming_invoice_payment.payment_date,
        payment_description=incoming_invoice_payment.payment_description,
        payment=incoming_invoice_payment.payment,
        incoming_invoice_id=incoming_invoice_payment.incoming_invoice_id)


@incoming_invoice_payments_router.delete("/delete-incoming-invoice-payment-by-id")
def delete_incoming_invoice_payment_by_id(incoming_invoice_payment_id: int):
    return IncomingInvoicePaymentController.delete_incoming_invoice_payment_by_id(
        incoming_invoice_payment_id=incoming_invoice_payment_id)


@incoming_invoice_payments_router.get("/get-sum-incoming-invoice-payments")
def get_sum_incoming_invoice_payments():
    return IncomingInvoicePaymentController.sum_incoming_invoice_payments()
