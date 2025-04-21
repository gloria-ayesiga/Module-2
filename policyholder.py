
from datetime import date

class Policyholder:
     def __init__(self, name, policy_no, sum_assured, dob, inception_date, policy_term, product):

        try:
            if not all(isinstance(arg, str) for arg in [name, policy_no]):
                raise TypeError("Name and policy number must be strings.")
            if not isinstance(sum_assured, (int, float)):
                raise TypeError("Sum assured must be a number.")
            if not isinstance(dob, date) or not isinstance(inception_date, date):
                raise TypeError("Date Of Birth and inception date must be datetime.date objects.")
            if not isinstance(policy_term, int):
                raise TypeError("Policy term must be an integer.")
            if not hasattr(product, "status") or not hasattr(product, "policy_name"):
                raise ValueError("Product must have 'status' and 'policy_name' attributes.")
            self.name = name
            self.policy_no = policy_no
            self.sum_assured = sum_assured
            self.dob = dob  #  date object
            self.inception_date = inception_date  # date object
            self.policy_term = policy_term
            self.payments = []  # list of payments instances
            self.status = "active"  #this would be the default status upon registration
    
            if product.status == "active":    #to prevent assigning suspended prducts to new policy holders
              self.product = product
              print(f"Assigned product '{product.policy_name}' to {self.name}")
            else:
              raise ValueError(f"Cannot assign suspended product '{product.policy_name}' to policyholder '{self.name}'")
    
        except Exception as e:
            print(f"Error initializing Policyholder: {e}")


     def add_payment(self, payment):

        try:
            if not hasattr(payment, 'process_payment'):
                raise TypeError("Invalid payment object.")
            self.payments.append(payment)
        except Exception as e:
            print(f"Error adding payment: {e}")
    
     def suspend(self):
        if self.status == "active":
            self.status = "suspended"
            print(f"Policyholder {self.name} (Policy No: {self.policy_no}) has been suspended due to missed payments.")
        

     def reactivate(self):
        if self.status == "suspended":
            self.status = "active"
            print(f"Policyholder {self.name} (Policy No: {self.policy_no}) has been reactivated.")
        

     def display_status(self):
        print(f"{self.name}'s policy (#{self.policy_no}) is currently: {self.status}")

     def check_payment_status(self):
        today = date.today()
        for payment in self.payments:
            if payment.next_due_date() < today:
                self.suspend()
                return  # stop checking after first missed payment
        print(f"{self.name} is up to date with payments.")
    
     def process_payment(self, payment_date):
        if not self.payments:
            print(f"No payments found for {self.name}")
            return
        latest_payment = self.payments[-1]
        latest_payment.process_payment(payment_date)

        if self.status == "suspended":
            self.reactivate()

     def send_reminder(self):
        today = date.today()
        for payment in self.payments:
            due_date = payment.next_due_date()
            if 0 <= (due_date - today).days <= 5:
                print(f"Reminder: {self.name}'s payment is due on {due_date}")
            elif due_date < today:
                print(f"Overdue Alert: {self.name} missed a payment due on {due_date}")