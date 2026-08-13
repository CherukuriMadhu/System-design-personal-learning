State Pattern ⭐⭐⭐
Definition

The State Pattern allows an object to change its behavior when its internal state changes.

Think:

State = Behavior depends on current state

Real-world example

ATM:

No Card
   ↓
Card Inserted
   ↓
PIN Verified
   ↓
Transaction
   ↓
Card Ejected

The ATM behaves differently depending on its current state.

Before State ❌
class ATM:

    def __init__(self):
        self.state = "NO_CARD"

    def action(self):

        if self.state == "NO_CARD":
            print("Insert card")

        elif self.state == "CARD_INSERTED":
            print("Enter PIN")

        elif self.state == "PIN_VERIFIED":
            print("Withdraw money")

Problem:

As states increase:

if
elif
elif
elif
elif
...

The class becomes difficult to maintain.

After State ✅

Create separate state classes:

class NoCardState:

    def action(self):
        print("Insert card")


class CardInsertedState:

    def action(self):
        print("Enter PIN")


class PinVerifiedState:

    def action(self):
        print("Withdraw money")

Context:

class ATM:

    def __init__(self):
        self.state = NoCardState()

    def set_state(self, state):
        self.state = state

    def action(self):
        self.state.action()

Usage:

atm = ATM()

atm.action()

atm.set_state(CardInsertedState())
atm.action()

atm.set_state(PinVerifiedState())
atm.action()

Output:

Insert card
Enter PIN
Withdraw money

The behavior changes based on the current state.

Structure
                 ATM
                  |
               State
            /    |    \
           ↓     ↓     ↓
       NoCard  Card   PIN
Real-world examples
ATM
Vending Machine
Traffic Light
Media Player
Order Status
Interview definition

State Pattern allows an object to alter its behavior when its internal state changes, making the object appear to change its class.