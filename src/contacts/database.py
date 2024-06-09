"""
Shim on top of sqlite3 in order to hide away implementation details
relating to handling the contacts-specific actions.
"""
import sqlite3
from datetime import datetime


class Database:
    tableSchema: dict[str, list[str]] = {
        "people": [
            "id INTEGER PRIMARY KEY AUTOINCREMENT",
            "firstName",
            "middleName",
            "lastName",
        ],
    }

    def __init__(self, database_file: str = "contacts.db") -> None:
        self.connection = sqlite3.connect(database_file)
        self.cursor = self.connection.cursor()

    def add_person(
        self,
        first_name: str,
        last_name: str,
        **kwargs,
    ) -> bool:
        try:
            self.cursor.execute(
                "INSERT INTO people VALUES (:firstName, :lastName)",
                {
                    "firstName": first_name,
                    "lastName": last_name,
                },
            )
            return True
        except Exception as ex:
            return False

    def delete_person(
        self,
        personid: str,
    ) -> bool:
        return False

    def update_person(
        self,
        personid: str,
        fields: dict[str, str],
    ) -> bool:
        return False

    def get_person(
        self,
        personid: str,
        format: str,
    ) -> str:
        return "Not working yet. :C"

    def _execute(self, dbCommand: str, data: dict) -> None:
        self.cursor.execute(dbCommand, data)

    def _init_tables(self) -> None:
        """Creates the underlying tables we use."""

        for tableName in Database.tableSchema.keys():
            self.cursor.execute(
                f"CREATE TABLE IF NOT EXISTS {tableName} ( {', '.join(Database.tableSchema[tableName])} );"
            )

        # log that tables were created
