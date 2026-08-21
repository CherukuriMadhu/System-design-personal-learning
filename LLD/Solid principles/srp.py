"""class GooglePay:

    def validate_user(self):
        print("User validated")

    def process_payment(self, amount):
        print(f"Paid ₹{amount}")

    def send_receipt(self):
        print("Receipt sent")

    def save_transaction(self):
        print("Transaction saved")


gpay = GooglePay()

gpay.validate_user()
gpay.process_payment(500)
gpay.send_receipt()
gpay.save_transaction()
"""

class UserValidator:

    def validate(self):
        print("User validated")


class PaymentProcessor:

    def pay(self, amount):
        print(f"Paid ₹{amount}")


class ReceiptService:

    def send_receipt(self):
        print("Receipt sent")


class TransactionRepository:

    def save(self):
        print("Transaction saved")


validator = UserValidator()
payment = PaymentProcessor()
receipt = ReceiptService()
repo = TransactionRepository()

validator.validate()
payment.pay(500)
receipt.send_receipt()
repo.save()
#srp only 1 class for 1 responsibility