"""Strategy Pattern 
Definition

The Strategy Pattern defines multiple algorithms/behaviors, encapsulates each one, and allows them to be swapped at runtime.

Think:

Strategy = Choose an algorithm

Real-world example

Google Maps:

Shortest Route
Fastest Route
Avoid Tolls
Walking Route

The destination stays the same, but the algorithm changes.

Before Strategy ❌
class Payment:

    def pay(self, payment_type):

        if payment_type == "UPI":
            print("Pay using UPI")

        elif payment_type == "CARD":
            print("Pay using Card")

        elif payment_type == "PAYPAL":
            print("Pay using PayPal")

Problem:

if/elif/else

keeps growing.

After Strategy ✅

Create separate strategies:

class UPIPayment:

    def pay(self):
        print("Pay using UPI")


class CardPayment:

    def pay(self):
        print("Pay using Card")


class PayPalPayment:

    def pay(self):
        print("Pay using PayPal")

Create Context:

class PaymentContext:

    def __init__(self, strategy):
        self.strategy = strategy

    def pay(self):
        self.strategy.pay()

Now:

payment = PaymentContext(UPIPayment())
payment.pay()

Output:

Pay using UPI

Change strategy:

payment = PaymentContext(CardPayment())
payment.pay()

Output:

Pay using Card

No change to PaymentContext.

Structure
              Context
                 |
                 ↓
             Strategy
            /    |    \
           /     |     \
         UPI   Card   PayPal
Interview definition

Strategy Pattern defines a family of algorithms, encapsulates each algorithm, and makes them interchangeable at runtime."""