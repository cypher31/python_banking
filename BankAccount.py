from Transaction import Transaction
import datetime

class BankAccount:
    
    def __init__(self, name, initialBalance) -> None:
        self.allTransactions = []
        self.accountNumberSeed = 1234567890
        self.Number = self.newAccountNumber(self.accountNumberSeed)
        self.Owner = name
        self.Balance = self.MakeDeposit(initialBalance, datetime.datetime.now(), "Initial balance")
        pass

    def generateBalance(self) -> float:
        balance = 0
        for transaction in self.allTransactions:
            balance += transaction.amount
        self.Balance = balance
        return balance
    
    def newAccountNumber(self, seed):
        accountNumber = self.accountNumberSeed + 1
        print("The generated account number is:", accountNumber)
        return accountNumber

    # Accepts amount of deposite, date/time of deposit, and any notes associated with the deposit
    def MakeDeposit(self, amount, date, note):
        if amount <= 0:
            print("Amount is less than 0!")
        else:
            deposit = Transaction(amount, date, note)
            self.allTransactions.append(deposit)
            print("After your most recent deposit, your new balance is:", self.generateBalance())
        pass

    # Accepts amount of withdrawal, date/time of deposit, and any notes associated with the deposit
    def MakeWithdrawal(self, amount, date, note):
        if amount <= 0:
            print("Amount is less than 0!")
        elif self.Balance - amount < 0:
            print("Overdrafting!")
        else:
            withdrawal = Transaction(-amount, date, note)
            self.allTransactions.append(withdrawal)
            print("After your most recent withdrawal, your new balance is:", self.generateBalance())
        pass

    def provideTransactions(self, transactions: Transaction):
        transactions = self.allTransactions

        for item in transactions:
            amount = item.amount
            dateStamp = item.date
            note = item.note
            print(f'Transaction amount: {amount};', f'Date of Transaction: {dateStamp};', f'Transaction Note: {note}')