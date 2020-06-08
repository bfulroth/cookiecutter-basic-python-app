
from unittest import TestCase

from {{cookiecutter.script_slug.cli}} import main


class test_Cli(TestCase):

    @classmethod
    def setUpClass(cls) -> None:
        """
        Method used to setup fixtures for testing
        :return:
        """

        cls.var_name = ''
        pass

    def test_1(self):
        pass