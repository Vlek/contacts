"""
Shim on top of sqlite3 in order to hide away implementation details
relating to handling the contacts-specific actions.
"""
import sqlite3
from pathlib import Path
from sqlite3 import Cursor
from typing import Any


class Database:
    tableSchema: dict[str, list[str]] = {
        "people": [
            "id INTEGER PRIMARY KEY AUTOINCREMENT",
            "firstName",
            "middleName",
            "lastName",
        ],
    }

    def __init__(self, config_folder: str, database_file: str = "contacts.db") -> None:
        database_file_location: Path = Path(config_folder) / database_file

        self.connection = sqlite3.connect(database_file_location)
        self.cursor = self.connection.cursor()

        self._init_tables()

    def add_person(
        self,
        first_name: str,
        last_name: str,
        **kwargs,
    ) -> bool:
        self.cursor.execute(
            "INSERT INTO people VALUES (:id, :firstName, :middleName, :lastName)",
            {
                "id": None,
                "firstName": first_name,
                "middleName": None,
                "lastName": last_name,
            },
        )
        return True

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

    def get_people(self, **kwargs) -> list[Any]:
        """Returns from the people table given filters."""
        dbResponse: Cursor = self.cursor.execute("SELECT * FROM people")

        return dbResponse.fetchall()

    def _execute(self, dbCommand: str, data: dict) -> None:
        self.cursor.execute(dbCommand, data)

    def _init_tables(self) -> None:
        """Creates the underlying tables we use."""

        for tableName in Database.tableSchema.keys():
            self.cursor.execute(
                f"CREATE TABLE IF NOT EXISTS {tableName} ( {', '.join(Database.tableSchema[tableName])} );"
            )

        # log that tables were created

    def __del__(self):
        """Write out changes to the db on delete."""
        self.connection.commit()
        self.connection.close()

    def __len__(self):
        """Returns the number of people in the db."""
        dbResult: Cursor = self.cursor.execute("SELECT COUNT(1) FROM people")

        return dbResult.fetchone()[0]
