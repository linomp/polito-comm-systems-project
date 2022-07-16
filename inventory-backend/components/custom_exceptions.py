
class WrongPinException(Exception):
    pass


class InvalidCardIDException(Exception):
    pass

class InvalidUserIDException(Exception):
    pass

class InvalidCostumerIDException(Exception):
    pass

class CustomerCreationException(Exception):
    pass


class DefaultUserCreationException(Exception):
    pass


class DatabaseException(Exception):
    pass

class NoPermissionException(Exception):
    pass

class NotAssociatedException(Exception):
    pass

class AlreadyClientException(Exception):
    pass

class AlreadyEmployeeException(Exception):
    pass

class InvalidItemException(Exception):
    pass

class InvalidRFIDException(Exception):
    pass

class InvalidEmailException(Exception):
    pass

class InvalidNameException(Exception):
    pass

class AlreadyRentedException(Exception):
    pass

class AlreadyRentedbymeException(Exception):
    pass

class AlreadyRFIDException(Exception):
    pass

class InvalidIDException(Exception):
    pass

class NotClientException(Exception):
    pass

class ActiveFlagException(Exception):
    pass