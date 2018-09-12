class BankAccount:
    def __init__(self):
        self.branchID = 1
        self.branchName = "Wandegeya"

    def get_balance(self):
        if self.status == 'active':
            return self.amount
        else:
            raise ValueError

    def open(self):
        # personal details
        self.name = "Samantha"
        self.id = "12345"
        self.phone = "0777704340"
        self.dob = "06 December 1996"
        self.location = "Kampala"

        # bank creates account details
        self.accountNo = 104002001001
        self.accountName = self.name
        self.status = "active"
        self.amount = 0

    def deposit(self, amount):
        if self.status == 'active' and amount >= 0:
            # add requested amount to account
            self.amount += amount
        else:
            raise ValueError

    def withdraw(self, amount):
        if self.status == 'active':
            # subtract requested amount from account
            if amount <= (self.amount) and amount >= 0:
                self.amount = self.amount - amount
            else:
                raise ValueError
        else:
            raise ValueError

    def close(self):
        self.status = 'not-active'
