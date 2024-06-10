"""Command-line interface."""
import click

from contacts.contacts import Contacts


CONTACTS: Contacts = Contacts()


@click.group()
@click.version_option()
def contacts() -> None:
    """Contacts."""


# TODO, would also like a, c, and create
@contacts.command()
@click.option("--firstname")
@click.option("--lastname")
def add(firstname: str, lastname: str) -> None:
    click.echo("Adding new contact")
    CONTACTS.addPerson(firstname, lastname)


# TODO, Would also like d and del
@contacts.command()
def delete() -> None:
    click.echo("Select which contact to delete")


@contacts.command()
def get() -> None:
    response = CONTACTS.
    click.echo(response)


if __name__ == "__main__":
    contacts(prog_name="contacts")  # pragma: no cover
