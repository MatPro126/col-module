---
runme:
  id: 01HSK5TWDSNJ8ZA49RFE64YXE5
  version: v3
---

### Exercise: Product Inventory Management
You are in charge of managing the inventory of a small electronics store. Your task is to track the number of each type of gadget sold over the course of a day and then update the inventory accordingly.
#### Part 1: Counting Gadgets Sold
You receive a list of gadgets sold during the day, represented by their names. Gadgets can include items like "Smartphone", "Tablet", "Laptop", "Headphones", etc.
Example of sales data for one day:
python
sales_data = ["Smartphone", "Tablet", "Smartphone", "Laptop", "Smartphone", "Headphones", "Tablet"]
*Task*: Write a Python function count_sales that takes a list of strings (sales_data) as input and returns a Counter object with the count of each gadget sold.
#### Part 2: Updating Inventory
At the end of the day, you need to update the store's inventory based on the sales data. The current inventory is also provided as a Counter object, which includes all types of gadgets in the store and their respective quantities.
Example of current inventory:
python
current_inventory = Counter({"Smartphone": 30, "Tablet": 20, "Laptop": 15, "Headphones": 50})
*Task*: Write a Python function update_inventory that takes two Counter objects (current_inventory and sales_counts) as input and updates the current_inventory based on the sales_counts. The function should subtract the count of each gadget sold from the current inventory and return the updated inventory as a Counter object.
#### Requirements:
- Use collections.Counter to solve this exercise.
- The update_inventory function should handle cases where a gadget sold is not in the current inventory (it should assume a starting count of 0 for such items).
- If the sales data includes gadgets not previously in the inventory, they should be added to the updated inventory with their counts set to negative numbers, indicating that they need to be restocked.