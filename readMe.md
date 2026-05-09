Project README: Lane Management System
This repository contains a Python-based simulation for managing customer traffic in a store scenario. The system includes lanes for regular checkout and self-service checkout, with capacity limits and processing times. Below is an overview of the project's components and how to run it.

**Table of Contents:**

- Overview
- Directory Structure
- Installation
- Usage
- License

**Overview:** The simulation models a store's checkout lane system with multiple lanes for customers to checkout their items. It includes features such as random customer generation, lane capacity management, and lottery ticket assignment based on the number of items in a basket.

**Key Features:**
Regular Lane: Capacity: 5
Self-Service Lane: Capacity: 15
Maximum Items in Basket: 30
Maximum Initial Customers: 10
Maximum Customers in Store: 40
Checkout Time (per item):
Regular: 4 seconds
Self-Service: 6 seconds

**Directory Structure:**

```text
- lane_management_system/
  │
  ├── constants.py # Constants for simulation parameters
  ├── customer.py # Customer class with methods for checkout and lottery assignment
  ├── lane.py # Lane class representing a checkout lane
  ├── main.py # Entry point of the simulation
  └── simulation.py # Simulation logic, including generation of customers, lane management, and display status

**Dependencies:** Ensure you have Python 3.x installed on your system. The project uses standard libraries, so no additional packages are required.

**Usage:**

1. Run the simulation by executing the main.py file:
   python main.py

2. The simulation will generate customers, assign them to lanes, and display the status of each lane and the customers in the store. The output will include the number of customers in each lane, the items they have, and any lottery tickets assigned. Simulation will run continously, displaying the status of lanes and indivisual coustomers at fixed intervals(every 20 seconds). It will also indicate when all lanes are saturated.

3. End the simulation by pressing Ctrl+C in the terminal.

**License:** This project is licensed under the MIT License.
# laneManagementSystem
```
