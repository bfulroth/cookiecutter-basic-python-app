"""Module for testing {{cookiecutter.script_slug}}"""

from unittest import TestCase
from unittest.mock import patch
import pandas as pd
from click.testing import CliRunner
import numpy as np

from {{cookiecutter.script_slug.cli}} import main


class test_Cli(TestCase):

    def test_Cli_somthing(self):

        # Use the click CliRunner object for testing Click implemented Cli programs.
        runner = CliRunner()
        result = runner.invoke(main, ['--option_1', 'EXAMPLE_path_to_fixture_', 'option_2',
                                                        'input_2'])

        self.assertEqual(0, result.exit_code)


class test_somthing(TestCase):

    @classmethod
    def setUpClass(cls) -> None:
        """
        Method used to setup fixtures for testing
        :return:
        """

        cls.var_name = ''
        pass

    def test_somthing(self):
        pass