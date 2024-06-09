from contacts.config import Config
from contacts.database import Database


class Contacts:
    def __init__(self) -> None:
        self.database: Database = Database()
        self.config: Config = Config()

    def addPerson(self, firstName: str, lastName: str) -> bool:
        return self.database.add_person(firstName, lastName)
