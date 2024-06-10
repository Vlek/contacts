from contacts.config import Config
from contacts.database import Database


class Contacts:
    def __init__(self) -> None:
        # Note, we load configurations first. This might inform other decisions and
        #   things that we are loading below.
        self.config: Config = Config()
        self.database: Database = Database(str(self.config.config_folder_path))

    def addPerson(self, firstName: str, lastName: str) -> bool:
        return self.database.add_person(firstName, lastName)
