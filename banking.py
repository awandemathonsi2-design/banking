import uuid


class SameAccount(Exception):
    pass


class DifferentBanks(Exception):
    pass


class InsufficientFunds(Exception):
    pass


class Account:
    def __init__(self, bank, id):
        self.bank = bank
        self.id = id

    @property
    def balance(self):
        return self.bank.get_balance(self.id)

    def deposit(self, amount):
        self.bank.deposit(self.id, amount)

    def withdraw(self, amount):
        self.bank.withdraw(self.id, amount)

    def __eq__(self, other):
        return (
            isinstance(other, self.__class__)
            and self.bank == other.bank
            and self.id == other.id
        )


class Bank:
    def __init__(self):
        self._accounts = {}
        self.transfer_log = []

    def create_account(self, balance=0):
        account_id = uuid.uuid4()
        self._accounts[account_id] = balance
        return Account(self, account_id)

    def get_balance(self, account_id):
        if account_id not in self._accounts:
            raise ValueError
        return self._accounts[account_id]

    def deposit(self, account_id, amount):
        if account_id not in self._accounts:
            raise ValueError
        if amount <= 0:
            raise ValueError("Deposit amount must be positive")
        self._accounts[account_id] += amount

    def withdraw(self, account_id, amount):
        if account_id not in self._accounts:
            raise ValueError
        if amount <= 0:
            raise ValueError("Withdrawal amount must be positive")
        if self._accounts[account_id] < amount:
            raise InsufficientFunds
        self._accounts[account_id] -= amount

    def transfer(self, account1, account2, amount):
        if account1 == account2:
            raise SameAccount
        if account1.bank != account2.bank:
            raise DifferentBanks
        if self._accounts[account1.id] < amount:
            raise InsufficientFunds
        self._accounts[account1.id] -= amount
        self._accounts[account2.id] += amount
        self.transfer_log.append((account1, account2, amount))

    def __repr__(self):
        return f"Bank(total_accounts={len(self._accounts)}, transfers={len(self.transfer_log)})"
