from vgen.core import Configuration
from vgen import config

from unittest import TestCase


class TestConfiguration(TestCase):

    def test_if_config_file_is_valid(self):
        for key, value in config.__dict__.items():
            if not key.startswith("__"):
                output = Configuration.is_valid(key)
                self.assertTrue(output)


