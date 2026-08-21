from abc import ABC, abstractmethod


class PaymentMethod(ABC):

    @abstractmethod
    def pay(self, amount):
        pass


class GooglePayUPI(PaymentMethod):

    def pay(self, amount):
        print(f"GPay UPI Paid ₹{amount}")


class CreditCard(PaymentMethod):

    def pay(self, amount):
        print(f"Credit Card Paid ₹{amount}")


def make_payment(payment_method):
    payment_method.pay(700)


upi = GooglePayUPI()
card = CreditCard()

make_payment(upi)
make_payment(card)
# lsp - we can use any payment method without changing the make_payment function, adhering to the Liskov Substitution Principle (LSP).
# bcz both GooglePayUPI and CreditCard are subclasses of PaymentMethod, we can use them interchangeably in the make_payment function without any issues.    
# we can also use in the code but the make_payment function will work to hide PaymentMethod class name, allowing for easy extension of the payment methods without modifying the existing code.