categories = ["Food", "Transport", "Rent","Entertainment"]
expenses = [500, 150, 1000, 200]
print(f" The most expensive category was: {categories[expenses.index(max(expenses))]}, with {max(expenses)} spent")