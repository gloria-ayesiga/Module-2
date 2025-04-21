
**#Title**
Python code used to develop a policy management system for an insurance company


#Outline

-Importing relevant functions
-Creation of relevant classes
-Implementing methods in each class
-Installing error handling code
-Split the classes in separate py files
-Creation of main python file to run all the py files.


#Code
from datetime import date, timedelta

**how it works**
#product.py
1. Creation of the Product class
2. Attributes such as name, policy_name, policy_term and status are defined in this class
3. Statuses such as active (which is the default at registration), suspended, and reactivated are defined

#product_manager.py
4. Creation of the Product_manager class
5. In this class more methods are implemented for policy product management
6. You're able to add, update, remove, suspend policy products
7. This class updates the Product class accordingly

#payment.py
8. Creation of the Payment class
9. Attributes such as premium, frequency, maturity_date and last_paid_date are defined in this class
10. Given the sensitivity of payments handling, it is prone to errors, so error handling code is installed to manage likely errors
11. The first try and except error handling mainly handles the datatype errors, and value entry errors
12. Methods such as next_due_date and processpayment are implemented
13. The next_due_date method calculates the date when the policy holder is supposed to pay their next premium depending on the frequency of payements at registration.
14. The inbuilt timedelta class helps us support this calculation
15. Further more, the processpayment method then calculates the days the policy holder has remaining to make their premium payment. 
    Penalities are calculated after the policy holder's due-date and a penalty of $1 is implemented.
16. A second error handling code is installed.

#policyholder.py
17. Creation of the Policyholder class
18. Defined attributes are name, policy_no, sum_assured, dob, inception_date, policy_term, product
19. Error handling code is installed to catch the value and typer errors.
20. Methods implemented in this class link to the Payment class attributes; such as add_payment, suspend, check_payement_status, reactivate and send-reminder.

#main.py
21. The main.py file brings everything together.
21. It runs all the py files in the order in which they're listed and returns the output based on the code that
    has been specified.
22. Two policyholders emma and ivan are created, products and payments details listed
22. A method that displays account details (display_account) is implemented and later called to display emma and ivan's details.


########
Notes
1. Ensure that all the py.files are in the same folder and directory

#######
Author: Gloria Eden Zion Ayesiga
Prepared for the fulfilment of Milestone 3 assignment for the BAN6420 course
Date: 4.21.2025
