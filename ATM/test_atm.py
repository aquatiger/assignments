import unittest
from atm import AtmAccount


class TestAccountCreation(unittest.TestCase):
    def setUp(self):
        self.my_account = AtmAccount('Roger', 500.0, 0.01)
        self.bad_account = AtmAccount('Bad', 20000000, 10)

    def testbalance(self):
        self.assertEqual(self.my_account.balance, 500)
        self.assertIsNotNone(self.my_account)
        self.assertNotEqual(self.my_account.balance, 1)
        self.assertNotAlmostEqual(self.my_account.balance, 250, delta=10)

        self.assertNotEqual(self.bad_account.balance, 500)
        self.assertIsNotNone(self.bad_account)
        self.assertNotEqual(self.bad_account.balance, 1)
        self.assertNotAlmostEqual(self.bad_account.balance, 250, delta=10)

    def testinterest(self):
        self.assertEqual(self.my_account.intrestrate, .01)
        self.assertNotEqual(self.bad_account.intrestrate, 1)

    # def testdposit(self):
    #     self.assertEqual(self.)
