"""Command-line interface."""
import click

from contacts.contacts import Contacts


CONTACTS: Contacts = Contacts()


@click.group()
@click.version_option()
def contacts() -> None:
    """Contacts."""
    click.echo("Hello world!")


# TODO, would also like a, c, and create
@contacts.command()
@click.option("--firstName")
@click.option("--lastName")
def add(firstName: str = "", lastName: str = "") -> None:
    click.echo("Adding new contact")
    CONTACTS.addPerson(firstName, lastName)


# TODO, Would also like d and del
@contacts.command()
def delete() -> None:
    click.echo("Select which contact to delete")


if __name__ == "__main__":
    contacts(prog_name="contacts")  # pragma: no cover
