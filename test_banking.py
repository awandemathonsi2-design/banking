import banking
import unittest


class TestBanking(unittest.TestCase):
    def test_simple_transaction(self):
        bank = banking.Bank()
        account1 = bank.create_account(balance=100)
        account2 = bank.create_account()
        bank.transfer(account1, account2, 50)
        self.assertEqual(account1.balance, 50)
        self.assertEqual(account2.balance, 50)

    def test_insufficient_funds(self):
        bank = banking.Bank()
        account1 = bank.create_account(balance=100)
        account2 = bank.create_account()
        with self.assertRaises(banking.InsufficientFunds):
            bank.transfer(account1, account2, 200)

    def test_cannot_transfer_to_same_account(self):
        bank = banking.Bank()
        account1 = bank.create_account(balance=100)
        with self.assertRaises(banking.SameAccount):
            bank.transfer(account1, account1, 50)

    def test_cannot_transfer_between_different_banks(self):
        bank1 = banking.Bank()
        bank2 = banking.Bank()
        account1 = bank1.create_account(balance=100)
        account2 = bank2.create_account()
        with self.assertRaises(banking.DifferentBanks):
            bank1.transfer(account1, account2, 50)

    def test_keeps_transfer_log(self):
        bank = banking.Bank()
        account1 = bank.create_account(balance=100)
        account2 = bank.create_account()
        bank.transfer(account1, account2, 50)
        self.assertEqual(len(bank.transfer_log), 1)
        self.assertEqual(bank.transfer_log[0], (account1, account2, 50))

    def test_deposit(self):
        bank = banking.Bank()
        account = bank.create_account(balance=100)
        account.deposit(50)
        self.assertEqual(account.balance, 150)

    def test_deposit_into_empty_account(self):
        bank = banking.Bank()
        account = bank.create_account()
        account.deposit(75)
        self.assertEqual(account.balance, 75)

    def test_deposit_non_positive_amount_raises(self):
        bank = banking.Bank()
        account = bank.create_account(balance=100)
        with self.assertRaises(ValueError):
            account.deposit(0)
        with self.assertRaises(ValueError):
            account.deposit(-10)

    def test_withdraw(self):
        bank = banking.Bank()
        account = bank.create_account(balance=100)
        account.withdraw(30)
        self.assertEqual(account.balance, 70)

    def test_withdraw_full_balance(self):
        bank = banking.Bank()
        account = bank.create_account(balance=100)
        account.withdraw(100)
        self.assertEqual(account.balance, 0)

    def test_withdraw_insufficient_funds(self):
        bank = banking.Bank()
        account = bank.create_account(balance=100)
        with self.assertRaises(banking.InsufficientFunds):
            account.withdraw(150)

    def test_withdraw_non_positive_amount_raises(self):
        bank = banking.Bank()
        account = bank.create_account(balance=100)
        with self.assertRaises(ValueError):
            account.withdraw(0)
        with self.assertRaises(ValueError):
            account.withdraw(-10)


if __name__ == "__main__":
    unittest.main()
