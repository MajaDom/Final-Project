import sqlalchemy
from sqlalchemy import func
from sqlalchemy.orm import Session
from sqlalchemy.exc import IntegrityError
from datetime import datetime
from app.outgoing_invoices.models import OutgoingInvoice
from app.outgoing_invoices.exceptions import OutgoingInvoiceDoesNotExistInTheDatabaseException, InvalidInputException


class OutgoingInvoiceRepository:
    def __init__(self, db: Session):
        self.db = db

    def create_outgoing_invoices(self, client_id, reference_code_invoice: str, start_date: str,
                                 date_of_transaction: str,
                                 certified_invoice: str, net: float = None, vat: float = None, gross: float = None,
                                 description_invoice: str = None, cost_center_id: int = None) -> OutgoingInvoice:
        """Method that creates new outgoing invoice"""
        try:
            if date_of_transaction is not None:
                conv_start_date = datetime.strptime(start_date, "%Y-%m-%d")
                conv_date_of_transaction = datetime.strptime(date_of_transaction, "%Y-%m-%d")
                if conv_start_date > conv_date_of_transaction:
                    raise InvalidInputException(message="Invalid date input.", code=400)
            if net < 0 or vat < 0 or gross < 0:
                raise InvalidInputException(message="Invalid number input.", code=400)
            outgoing_invoices = OutgoingInvoice(client_id=client_id, reference_code_invoice=reference_code_invoice,
                                                start_date=start_date, date_of_transaction=date_of_transaction,
                                                net=net, vat=vat, gross=gross, description_invoice=description_invoice,
                                                certified_invoice=certified_invoice, cost_center_id=cost_center_id)
            self.db.add(outgoing_invoices)
            self.db.commit()
            self.db.refresh(outgoing_invoices)
            return outgoing_invoices
        except IntegrityError as e:
            raise e
        except Exception as e:
            raise e

    def read_all_outgoing_invoices(self) -> list[OutgoingInvoice]:
        """Method that reads all outgoing invoices."""
        outgoing_invoice = self.db.query(OutgoingInvoice).all()
        return outgoing_invoice

    def read_outgoing_invoice_by_id(self, outgoing_invoice_id: int) -> OutgoingInvoice:
        """Method that reads outgoing invoice by id."""
        outgoing_invoice = self.db.query(OutgoingInvoice).filter(
            OutgoingInvoice.outgoing_invoice_id == outgoing_invoice_id).first()
        if outgoing_invoice is None:
            raise OutgoingInvoiceDoesNotExistInTheDatabaseException(
                message=f'Invoice with id {outgoing_invoice_id} not in the database.',
                code=400)
        return outgoing_invoice

    def update_outgoing_invoice_by_id(self, outgoing_invoice_id: int, client_id: int = None,
                                      reference_code_invoice: str = None,
                                      start_date: str = None, date_of_transaction: str = None,
                                      certified_invoice: str = None, net: float = None, vat: float = None,
                                      gross: float = None,
                                      description_invoice: str = None, cost_center_id: int = None) -> OutgoingInvoice:
        """Method that updates existing values in the database."""
        outgoing_invoice = self.db.query(OutgoingInvoice).filter(
            OutgoingInvoice.outgoing_invoice_id == outgoing_invoice_id).first()

        if outgoing_invoice is None:
            raise OutgoingInvoiceDoesNotExistInTheDatabaseException(
                message=f'Invoice with id {outgoing_invoice_id} not in the database.',
                code=400)
        if client_id is not None and client_id != "":
            outgoing_invoice.client_id = client_id
        if reference_code_invoice is not None and reference_code_invoice != "":
            outgoing_invoice.reference_code_invoice = reference_code_invoice
        if start_date is not None and start_date != "":
            outgoing_invoice.start_date = start_date
        if date_of_transaction is not None and date_of_transaction != "":
            outgoing_invoice.date_of_transaction = date_of_transaction
        if certified_invoice is not None and certified_invoice != "":
            outgoing_invoice.certified_invoice = certified_invoice
        if net is not None and net != "":
            outgoing_invoice.net = net
        if vat is not None and vat != "":
            outgoing_invoice.vat = vat
        if gross is not None and gross != "":
            outgoing_invoice.gross = gross
        if description_invoice is not None and description_invoice != "":
            outgoing_invoice.description_invoice = description_invoice
        if cost_center_id is not None and cost_center_id != "":
            outgoing_invoice.cost_center_id = cost_center_id

        self.db.add(outgoing_invoice)
        self.db.commit()
        self.db.refresh(outgoing_invoice)
        return outgoing_invoice

    def delete_outgoing_invoice_by_id(self, outgoing_invoice_id: int):
        """Method that deletes outgoing invoice by id."""
        outgoing_invoice = self.db.query(OutgoingInvoice).filter(
            OutgoingInvoice.outgoing_invoice_id == outgoing_invoice_id).first()
        if outgoing_invoice is None:
            raise OutgoingInvoiceDoesNotExistInTheDatabaseException(
                message=f'Invoice with id {outgoing_invoice_id} not in the database.',
                code=400)
        self.db.delete(outgoing_invoice)
        self.db.commit()
        return True

    def sum_outgoing_invoices_grouped_by_clients(self):
        """Method that sums gross total grouped by clients."""
        outgoing_invoices = self.db.query(OutgoingInvoice.client_id, func.sum(OutgoingInvoice.gross)).group_by(
            OutgoingInvoice.client_id)
        response = []
        for row in outgoing_invoices:
            dictionary = {row[0]: row[1]}
            response.append(dictionary)
        return response

    def sum_outgoing_invoices_grouped_by_cost_centers(self):
        """Method that sums gross total grouped by cost center."""
        outgoing_invoices = self.db.query(OutgoingInvoice.cost_center_id, func.sum(OutgoingInvoice.gross)).group_by(
            OutgoingInvoice.cost_center_id)
        response = []
        for row in outgoing_invoices:
            dictionary = {row[0]: row[1]}
            response.append(dictionary)
        return response

    def sum_outgoing_invoices_by_years_and_months(self):
        """Method that sums gross total grouped by years and months."""
        outgoing_invoices = self.db.query(OutgoingInvoice.start_date, func.sum(OutgoingInvoice.gross)).group_by(
            sqlalchemy.func.year(OutgoingInvoice.start_date),
            sqlalchemy.func.month(OutgoingInvoice.start_date)).order_by(OutgoingInvoice.start_date)
        response = []
        for row in outgoing_invoices:
            year_month = str(row[0])[0:7]
            dictionary = {year_month: row[1]}
            response.append(dictionary)
        return response


