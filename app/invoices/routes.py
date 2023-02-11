from fastapi import APIRouter
from app.invoices.controller import OutgoingInvoiceController
from app.invoices.schemas import *

outgoing_invoice_router = APIRouter(tags=["Outgoing Invoices"], prefix="/api/outgoing-invoices")


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
