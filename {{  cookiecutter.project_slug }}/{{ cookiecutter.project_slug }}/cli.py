"""
cli.py
"""
import click

from {{ cookiecutter.project_slug }}.config import setup_logging


setup_logging()


@click.group()
def {{ cookiecutter.project_slug }}():
    """
    Commands for the project
    """


if __name__ == '__main__':
    {{ cookiecutter.project_slug }}
