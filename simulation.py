# simulation.py
import time
import random
from lane import Lane
from customer import Customer
from constants import *
import threading

class Simulation:
    def __init__(self):
        self.lanes = [Lane('regular', REGULAR_LANE_CAPACITY) for _ in range(5)] + \
                     [Lane('self-service', SELF_SERVICE_LANE_CAPACITY) for _ in range(1)]
        self.time = 0  # Simulation time in seconds
        #self.stop_event = threading.Event()

    def generate_customer(self):
        customer = Customer()
        customer.calculate_checkout_time(is_self_service=False)  # Default to regular lane for checkout time
        customer.assign_lottery_ticket()
        return customer

    def assign_customer_to_lane(self, customer: Customer):
    # Assign customers to self-service lane if items < 10 and self-service lane is not full
        if customer.items < 10:
            self_service_lane = self.lanes[-1]  # the self-service lane is the last in the list
            if not self_service_lane.is_open:
                self_service_lane.open_lane() # Open the self-service lane if it's closed
            if not self_service_lane.is_full():
                self_service_lane.add_customer(customer)
                return
    
        # Otherwise, assign to the first available regular lane
        for lane in self.lanes[:-1]:  # Excluding the self-service lane
            if lane.is_open and not lane.is_full():
                lane.add_customer(customer)
                return
    
        # If all open lanes are full, open a new lane if available
        for lane in self.lanes[:-1]:
            if not lane.is_open:
                lane.open_lane()
                lane.add_customer(customer)
                return
    
        # If all lanes are full and no more can be opened, display lane saturation
        print("All lanes are full. Lane saturation reached!")


    def process_checkout(self):
        for lane in self.lanes:
            if lane.is_open and lane.customers:
                customer = lane.customers[0]  # Get the first customer in the lane
                customer.checkout_time -= 1  # Process checkout for 1 second
                if customer.checkout_time <= 0:
                    lane.remove_customer()  # Customer leaves the lane after checkout


    def manage_lanes(self):
        # Close lanes if they are empty
        for lane in self.lanes:
            if lane.is_open and not lane.customers:
                lane.close_lane()
    
        # Open a new lane if all open lanes are full and there's a lane available to open
        open_lanes = [lane for lane in self.lanes if lane.is_open]
        if all(lane.is_full() for lane in open_lanes):
            for lane in self.lanes:
                if not lane.is_open:
                    lane.open_lane()
                    break  # Open one lane at a time
            

    def display_lane_status(self):
        print(f"Lane status at time {self.time // 60}:{str(self.time % 60).zfill(2)}")
        for i, lane in enumerate(self.lanes, 1):
            lane_type = 'Reg' if i <= 5 else 'Slf'
            status = 'open' if lane.is_open else 'closed'
            customers = ' '.join('*' for _ in lane.customers)
            print(f"L{i} ({lane_type}) --> {status} : {customers}")

            # Display details for each customer in the lane
            for customer in lane.customers:
                if lane_type == 'Reg':
                    lottery_status = "### LUCKY CUSTOMER ### wins a lottery ticket!" if customer.lottery_ticket else "hard luck, no lottery ticket this time!"
                    print(f"### Customer C{customer.id} ### --> items in basket: {customer.items}, {lottery_status}, time to process basket: {customer.checkout_time} Secs")
        print("\n")  # Adds a newline for better separation between intervals

        #print(f"Managing lanes at time {self.time}")  # Debug print
        #for lane in self.lanes:
            #print(f"Lane type: {lane.lane_type}, is_open: {lane.is_open}, customer count: {len(lane.customers)}")  # Debug print

    def run_simulation(self):
        # Open initial lanes
        self.lanes[0].open_lane()  # Open one regular lane
        self.lanes[-1].open_lane()  # Open the self-service lane

        # Add initial customers
        for _ in range(random.randint(1, MAX_INITIAL_CUSTOMERS)):
            customer = self.generate_customer()
            self.assign_customer_to_lane(customer)

        # Main simulation loop
        while self.time < SIMULATION_DURATION:
            # Generate new customers at random intervals
            if self.time % 30 == 0:  # Assuming new customers every 30 seconds
                for _ in range(random.randint(1, 3)):  # 1-3 new customers
                    if sum(len(lane.customers) for lane in self.lanes) < MAX_CUSTOMERS_IN_STORE:
                        customer = self.generate_customer()
                        self.assign_customer_to_lane(customer)

            # Process checkout for customers
            self.process_checkout()

            # Manage lanes based on current customer load
            self.manage_lanes()

            # Display lane status at fixed intervals
            if self.time % 20 == 0:  # Display status every 20 seconds
                self.display_lane_status()

            # Increment time
            self.time += 1
            time.sleep(1)  # Simulate real time; remove or adjust for faster simulation

        # End of simulation
        print("Simulation ended.")
