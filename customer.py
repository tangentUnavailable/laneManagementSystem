# customer.py
import random
from constants import MAX_ITEMS_IN_BASKET, CHECKOUT_TIME_REGULAR, CHECKOUT_TIME_SELF_SERVICE

class Customer:
    id_counter = 1

    def __init__(self):
        self.id = Customer.id_counter
        Customer.id_counter += 1
        self.items = random.randint(1, MAX_ITEMS_IN_BASKET)
        self.checkout_time = 0
        self.lottery_ticket = False

    def calculate_checkout_time(self, is_self_service):
        if is_self_service:
            self.checkout_time = self.items * CHECKOUT_TIME_SELF_SERVICE
        else:
            self.checkout_time = self.items * CHECKOUT_TIME_REGULAR

    def assign_lottery_ticket(self):
        if self.items >= 10:
            self.lottery_ticket = random.choice([True, False])  # 50% chance to get a ticket    

