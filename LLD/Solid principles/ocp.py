"""class Payment:

    def pay(self, method, amount):

        if method == "UPI":
            print(f"UPI Payment ₹{amount}")

        elif method == "CARD":
            print(f"Card Payment ₹{amount}")

        elif method == "WALLET":
            print(f"Wallet Payment ₹{amount}")


payment = Payment()
payment.pay("UPI", 1000)"""


from abc import ABC, abstractmethod


class PaymentMethod(ABC):

    @abstractmethod
    def pay(self, amount):
        pass


class UPI(PaymentMethod):

    def pay(self, amount):
        print(f"UPI Payment ₹{amount}")


class CreditCard(PaymentMethod):

    def pay(self, amount):
        print(f"Card Payment ₹{amount}")


class Wallet(PaymentMethod):

    def pay(self, amount):
        print(f"Wallet Payment ₹{amount}")


class NetBanking(PaymentMethod):

    def pay(self, amount):
        print(f"Net Banking Payment ₹{amount}")


payment = NetBanking()
payment.pay(2500)
# we can extend the payment clasess without modifying the existing code, adhering to the Open/Closed Principle (OCP).
# new fetures = new classes 