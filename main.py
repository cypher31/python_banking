import datetime
from BankAccount import BankAccount

def createNewBankAccount(name, initialAmount):
    account = BankAccount(name, initialAmount)
    balance = BankAccount.generateBalance(account)
    return account

account = createNewBankAccount("name", 1000)

account.MakeDeposit(5000, datetime.datetime.now(), "Bonus Baby!")

account.MakeWithdrawal(3000, datetime.datetime.now(), "Engagement ring...")

print(account.provideTransactions(account))