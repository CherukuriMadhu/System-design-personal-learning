from abc import ABC, abstractmethod


# ---------------- Interfaces ----------------

class Payment(ABC):
    @abstractmethod
    def pay(self, amount):
        pass


class Balance(ABC):
    @abstractmethod
    def check_balance(self):
        pass


class Loan(ABC):
    @abstractmethod
    def apply_loan(self):
        pass


class FlightBooking(ABC):
    @abstractmethod
    def book_flight(self, source, destination):
        pass


# ---------------- Implementations ----------------

# QR Payment Service only needs Payment and Balance
class QRPayment(Payment, Balance):

    def pay(self, amount):
        print(f"✅ QR Payment Successful: ₹{amount}")

    def check_balance(self):
        print("💰 Available Balance: ₹15,000")


# Loan Service only needs Loan
class GooglePayLoan(Loan):

    def apply_loan(self):
        print("🏦 Loan Application Submitted")


# Flight Service only needs FlightBooking
class GooglePayFlight(FlightBooking):

    def book_flight(self, source, destination):
        print(f"✈️ Flight Booked from {source} to {destination}")


# ---------------- Main ----------------

qr = QRPayment()
qr.pay(2500)
qr.check_balance()

print("-" * 40)

loan = GooglePayLoan()
loan.apply_loan()

print("-" * 40)

flight = GooglePayFlight()
flight.book_flight("Hyderabad", "Delhi")
#ISP: One interface → One purpose. Don't force classes to implement methods they don't use.