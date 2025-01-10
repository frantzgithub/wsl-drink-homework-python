
last_year = 2024

quantity_coca_selled = 150
quantity_pepsi_selled = 150
price_of_one_coca = 1.50
price_of_one_pepsi = 1.50
store_expenses = 250.0

coca_revenue = quantity_coca_selled * price_of_one_coca
print("coca revenue is: " + str(coca_revenue))
pepsi_revenue = quantity_pepsi_selled * price_of_one_pepsi
print("pepsi revenue is: " + str(pepsi_revenue))

total_revenue = pepsi_revenue + coca_revenue

profit = total_revenue - store_expenses
print("The benefit is: " + str(profit))

store_margin = profit / store_expenses
print("The store margin is: " + str(store_margin))