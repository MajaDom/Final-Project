# "SupplierDoesNotExistInTheDatabaseException is a class that inherits from the Exception class and has two attributes:
# message and code."
#
# Now, let's look at the code in more detail
class SupplierDoesNotExistInTheDatabaseException(Exception):

    def __init__(self, message, code):
        self.message = message
        self.code = code
