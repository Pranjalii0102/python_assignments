from abc import ABC, abstractmethod

class PaymentStratergy(ABC):
    @abstractmethod
    def pay(self,amount):
        pass

class CreditCardPayment(PaymentStratergy):
    def pay(self,amount):
        print(f"\nPayment Successful!!!!!!")
        print(f"Amount paid : RS.{amount}")
        print(f"Payment method : Credit Card")

class PayPalPayment(PaymentStratergy):
    def pay(self, amount):
        print(f"\nPayment Successful!!!!!!")
        print(f"Amount paid : RS.{amount}")
        print(f"Payment method : PayPal")

class BitcoinPayment(PaymentStratergy):
    def pay(self, amount):
        print(f"\nPayment Successful!!!!!!")
        print(f"Amount paid : RS.{amount}")
        print(f"Payment method : Bitcoin")

class PaymentProcessor:
    def __init__(self,strategy):
        self.strategy=strategy

    def set_strategy(self,strategy):
        self.strategy=strategy

    def process_payment(self,amount):
        self.strategy.pay(amount)

def main():
    amount=float(input("Enter Payment Amount : Rs."))

    print("\nChoose Payment Method: ")
    print("1. Credit Card")
    print("2. PayPal")
    print("3. Bitcoin")

    choice=int(input("Enter your choice: "))

    if choice==1:
        strategy=CreditCardPayment()
    elif choice==2:
        strategy=PayPalPayment()
    elif choice==3:
        strategy=BitcoinPayment()
    else:
        print("Invalid Choice!")

    processor=PaymentProcessor(strategy)
    processor.process_payment(amount)

    print("\nDo you want to switch paymnet method?")
    print("1.Yes")
    print("2.No")

    switch=int(input("Enter choice :"))

    if switch==1:
        print("\nChoose new Payment Method: ")
        print("1. Credit Card")
        print("2. PayPal")
        print("3. Bitcoin")

        new_choice=int(input("Enter your choice: "))

        if new_choice==1:
            processor.set_strategy(CreditCardPayment())
        elif new_choice==2:
            processor.set_strategy(PayPalPayment())
        elif choice==3:
            processor.set_strategy(BitcoinPayment())
        else:
            print("Invalid Choice!")
            return 
        print("\nProcessing Payment again......")
        processor.process_payment(amount)

    else:
        print("\nThank You!!!")

if __name__=="__main__":
    main()


    

    