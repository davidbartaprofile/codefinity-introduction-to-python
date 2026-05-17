#    Determine whether a grocery item should be discounted based on its seasonal status, stock level, and sales performance.
#    Define a boolean variable overstock_risk — it should be True if the item is seasonal and its current_stock exceeds high_stock_threshold.
#    Define a boolean variable discount_eligible — it should be True if the item is not selling_well and not on_sale.
#    Define a boolean variable make_discount — it should be True if either overstock_risk or discount_eligible is True.
#    Output: Print the following line, where the value of make_discount is shown at the end: "Should the item be discounted?" True

seasonal = True
on_sale = False
selling_well = False
current_stock = 150
high_stock_threshold = 100
overstock_risk=seasonal and current_stock >= high_stock_threshold
discount_eligible=not selling_well and not on_sale
make_discount=overstock_risk or discount_eligible
print("Should the item be discounted?", make_discount)
