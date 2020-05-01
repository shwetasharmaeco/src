melon_cost = 1.00

def correct_pay(file_name):

  file= open(file_name)

  for line in file:
    line= line.rstrip()
    order_data= line.split("|")

    customer_name = order_data[1]
    melon_count = float(order_data[2])
    current_pay = float(order_data[3]) 
    expected_pay = melon_count * melon_cost

    
    print(f"{customer_name} paid ${current_pay},",
          f"expected ${expected_pay:.2f}")
    
    payment_status = "underpaid" if expected_pay < current_pay else "overpaid"
  

    print(f"{customer_name} was {payment_status} by ${abs(current_pay - expected_pay):.2f}")

  file.close()


correct_pay("customer-orders.txt")



# customer1_name = "Joe"
# customer1_melons = 5
# customer1_paid = 5.00

# customer2_name = "Frank"
# customer2_melons = 6
# customer2_paid = 6.00

# customer3_name = "Sally"
# customer3_melons = 3
# customer3_paid = 3.00

# customer4_name = "Sean"
# customer4_melons = 9
# customer4_paid = 9.50

# customer5_name = "David"
# customer5_melons = 4
# customer5_paid = 4.00

# customer6_name = "Ashley"
# customer6_melons = 3
# customer6_paid = 2.00

# customer1_expected = customer1_melons * melon_cost
# if customer1_expected != customer1_paid:
#     print(f"{customer1_name} paid ${customer1_paid:.2f},",
#           f"expected ${customer1_expected:.2f}"
#           )

# customer2_expected = customer2_melons * melon_cost
# if customer2_expected != customer2_paid:
#     print(f"{customer2_name} paid ${customer2_paid:.2f},",
#           f"expected ${customer2_expected:.2f}"
#           )

# customer3_expected = customer3_melons * melon_cost
# if customer3_expected != customer3_paid:
#     print(f"{customer3_name} paid ${customer3_paid:.2f},",
#           f"expected ${customer3_expected:.2f}"
#           )

# customer4_expected = customer4_melons * melon_cost
# if customer4_expected != customer4_paid:
#     print(f"{customer4_name} paid ${customer4_paid:.2f},",
#           f"expected ${customer4_expected:.2f}"
#           )

# customer5_expected = customer5_melons * melon_cost
# if customer5_expected != customer5_paid:
#     print(f"{customer5_name} paid ${customer5_paid:.2f},",
#           f"expected ${customer5_expected:.2f}"
#           )

# customer6_expected = customer6_melons * melon_cost
# if customer6_expected != customer6_paid:
#     print(f"{customer6_name} paid ${customer6_paid:.2f},",
#           f"expected ${customer6_expected:.2f}"
#           )
