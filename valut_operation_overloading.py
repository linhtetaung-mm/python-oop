# https://docs.python.org/3/reference/datamodel.html#special-method-names

class Vault:
    def __init__(self, dollar, nickel, quarter):
        self.dollar = dollar
        self.nickel = nickel
        self.quarter = quarter
    
    def __str__(self):
        return f"{self.dollar} Dollars, {self.nickel} Nickels, {self.quarter} Quarters"
    
    def __add__(self, other):
        dollars = self.dollar + other.dollar
        nickels = self.nickel + other.nickel
        quarters = self.quarter + other.quarter
        return Vault(dollars, nickels, quarters)

potter = Vault(100,20,13)
print(potter)

wesley = Vault(20, 12, 5)
print(wesley)

total = potter + wesley
print(total)
