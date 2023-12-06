import unittest

broken = unittest.skip("broken")


class MyTests(unittest.TestCase):
    @broken
    def test_good(self):
        assert False

    @broken("bar")
    def test_evil(self):
        assert False
