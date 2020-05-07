"""Randomly pick customer and print customer info"""
import random
from customers import get_customers_from_file

def pick_winner(customers):

    random_customer = random.choice(customers)

    print(f"Tell {random_customer.name} at {random_customer.email} that they've won ")

def run_raffle():
    customers = get_customers_from_file ("customers.txt")
    pick_winner(customers)

if __name__ == "__main__":
    run_raffle()



# Add code starting here

# Hint: remember to import any functions you need from
# other files or libraries
