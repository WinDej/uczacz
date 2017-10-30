
import json
from unittest import TestCase

from uczacz.app import Uczacz


class UczaczTest(TestCase):

    def setUp(self):
        self.u = Uczacz()

    def test_data_loading(self):
        src = 'data/data.json'
        with open(src, 'r') as f:
            data = json.load(f)

        self.assertDictEqual(self.u.data, data)
