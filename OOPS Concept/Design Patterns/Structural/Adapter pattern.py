""" Adapter Pattern 
Definition

The Adapter Pattern allows incompatible interfaces to work together.

Think:

Adapter = Translator

Real-world example

You have:

Indian Plug → Adapter → US Socket

The plug and socket have different interfaces.

The adapter makes them compatible.

Before Adapter ❌

Suppose your application expects:

class PaymentProcessor:

    def pay(self):
        print("Processing payment")

But a third-party library provides:

class PayPal:

    def make_payment(self):
        print("PayPal payment")

The method names don't match.

Application expects:

pay()

PayPal provides:

make_payment()

Directly:

paypal = PayPal()
paypal.pay()

This doesn't work.

After Adapter ✅

Create an adapter:

class PayPal:

    def make_payment(self):
        print("PayPal payment")


class PayPalAdapter:

    def __init__(self, paypal):
        self.paypal = paypal

    def pay(self):
        self.paypal.make_payment()

Now:

paypal = PayPal()

payment = PayPalAdapter(paypal)

payment.pay()

Output:

PayPal payment

The application only knows:

pay()

The adapter translates:

pay()
 ↓
make_payment()
Structure
Client
  ↓
Expected Interface
  ↓
Adapter
  ↓
Existing Class
Interview definition

Adapter Pattern converts the interface of one class into another interface expected by the client, allowing incompatible classes to work together."""