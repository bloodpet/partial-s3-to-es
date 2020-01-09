"""Console script for partial_s3_to_es."""
import sys
import click


@click.command()
def main(args=None):
    """Console script for partial_s3_to_es."""
    click.echo("Replace this message by putting your code into "
               "partial_s3_to_es.cli.main")
    click.echo("See click documentation at https://click.palletsprojects.com/")
    return 0


if __name__ == "__main__":
    sys.exit(main())  # pragma: no cover
