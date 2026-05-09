# lane.py
from customer import Customer

class Lane:
    def __init__(self, lane_type, capacity):
        self.lane_type = lane_type
        self.is_open = False
        self.customers = []
        self.capacity = capacity

    def open_lane(self):
        self.is_open = True

    def close_lane(self):
        self.is_open = False
        # Move customers to other lanes before closing (handled in simulation)

    def add_customer(self, customer: Customer):
        if len(self.customers) < self.capacity:
            self.customers.append(customer)

    def remove_customer(self):
        if self.customers:
            return self.customers.pop(0)  # Remove the first customer (FIFO)
        return None

    def is_full(self):
        return len(self.customers) >= self.capacity
