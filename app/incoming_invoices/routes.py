from fastapi import APIRouter
from app.incoming_invoices.controller import IncomingInvoiceController, IncomingInvoicePaymentController
from app.incoming_invoices.schemas import *

incoming_invoice_router = APIRouter(tags=["Incoming Invoices"], prefix="/api/incoming-incoming_invoices")


@incoming_invoice_router.post("/create-new-incoming-invoice", response_model=IncomingInvoiceSchema)
def create_incoming_invoice(incoming_invoice: IncomingInvoiceSchemaIN):
    return IncomingInvoiceController.create_incoming_invoice(
        reference_code_invoice=incoming_invoice.reference_code_invoice,
        number_invoice=incoming_invoice.number_invoice, invoice_date=incoming_invoice.invoice_date,
        supplier_id=incoming_invoice.supplier_id, net=incoming_invoice.net, vat=incoming_invoice.vat,
        gross=incoming_invoice.gross, description_invoice=incoming_invoice.description_invoice,
        cost_center_id=incoming_invoice.cost_center_id)


@incoming_invoice_router.get("/get-all-incoming_invoices", response_model=list[IncomingInvoiceSchema])
def get_all_incoming_invoices():
    return IncomingInvoiceController.get_all_incoming_invoices()


@incoming_invoice_router.get("/get-incoming-invoice-by-id", response_model=IncomingInvoiceSchema)
def get_incoming_invoice_by_id(incoming_invoice_id: int):
    return IncomingInvoiceController.get_incoming_invoice_by_id(incoming_invoice_id=incoming_invoice_id)


@incoming_invoice_router.put("/update-incoming-invoice-data", response_model=IncomingInvoiceSchema)
def update_incoming_invoice_by_id(incoming_invoice_id: int, incoming_invoice: IncomingInvoiceSchemaUpdate):
    return IncomingInvoiceController.update_incoming_invoices_by_id(
        incoming_invoice_id=incoming_invoice_id,
        reference_code_invoice=incoming_invoice.reference_code_invoice,
        number_invoice=incoming_invoice.number_invoice, invoice_date=incoming_invoice.invoice_date,
        supplier_id=incoming_invoice.supplier_id, net=incoming_invoice.net,
        vat=incoming_invoice.vat, gross=incoming_invoice.gross,
        description_invoice=incoming_invoice.description_invoice,
        cost_center_id=incoming_invoice.cost_center_id)


@incoming_invoice_router.delete("/delete-incoming-invoice-by-id")
def delete_incoming_invoice_by_id(incoming_invoice_id: int):
    return IncomingInvoiceController.delete_incoming_invoice_by_id(incoming_invoice_id=incoming_invoice_id)


@incoming_invoice_router.get("/get-sum-of-incoming-invoices-grouped-by-supplier")
def sum_incoming_invoices_grouped_by_suppliers():
    return IncomingInvoiceController.sum_incoming_invoices_grouped_by_suppliers()


@incoming_invoice_router.get("/get-sum-of-incoming-invoices-grouped-by-cost-centers")
def sum_incoming_invoices_grouped_by_cost_centers():
    return IncomingInvoiceController.sum_incoming_invoices_grouped_by_cost_centers()


@incoming_invoice_router.get("/get-sum-incoming-invoices-by-years-and-months")
def get_sum_incoming_invoices_by_years_and_months():
    return IncomingInvoiceController.sum_incoming_invoices_grouped_by_years_and_months()


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
