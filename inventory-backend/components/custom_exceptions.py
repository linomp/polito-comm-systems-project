
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