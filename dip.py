"""
    "Clients should not be forced to depend on interfaces they do not use."

"""
"""



class SBI:

    def transfer(self, amount):
        print(f"SBI transferred ₹{amount}")


class GooglePay:

    def __init__(self):
        self.bank = SBI()      # Direct dependency:---- 1 class is controled by another class

    def pay(self, amount):
        self.bank.transfer(amount)


gpay = GooglePay()
gpay.pay(500)


"""



from abc import ABC, abstractmethod


# ---------------- Interface ----------------

class Bank(ABC):

    @abstractmethod
    def transfer(self, amount):
        pass


# ---------------- Implementations ----------------

class SBI(Bank):

    def transfer(self, amount):
        print(f"SBI transferred ₹{amount}")


class HDFC(Bank):

    def transfer(self, amount):
        print(f"HDFC transferred ₹{amount}")


class ICICI(Bank):

    def transfer(self, amount):
        print(f"ICICI transferred ₹{amount}")


# ---------------- High-Level Module ----------------

class GooglePay:

    def __init__(self, bank):
        self.bank = bank

    def pay(self, amount):
        self.bank.transfer(amount)


# ---------------- Main ----------------

gpay = GooglePay(SBI())
gpay.pay(500)

gpay = GooglePay(HDFC())
gpay.pay(1000)

gpay = GooglePay(ICICI())
gpay.pay(1500)


# it directly depends on the Bank interface, allowing for easy extension of new banks without modifying the existing code, adhering to the Dependency Inversion Principle (DIP).    
# GooglePay depends on the Bank interface, not on any specific bank.
"""
           Bank (Interface)
           ▲      ▲      ▲
           │      │      │
         SBI    HDFC   ICICI
              ▲
              │
         GooglePay
         
         
"""