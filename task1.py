from collections import Counter

current_inventory = Counter({"Smartphone": 30, 
                             "Tablet": 20, 
                             "Laptop": 15, 
                             "Headphones": 50})

sales_data = ["Smartphone", 
              "Tablet", 
              "Smartphone", 
              "Laptop", 
              "Smartphone", 
              "Headphones", 
              "Tablet",
              "Battery"
              ]

def count_sales(sl):
    return Counter(sl)

def update_inventory(inv, sales):
    inv.subtract(sales)
    return inv

sales = count_sales(sales_data)
print(sales)
print(update_inventory(current_inventory, sales))
