""" Decorator Pattern 
Definition

The Decorator Pattern dynamically adds new behavior to an object without modifying its original class.

Think:

Decorator = Add features around an existing object

Real-world example

Coffee shop.

Start with:

Coffee

Then add:

+ Milk
+ Sugar
+ Whipped Cream

Instead of creating:

CoffeeWithMilk
CoffeeWithMilkAndSugar
CoffeeWithMilkSugarCream

we dynamically decorate the coffee.

Before Decorator ❌
class Coffee:

    def cost(self):
        return 50

Now suppose:

Coffee = ₹50
Coffee + Milk = ₹60
Coffee + Sugar = ₹55
Coffee + Milk + Sugar = ₹65

You might create many classes:

class CoffeeWithMilk:
    pass

class CoffeeWithSugar:
    pass

class CoffeeWithMilkAndSugar:
    pass

This causes class explosion.

After Decorator ✅
class Coffee:

    def cost(self):
        return 50


class MilkDecorator:

    def __init__(self, coffee):
        self.coffee = coffee

    def cost(self):
        return self.coffee.cost() + 10


class SugarDecorator:

    def __init__(self, coffee):
        self.coffee = coffee

    def cost(self):
        return self.coffee.cost() + 5

Now:

coffee = Coffee()

coffee = MilkDecorator(coffee)

coffee = SugarDecorator(coffee)

print(coffee.cost())

Output:

65

Because:

Coffee = 50
Milk = +10
Sugar = +5

Total = 65

We can dynamically add:

Coffee
 ↓
Milk
 ↓
Sugar
 ↓
Whipped Cream
Real-world examples
Java I/O streams
Middleware
Logging
Authentication
Compression
Coffee toppings
Interview definition

Decorator Pattern dynamically attaches additional responsibilities or behavior to an object without modifying its original class."""