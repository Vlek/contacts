"""Command-line interface."""
import click


@click.command()
@click.version_option()
def main() -> None:
    """Contacts."""


if __name__ == "__main__":
    main(prog_name="contacts")  # pragma: no cover
