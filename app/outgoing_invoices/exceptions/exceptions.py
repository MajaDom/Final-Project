# This classes are used to raise exceptions when the user tries to access an outgoing invoice that does not exist in the
# database.
class OutgoingInvoiceDoesNotExistInTheDatabaseException(Exception):

    def __init__(self, message, code):
        self.message = message
        self.code = code


class OutgoingInvoicePaymentDoesNotExistInTheDatabaseException(Exception):

    def __init__(self, message, code):
        self.message = message
        self.code = code


class InvalidInputException(Exception):

    def __init__(self, message, code):
        self.message = message
        self.code = code
