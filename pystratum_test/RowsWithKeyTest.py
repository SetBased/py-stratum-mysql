"""
PyStratum
"""
from pystratum_test.TestDataLayer import TestDataLayer
from pystratum_test.StratumTestCase import StratumTestCase


class RowsWithKeyTest(StratumTestCase):
    # ------------------------------------------------------------------------------------------------------------------
    def test1(self):
        """
        Stored routine with designation type rows_with_key must return multi dimensional array.
        """
        from pystratum_test.TestDataLayer import TestDataLayer
        rows = TestDataLayer.tst_test_rows_with_key1(100)
        self.assertIsInstance(rows, dict)
        self.assertEqual(1, len(rows))
        self.assertTrue('a' in rows)
        self.assertTrue('b' in rows['a'])
        self.assertNotEqual(0, len(rows['a']['b']))
        self.assertTrue('c1' in rows['a']['b'])
        self.assertNotEqual(0, len(rows['a']['b']['c1']))

    # ------------------------------------------------------------------------------------------------------------------
    def test2(self):
        """
        Stored routine with designation type rows_with_key must return empty array when no rows are selected.
        """
        rows = TestDataLayer.tst_test_rows_with_key1(0)
        self.assertIsInstance(rows, dict)
        self.assertEqual(0, len(rows))

# ----------------------------------------------------------------------------------------------------------------------