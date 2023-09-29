"""Employee pay calculator."""
"""ENTER YOUR SOLUTION HERE!"""


class Employee:
    def __init__(
        self, name, wages=0, hours=0, salary=0, comission=0, contracts=0, bonus=0
    ):
        self.name = name
        self.wages = wages
        self.hours = hours
        self.salary = salary
        self.comission = comission
        self.contracts = contracts
        self.bonus = bonus

    def get_pay(self):
        comission = 0
        if self.contracts:
            comission = self.comission * self.contracts
        elif self.bonus:
            comission = self.bonus

        return self.salary + (self.wages * self.hours) + comission

    def __str__(self):
        if self.salary != 0:
            if self.comission:
                return f"{self.name} works on a monthly salary of {self.salary} and receives a commission for {self.contracts} contract(s) at {self.comission}/contract. Their total pay is {self.get_pay()}."
            elif self.bonus:
                return f"{self.name} works on a monthly salary of {self.salary} and receives a bonus commission of {self.bonus}. Their total pay is {self.get_pay()}."
            else:
                return f"{self.name} works on a monthly salary of {self.salary}. Their total pay is {self.get_pay()}."
        else:
            if self.comission:
                return f"{self.name} works on a contract of {self.hours} hours at {self.wages}/hour and receives a commission for {self.contracts} contract(s) at {self.comission}/contract. Their total pay is {self.get_pay()}."
            elif self.bonus:
                return f"{self.name} works on a contract of {self.hours} hours at {self.wages}/hour and receives a bonus commission of {self.bonus}. Their total pay is {self.get_pay()}."
            else:
                return f"{self.name} works on a contract of {self.hours} hours at {self.wages}/hour. Their total pay is {self.get_pay()}."


# Billie works on a monthly salary of 4000.  Their total pay is 4000.
billie = Employee("Billie", salary=4000)
# Charlie works on a contract of 100 hours at 25/hour.  Their total pay is 2500.
charlie = Employee("Charlie", wages=25, hours=100)

# Renee works on a monthly salary of 3000 and receives a commission for 4 contract(s) at 200/contract.  Their total pay is 3800.
renee = Employee("Renee", salary=3000, contracts=4, comission=200)

# Jan works on a contract of 150 hours at 25/hour and receives a commission for 3 contract(s) at 220/contract.  Their total pay is 4410.
jan = Employee("Jan", wages=25, hours=150, contracts=3, comission=220)

# Robbie works on a monthly salary of 2000 and receives a bonus commission of 1500.  Their total pay is 3500.
robbie = Employee("Robbie", salary=2000, bonus=1500)

# Ariel works on a contract of 120 hours at 30/hour and receives a bonus commission of 600.  Their total pay is 4200.
ariel = Employee("Ariel", hours=120, wages=30, bonus=600)


list = {billie, charlie, renee, jan, ariel}

for i in list:
    print(str(i))
