# To find the total billing amount of the items purchased
def add_prices(basket):
	total = 0
	for items in basket:
		total += basket[items]
	return round(total, 2)


groceries = {"bananas": 1.56, "apples": 2.50, "oranges": 0.99, "bread": 4.59,
	"coffee": 6.99, "milk": 3.39, "eggs": 2.98, "cheese": 5.44}

print('Total Amount ', add_prices(groceries))

