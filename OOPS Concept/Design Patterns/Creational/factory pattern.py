"""Factory Method Pattern ⭐⭐⭐
Definition

The Factory Method Pattern provides a method for creating objects without exposing the object-creation logic to the client.

Problem

Suppose:

Payment
├── CreditCardPayment
├── UPIPayment
└── PayPalPayment

Without Factory:

if payment_type == "card":
    payment = CreditCardPayment()
elif payment_type == "upi":
    payment = UPIPayment()

Creation logic is spread throughout the application.

Factory centralizes it.

Code
class CreditCardPayment:
    def pay(self):
        print("Paid using Credit Card")


class UPIPayment:
    def pay(self):
        print("Paid using UPI")


class PaymentFactory:

    @staticmethod
    def create_payment(payment_type):

        if payment_type == "card":
            return CreditCardPayment()

        elif payment_type == "upi":
            return UPIPayment()

        else:
            raise ValueError("Invalid payment type")


payment = PaymentFactory.create_payment("upi")

payment.pay()

Output:

Paid using UPI
Structure
Client
  |
  v
Factory
  |
  ├──> CreditCardPayment
  |
  └──> UPIPayment
When to use?

When:

Object creation depends on some input or condition.

Common interview examples
Payment system
Notification system
Vehicle factory
Shape factory
Database connection
Document parser



"""

# pizza factory example
