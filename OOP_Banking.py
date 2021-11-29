#parent class

class User():
    def __init__(self, name, age, gender):
        self.name = name
        self.age = age
        self.gender = gender


    def show_details(self):
        print("Personal Details")
        print("")
        print("Name ", self.name)
        print("Age ", self.age)
        print("Gender ", self.gender)

#child class

class Bank(User):
    def __init__(self, name, age, gender):
        super().__init__(name, age, gender)
        self.balance = 0

    def deposit(self, amount):
        self.amount = amount
        self.balance = self.balance + amount
        print("Account Balance has been updated : £", self.balance)

    def withdraw(self, amount):
        self.amount = amount
        if self.amount > self.balance:
            print("You have insufficient funds | Balance Available : £", self.balance)
        else:
            self.balance = self.balance - self.amount
            print("Account balance has been updated : £" , self.balance)

    def view_balance(self):
        self.show_details()
        print("Your  Account balance is : £", self.balance)


p = Bank("Peter", 30, "Male")
p.deposit(2000)
p.withdraw(1400)
p.withdraw(220)
p.withdraw(80)
p.view_balance()


