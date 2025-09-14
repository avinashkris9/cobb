import click


# -------------------
# GET COMMAND
# -------------------
@click.group()
def get_command():
    """Get information about Cobb or infrastructure."""
    pass


@get_command.command("info")
def info():
    """Print general Cobb info."""
    click.echo("Cobb CLI - DevOps Helper")
    click.echo("Author: Your Name")
    click.echo("Version: 0.1.0")
    click.echo("Supports CLI + Slack bot interactions")


@get_command.command("k8s")
@click.option(
    "--env",
    type=click.Choice(["test", "ort", "prod"], case_sensitive=False),
    required=True,
    help="Cluster environment",
)
def k8s(env):
    """Print cluster info for a given environment."""
    clusters = {
        "test": "Test cluster: test-cluster.example.com",
        "ort": "Ort cluster: ort-cluster.example.com",
        "prod": "Prod cluster: prod-cluster.example.com",
    }
    click.echo(clusters.get(env.lower(), "Unknown environment"))


# -------------------
# STATUS COMMAND
# -------------------
@click.command("status")
def status_command():
    """Print current Cobb system status."""
    click.echo("Cobb system is up and running!")


# -------------------
# VERSION COMMAND
# -------------------
@click.command("version")
def version_command():
    """Print Cobb CLI version."""
    click.echo("Cobb CLI version 0.1.0")
