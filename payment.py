
from datetime import date, timedelta

class Payment:
    def __init__(self, premium, frequency, maturity_date, last_paid_date):

       try:
           if not isinstance(premium, (int, float)):
                raise ValueError("Premium must be a number.")  #datatype is important that is is correct
           if frequency not in ['monthly', 'quarterly', 'yearly']:  
                raise ValueError("Frequency must be 'monthly', 'quarterly', or 'yearly'.")
           if not isinstance(maturity_date, date) or not isinstance(last_paid_date, date):  
              raise TypeError("Maturity date and last paid date must be datetime.date objects.")
        
           self.premium = premium
           self.frequency = frequency
           self.maturity_date = maturity_date  # date object
           self.last_paid_date = last_paid_date
           self.penalties = 0
        
       except Exception as e:
            print(f"Error initializing Payment: {e}")

    def next_due_date(self):

        try:
           if self.frequency == 'monthly':
            return self.last_paid_date + timedelta(days=30)
           elif self.frequency == 'quarterly':
            return self.last_paid_date + timedelta(days=90)
           elif self.frequency == 'yearly':
            return self.last_paid_date + timedelta(days=365)
           else:
            return self.last_paid_date  # default
        except Exception as e:
            print(f"Error calculating next due date: {e}")
            return self.last_paid_date  # fallback
    
    def process_payment(self, payment_date):
        if payment_date > self.next_due_date():
            days_late = (payment_date - self.next_due_date()).days
            penalty = days_late * 1  # $1 per late day
            self.penalties += penalty
            print(f"Payment was late. Penalty of ${penalty} applied.")
        else:
            print("Payment received on time.")

        self.last_paid_date = payment_date  # update last paid date