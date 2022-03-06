# -*- coding: UTF-8 -*-
"""PyRamen Homework Starter."""

# @TODO: Import libraries
import csv
from pathlib import Path

# @TODO: Set file paths for menu_data.csv and sales_data.csv
menu_filepath = Path('Resources/menu_data.csv')
sales_filepath = Path('Resources/sales_data.csv')

# @TODO: Initialize list objects to hold our menu and sales data
menu = []
sales = []
report = {}
row_count = 0

# @TODO: Read in the menu data into the menu list
with open(menu_filepath, 'r') as csvfile:
    # print(csvfile)
    
    menu_reader = csv.reader(csvfile, delimiter = ',')
    menu_header = next(menu_reader)
    
    # print(f"{header} <- this is the header" )
    
    for row in menu_reader:
        menu.append(row)

with open(sales_filepath, 'r') as csvfile:
    # print(csvfile)
    
    sales_reader = csv.reader(csvfile, delimiter = ',')
    sales_header = next(sales_reader)
    
    
    for row in sales_reader:
        sales.append(row)

for sales_row in sales:
    
    sales_item = sales_row[4] 
    quantity = sales_row[3]

    if sales_item not in report:
        report[sales_item] = {"01-count": 0, "02-revenue": 0, "03-cogs": 0, "04-profit": 0}
    else:
        continue

# extra quantites from sales to report
for sales_row in sales:
    
    sales_item = sales_row[4]
    quantity = sales_row[3]
    
    if sales_item in report:
        report[sales_item]["01-count"] += int(quantity)

# extra price and cost from menu and calculate revenue and cogs
for sales_row in sales:
    
    sales_item = sales_row[4]
    quantity = sales_row[3]
    
    for menu_row in menu:
        menu_item = menu_row[0]
        menu_price = menu_row[3]
        menu_cost = menu_row[4]
        
        if sales_item == menu_item:
            report[menu_item]["02-revenue"] += (int(menu_price) * int(quantity))
            report[menu_item]["03-cogs"] += (int(menu_cost) * int(quantity))
        elif sales_item != menu_item:
            continue

# calculate profit using revenue and cogs
for item, valuedict in report.items():
     
    for key in valuedict:
        
        cogs = report[item]["03-cogs"]
        revenue = report[item]["02-revenue"]
        
        if key == "04-profit":
            report[item][key] = revenue - cogs
        else:
            continue 

# output file with metrics
output_path = Path("PyRamen.txt")

with open(output_path, 'w') as file:
    file.write("This is the financial report for PyRamen.\n")
    for key in report:
        file.write(f"{key} {report[key]} \n")








# @TODO: Read in the sales data into the sales list










# @TODO: Initialize dict object to hold our key-value pairs of items and metrics
report = {}

# Initialize a row counter variable
row_count = 0

# @TODO: Loop over every row in the sales list object




    # Line_Item_ID,Date,Credit_Card_Number,Quantity,Menu_Item
    # @TODO: Initialize sales data variables


    # @TODO:
    # If the item value not in the report, add it as a new entry with initialized metrics
    # Naming convention allows the keys to be ordered in logical fashion, count, revenue, cost, profit








    # @TODO: For every row in our sales data, loop over the menu records to determine a match


        # Item,Category,Description,Price,Cost
        # @TODO: Initialize menu data variables




        # @TODO: Calculate profit of each item in the menu data


        # @TODO: If the item value in our sales data is equal to the any of the items in the menu, then begin tracking metrics for that item


            # @TODO: Print out matching menu data






            # @TODO: Cumulatively add up the metrics for each item key





        # @TODO: Else, the sales item does not equal any fo the item in the menu data, therefore no match



    # @TODO: Increment the row counter by 1


# @TODO: Print total number of records in sales data




# @TODO: Write out report to a text file (won't appear on the command line output)
