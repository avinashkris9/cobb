# src/cobb/cli.py
import click
from .cobb_cli.commands import get_command, status_command, version_command


@click.group()
def cli():
    """Cobb CLI - Developer DevOps Assistant"""
    pass


cli.add_command(get_command)
cli.add_command(status_command)
cli.add_command(version_command)


def main():
    """Entrypoint for console scripts"""
    cli()


if __name__ == "__main__":
    main()
