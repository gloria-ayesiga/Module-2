
from product import Product

class ProductManager:    #this class will handle a collection of products with their statuses
    def __init__(self):
        self.products = {}  # key: policy_name, value: Product object

    def add_product(self, product):
        if product.policy_name in self.products:
            print(f"Product '{product.policy_name}' already exists.")
        else:
            self.products[product.policy_name] = product
            print(f"Product '{product.policy_name}' added successfully.")

    def update_product(self, policy_name, **kwargs):
        product = self.products.get(policy_name)
        if product:
            product.update(**kwargs)
        else:
            print(f"Product '{policy_name}' not found.")

    def suspend_product(self, policy_name):
        product = self.products.get(policy_name)
        if product:
            product.suspend()
        else:
            print(f"Product '{policy_name}' not found.")

    def reactivate_product(self, policy_name):
        product = self.products.get(policy_name)
        if product:
            product.reactivate()
        else:
            print(f"Product '{policy_name}' not found.")

    def remove_product(self, policy_name):
        if policy_name in self.products:
            del self.products[policy_name]
            print(f"Product '{policy_name}' has been permanently removed.")
        else:
            print(f"Product '{policy_name}' does not exist.")