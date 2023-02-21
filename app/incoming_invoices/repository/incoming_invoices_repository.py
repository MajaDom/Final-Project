from datetime import datetime
import sqlalchemy
from sqlalchemy import func
from sqlalchemy.orm import Session
from app.incoming_invoices.models import IncomingInvoice
from app.incoming_invoices.exceptions import IncomingInvoiceDoesNotExistInTheDatabaseException, InvalidInputException


class IncomingInvoiceRepository:
    def __init__(self, db: Session):
        self.db = db

    def create_incoming_invoices(self, reference_code_invoice: str, number_invoice: str, invoice_date: str,
                                 supplier_id: int, net: float = None, vat: float = None, gross: float = None,
                                 description_invoice: str = None, cost_center_id: int = None) -> IncomingInvoice:
        """Method that creates new incoming invoice."""
        try:
            datetime.strptime(invoice_date, "%Y-%m-%d")
            if net < 0 or vat < 0 or gross < 0:
                raise InvalidInputException(code=400, message="Invalid Input.")

            incoming_invoices = IncomingInvoice(reference_code_invoice=reference_code_invoice,
                                                number_invoice=number_invoice, invoice_date=invoice_date, net=net,
                                                vat=vat, gross=gross, description_invoice=description_invoice,
                                                supplier_id=supplier_id, cost_center_id=cost_center_id)
            self.db.add(incoming_invoices)
            self.db.commit()
            self.db.refresh(incoming_invoices)
            return incoming_invoices
        except InvalidInputException:
            raise InvalidInputException(code=400, message="Invalid Input.")
        except Exception as e:
            raise e

    def read_all_incoming_invoices(self) -> list[IncomingInvoice]:
        """Method that shows all incoming invoices."""
        incoming_invoices = self.db.query(IncomingInvoice).all()
        return incoming_invoices

    def read_incoming_invoice_by_id(self, incoming_invoice_id: int) -> IncomingInvoice:
        """Method that reads specific invoice based on invoice id."""
        incoming_invoice_repository = self.db.query(IncomingInvoice).filter(
            IncomingInvoice.incoming_invoice_id == incoming_invoice_id).first()
        if incoming_invoice_repository is None:
            raise IncomingInvoiceDoesNotExistInTheDatabaseException(
                message=f'Invoice with id {incoming_invoice_id} not in the database.',
                code=400)
        return incoming_invoice_repository

    def update_incoming_invoice_by_id(self, incoming_invoice_id: int, reference_code_invoice: str = None,
                                      number_invoice: str = None, invoice_date: str = None,
                                      supplier_id: int = None, net: float = None, vat: float = None,
                                      gross: float = None,
                                      description_invoice: str = None, cost_center_id: int = None) -> IncomingInvoice:
        """Method that updates values in the database based on invoice id."""
        incoming_invoice = self.db.query(IncomingInvoice).filter(
            IncomingInvoice.incoming_invoice_id == incoming_invoice_id).first()

        if incoming_invoice is None:
            raise IncomingInvoiceDoesNotExistInTheDatabaseException(
                message=f'Invoice with id {incoming_invoice_id} not in the database.',
                code=400)
        if reference_code_invoice is not None and reference_code_invoice != "":
            incoming_invoice.reference_code_invoice = reference_code_invoice
        if number_invoice is not None and number_invoice != "":
            incoming_invoice.number_invoice = number_invoice
        if invoice_date is not None and invoice_date != "":
            try:
                datetime.strptime(invoice_date, "%Y-%m-%d")
                incoming_invoice.invoice_date = invoice_date
            except InvalidInputException:
                raise InvalidInputException(code=400, message="Invalid Input.")
        if supplier_id is not None and supplier_id != "":
            incoming_invoice.supplier_id = supplier_id
        if net is not None and net != "":
            if net < 0:
                raise InvalidInputException(code=400, message="Invalid Input.")
            incoming_invoice.net = net
        if vat is not None and vat != "":
            if vat < 0:
                raise InvalidInputException(code=400, message="Invalid Input.")
            incoming_invoice.vat = vat
        if gross is not None and gross != "":
            if gross < 0:
                raise InvalidInputException(code=400, message="Invalid Input.")
            incoming_invoice.gross = gross
        if description_invoice is not None and description_invoice != "":
            incoming_invoice.description_invoice = description_invoice
        if cost_center_id is not None and cost_center_id != "":
            incoming_invoice.cost_center_id = cost_center_id
        self.db.add(incoming_invoice)
        self.db.commit()
        self.db.refresh(incoming_invoice)
        return incoming_invoice

    def delete_incoming_invoice_by_id(self, incoming_invoice_id: int) -> bool:
        """Method that deletes incoming invoice by id."""
        incoming_invoice = self.db.query(IncomingInvoice).filter(
            IncomingInvoice.incoming_invoice_id == incoming_invoice_id).first()
        if incoming_invoice is None:
            raise IncomingInvoiceDoesNotExistInTheDatabaseException(
                message=f'Invoice with id {incoming_invoice_id} not in the database.',
                code=400)
        self.db.delete(incoming_invoice)
        self.db.commit()
        return True

    def sum_incoming_invoices_grouped_by_suppliers(self) -> list[dict]:
        """Method that shows sum of incoming invoices grouped by suppliers."""
        incoming_invoices = self.db.query(IncomingInvoice.supplier_id, func.sum(IncomingInvoice.gross)).group_by(
            IncomingInvoice.supplier_id)
        response = []
        for row in incoming_invoices:
            dictionary = {row[0]: row[1]}
            response.append(dictionary)
        return response

    def sum_incoming_invoices_grouped_by_cost_center(self) -> list[dict]:
        """Method that shows sum of incoming invoices grouped by cost centers."""
        incoming_invoices = self.db.query(IncomingInvoice.cost_center_id, func.sum(IncomingInvoice.gross)).group_by(
            IncomingInvoice.cost_center_id)
        response = []
        for row in incoming_invoices:
            dictionary = {row[0]: row[1]}
            response.append(dictionary)
        return response

    def sum_incoming_invoices_by_years_and_months(self) -> list[dict]:
        """Method that shows sum of incoming invoices grouped by years and months."""
        incoming_invoices = self.db.query(IncomingInvoice.invoice_date, func.sum(IncomingInvoice.gross)).group_by(
            sqlalchemy.func.year(IncomingInvoice.invoice_date),
            sqlalchemy.func.month(IncomingInvoice.invoice_date)).order_by(IncomingInvoice.invoice_date)
        response = []
        for row in incoming_invoices:
            year_month = str(row[0])[0:7]
            dictionary = {year_month: row[1]}
            response.append(dictionary)
        return response
