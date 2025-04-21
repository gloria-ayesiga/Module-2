
class Product: # this class will handle the policy products and their current statuses 
    def __init__(self, name, policy_name, policy_term):
        self.name = name
        self.policy_name = policy_name
        self.policy_term = policy_term
        self.status = "active"

    def suspend(self):
        self.status = "suspended"
        print(f"Product '{self.policy_name}' has been suspended.")

    def reactivate(self):
        self.status = "active"
        print(f"Product '{self.policy_name}' has been reactivated.")

    def update(self, name=None, policy_name=None, policy_term=None):
        if name:
            self.name = name
        if policy_name:
            self.policy_name = policy_name
        if policy_term:
            self.policy_term = policy_term
        print(f"Product '{self.policy_name}' has been updated.")