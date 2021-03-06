from pystratum_middle.exception.ResultException import ResultException

from test.StratumTestCase import StratumTestCase


class Row0Test(StratumTestCase):
    # ------------------------------------------------------------------------------------------------------------------
    def test1(self):
        """
        Stored routine with designation type row0 must return null.
        """
        ret = self._dl.tst_test_row0a(0)
        self.assertIsNone(ret)

    # ------------------------------------------------------------------------------------------------------------------
    def test2(self):
        """
        Stored routine with designation type row0 must return 1 row.
        """
        ret = self._dl.tst_test_row0a(1)
        self.assertIsInstance(ret, dict)

    # ------------------------------------------------------------------------------------------------------------------
    def test3(self):
        """
        An exception must be thrown when a stored routine with designation type row0 returns more than 1 rows.
        @expectedException Exception
        """
        with self.assertRaises(ResultException):
            self._dl.tst_test_row0a(2)

# ----------------------------------------------------------------------------------------------------------------------
