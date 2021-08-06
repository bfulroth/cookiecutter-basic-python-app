"""
Entry point to '{{cookiecutter.script_slug}}' command line script.
"""

from {{cookiecutter.script_slug}}.{{cookiecutter.script_slug}} import main
import click

# Using click to manage the command line interface
@click.command()
@click.option('--option_1', prompt="Replace with your prompt here", type=click.Path(exists=True),
              help="Replace with help menu text")
@click.option('--option_2', prompt="Replace your prompt for this option here" ,help="Replace with help menu text")
@click.option('--change_this_flag_name', is_flag=True, help="Replace with help menu text")
def run_main(option_1, option_2, change_this_flag_name):
    main(option_1=option_1, option_2=option_2, change_this_flag_name=change_this_flag_name)