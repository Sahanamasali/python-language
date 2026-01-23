opening_stock = [50, 60, 40, 30]
closing_stock = [45, 70, 35, 30]

for i in range(len(opening_stock)):
    if closing_stock[i] > opening_stock[i]:
        print(f"Product {i+1}: Stock Increased")
    elif closing_stock[i] < opening_stock[i]:
        print(f"Product {i+1}: Stock Reduced")
    else:
        print(f"Product {i+1}: No Change")
