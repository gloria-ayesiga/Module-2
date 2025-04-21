
from datetime import date
from product import Product
from payment import Payment
from policyholder import Policyholder

#product details
product1 = Product(name = "Education cover", policy_name= "Pru Edusave", policy_term = 20)
product2 = Product(name = "Life assurance", policy_name= "Pru Lifesaver", policy_term = 30)

#creating new policy holders
ivan = Policyholder(
    name="Ivan Jireh",
    policy_no="0025041",
    sum_assured=350000,
    dob=date(1987, 2, 12),
    policy_term = 20,
    inception_date=date(2023, 4, 1),
    product=product1
)

emma = Policyholder(
    name="Emma Aaron",
    policy_no="0025051",
    sum_assured=40000,
    dob=date(1985, 4, 3),
    policy_term = 30,
    inception_date=date(2023, 4, 1),
    product=product1
)

# payment details
payment1 = Payment(premium=5000, frequency='monthly', maturity_date= date(2043,4,1), last_paid_date=date(2025, 4, 19))
payment2 = Payment(premium=2000, frequency='yearly', maturity_date= date(2053, 4, 1), last_paid_date=date(2025, 4, 10))

ivan.add_payment(payment1)
emma.add_payment(payment2)

#process payments to keep statuses updated
ivan.check_payment_status()
emma.check_payment_status()

#display account details

def display_account(policyholder):
    print("\n--- Policyholder Account ---")
    print(f"Name: {policyholder.name}")
    print(f"Policy No: {policyholder.policy_no}")
    print(f"Sum Assured: {policyholder.sum_assured}")
    print(f"Product: {policyholder.product.policy_name}")
    print(f"Policy Term: {policyholder.policy_term} years")
    print(f"Status: {policyholder.status}")
    for i, p in enumerate(policyholder.payments, start=1):
        print(f"Payment {i}:")
        print(f"  Premium: {p.premium}")
        print(f"  Frequency: {p.frequency}")
        print(f"  Last Paid Date: {p.last_paid_date}")
        print(f"  Next Due Date: {p.next_due_date()}")
        print(f"  Total Penalties: ${p.penalties}")



display_account(ivan)
display_account(emma)