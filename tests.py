
import json
from unittest import TestCase

from uczacz.app import Uczacz


class UczaczTest(TestCase):

    def test_data_loading(self):
        u = Uczacz()
        self.assertDictEqual(u.data, json.load('data/data.json'))
