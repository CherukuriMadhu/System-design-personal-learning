"""Facade Pattern 
Definition

The Facade Pattern provides a simple interface to a complex subsystem.

Think:

Facade = One simple interface hiding complexity

Real-world example

When you order food through an app, you don't manually:

Find restaurant
 ↓
Check availability
 ↓
Process payment
 ↓
Prepare order
 ↓
Assign delivery
 ↓
Track delivery

You simply click:

Place Order

The app handles the complexity internally."""

#Before Facade ❌
class Inventory:
    def check(self):
        print("Checking inventory")


class Payment:
    def pay(self):
        print("Processing payment")


class Shipping:
    def ship(self):
        print("Shipping order")

#Client must know everything:

inventory = Inventory()
payment = Payment()
shipping = Shipping()

inventory.check()
payment.pay()
shipping.ship()

#The client is tightly coupled to multiple classes.

#After Facade ✅
class Inventory:

    def check(self):
        print("Checking inventory")


class Payment:

    def pay(self):
        print("Processing payment")


class Shipping:

    def ship(self):
        print("Shipping order")


class OrderFacade:

    def __init__(self):
        self.inventory = Inventory()
        self.payment = Payment()
        self.shipping = Shipping()

    def place_order(self):

        self.inventory.check()
        self.payment.pay()
        self.shipping.ship()

        print("Order placed successfully")

#Client:

order = OrderFacade()

order.place_order()
"""
Output:

Checking inventory
Processing payment
Shipping order
Order placed successfully

Client only knows:

place_order()
Structure
                 Client
                   |
                   ↓
                Facade
                   |
       ┌───────────┼───────────┐
       ↓           ↓           ↓
   Inventory     Payment    Shipping
Interview definition

Facade provides a simplified interface to a complex subsystem and hides its internal complexity from the client."""