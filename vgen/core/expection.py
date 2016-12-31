class ImproperlyConfigured(Exception):
    """Vgen is somehow improperly configured"""
    pass


class FieldDoesNotExist(Exception):
    """The requested model field does not exist"""
    pass


class PermissionDenied(Exception):
    """The user did not have permission to do that"""
    pass
