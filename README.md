# Banking System

A small object-oriented banking simulation in Python, built to practice
core OOP concepts, custom exceptions, and unit testing.

## Features

- Create accounts with an opening balance
- Deposit and withdraw funds directly on an account
- Transfer funds between accounts within the same bank
- Custom exceptions for insufficient funds, same-account transfers,
  and cross-bank transfers
- Full transfer log / audit trail
- Unique account IDs via `uuid.uuid4()`

## Run the tests

    python -m unittest test_banking.py -v

## Example usage

```python
import banking

bank = banking.Bank()
account = bank.create_account(balance=100)

account.deposit(50)      # balance: 150
account.withdraw(30)     # balance: 120
```

## What I learned

- Designing clean custom exception classes
- Encapsulating balance access via a `@property`
- Writing tests first (TDD) to define expected behaviour before implementation
- Extending an existing class design (adding `deposit`/`withdraw`) without
  breaking existing tests
