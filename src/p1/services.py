"""
Systemy i ich depnencje

- users (clients)
- users (employees)
- access_rights
- logging
- metrics
- secret_storage

Zadnie do zrobienia:

 Poprawnie zainicjalizować system

 Poprawnie wyłączyć system


Context... Dependency Injection....

"""

class AccessRightsChecker:
    pass

class Logger:
    pass

class ClientStore:

    def __init__(self, a: AccessRightsChecker, l : Logger) -> None:
        super().__init__()


class EmployeeHrStore:
    pass


class MetricsExporter:
    pass

## MODEL
class Request:
    pass