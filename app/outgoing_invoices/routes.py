from fastapi import APIRouter
from app.outgoing_invoices.controller import OutgoingInvoicePaymentController, OutgoingInvoiceController
from app.outgoing_invoices.schemas import *

outgoing_invoice_router = APIRouter(tags=["Outgoing Invoices"], prefix="/api/outgoing-outgoing_invoices")


@outgoing_invoice_router.post("/create-new-outgoing-invoice", response_model=OutgoingInvoiceSchema)
def create_outgoing_invoice(outgoing_invoice: OutgoingInvoiceSchemaIN):
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


@outgoing_invoice_router.get("/get-all-outgoing_invoices", response_model=list[OutgoingInvoiceSchema])
def get_all_outgoing_invoices():
    return OutgoingInvoiceController.get_all_outgoing_invoices()


@outgoing_invoice_router.get("/get-outgoing-invoice-by-id", response_model=OutgoingInvoiceSchema)
def get_outgoing_invoice_by_id(outgoing_invoice_id: int):
    return OutgoingInvoiceController.get_outgoing_invoice_by_id(outgoing_invoice_id=outgoing_invoice_id)


@outgoing_invoice_router.put("/update-outgoing-invoice-data", response_model=OutgoingInvoiceSchema)
def update_outgoing_invoice_by_id(outgoing_invoice_id: int, outgoing_invoice: OutgoingInvoiceSchemaUpdate):
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
    return OutgoingInvoiceController.delete_outgoing_invoice_by_id(outgoing_invoice_id)


@outgoing_invoice_router.get("/get-sum-outgoing_invoices-by-client")
def get_all_outgoing_invoices_grouped_by_clients():
    return OutgoingInvoiceController.sum_outgoing_invoices_grouped_by_clients()


@outgoing_invoice_router.get("/get-sum-outgoing_invoices-by-cost-centers")
def get_all_outgoing_invoices_grouped_by_cost_centers():
    return OutgoingInvoiceController.sum_outgoing_invoices_grouped_by_cost_centers()


@outgoing_invoice_router.get("/get-sum-outgoing_invoices-by-years-and-months")
def get_sum_outgoing_invoices_by_years_and_months():
    return OutgoingInvoiceController.sum_outgoing_invoices_grouped_by_years_and_months()


@outgoing_invoice_router.get("/get-difference-outgoing_invoices-gross-and-invoice-payments")
def get_difference_outgoing_invoice_gross_and_invoice_payments():
    return OutgoingInvoiceController.find_difference_outgoing_invoice_gross_and_invoice_payments()


outgoing_invoice_payments_router = APIRouter(tags=["Outgoing Invoice Payments"],
                                             prefix="/api/outgoing-invoice-payments")


@outgoing_invoice_payments_router.post("/create-new-outgoing-invoice-payments",
                                       response_model=OutgoingInvoicePaymentSchema)
def create_outgoing_invoice_payment(outgoing_invoice_payment: OutgoingInvoicePaymentIN):
    return OutgoingInvoicePaymentController.create_outgoing_invoice_payment(
        payment_date=outgoing_invoice_payment.payment_date,
        payment_description=outgoing_invoice_payment.payment_description,
        payment=outgoing_invoice_payment.payment, outgoing_invoice_id=outgoing_invoice_payment.outgoing_invoice_id)


@outgoing_invoice_payments_router.get("/get-all-outgoing_invoices-payments",
                                      response_model=list[OutgoingInvoicePaymentSchema])
def get_all_outgoing_invoices_payments():
    return OutgoingInvoicePaymentController.get_all_outgoing_invoices_payments()


@outgoing_invoice_payments_router.get("/get-outgoing-invoice-payments-by-outgoing-invoice-id",
                                      response_model=list[OutgoingInvoicePaymentSchema])
def get_outgoing_invoice_payments_by_outgoing_invoice_id(outgoing_invoice_id: int):
    return OutgoingInvoicePaymentController.get_outgoing_invoice_payments_by_outgoing_invoice_id(
        outgoing_invoice_id=outgoing_invoice_id)


@outgoing_invoice_payments_router.put("/update-outgoing-invoice-payment-by-id",
                                      response_model=OutgoingInvoicePaymentSchema)
def update_outgoing_invoice_payment_by_id(outgoing_invoice_payment_id: int,
                                          outgoing_invoice_payment: OutgoingInvoicePaymentUpdate):
    return OutgoingInvoicePaymentController.update_outgoing_invoice_payment_by_id(
        outgoing_invoice_payment_id=outgoing_invoice_payment_id,
        payment_date=outgoing_invoice_payment.payment_date,
        payment_description=outgoing_invoice_payment.payment_description,
        payment=outgoing_invoice_payment.payment,
        outgoing_invoice_id=outgoing_invoice_payment.outgoing_invoice_id)


@outgoing_invoice_payments_router.delete("/delete-outgoing-invoice-payment-by-id")
def delete_outgoing_invoice_payment_by_id(outgoing_invoice_payment_id: int):
    return OutgoingInvoicePaymentController.delete_outgoing_invoice_payment_by_id(
        outgoing_invoice_payment_id=outgoing_invoice_payment_id)


@outgoing_invoice_payments_router.get("/get-sum-outgoing-invoice-payments")
def get_sum_outgoing_invoice_payments():
    return OutgoingInvoicePaymentController.sum_outgoing_invoice_payments()
