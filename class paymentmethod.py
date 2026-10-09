from abc import ABC, abstractmethod

class PaymentMethod(ABC):
    @abstractmethod
    def pay(self, amount):
        pass

class CreditCardPayment(PaymentMethod):
    def pay(self, amount):
        print("Charging {amount} "to credit card")

class Paypal (PaymentMethod):
    def pay(self, amount):
        print("Sending", amount, "via Paypal")

methods = [CreditCard(), Paypal()]
for m in methods:
    m.pay(49,99)