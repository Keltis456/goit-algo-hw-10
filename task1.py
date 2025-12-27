from pulp import LpMaximize, LpProblem, LpVariable, lpSum, value

model = LpProblem(name="beverage-production", sense=LpMaximize)

lemonade = LpVariable(name="lemonade", lowBound=0, cat="Integer")
fruit_juice = LpVariable(name="fruit_juice", lowBound=0, cat="Integer")

model += lpSum([lemonade, fruit_juice]), "Total Production"

model += (2 * lemonade + 1 * fruit_juice <= 100), "Water"
model += (1 * lemonade <= 50), "Sugar"
model += (1 * lemonade <= 30), "Lemon Juice"
model += (2 * fruit_juice <= 40), "Fruit Puree"

model.solve()

status_names = [
    'Not Solved', 'Optimal', 'Infeasible', 'Unbounded', 'Not Solved'
]
print("=" * 50)
print("Production Optimization Results")
print("=" * 50)
print(f"Status: {model.status} ({status_names[model.status]})")
print("\nOptimal Production:")
print(f"  Lemonade:    {int(value(lemonade))} units")
print(f"  Fruit Juice: {int(value(fruit_juice))} units")
print(f"\nTotal Products: {int(value(model.objective))} units")

print("\nResource Usage:")
water_used = 2 * value(lemonade) + 1 * value(fruit_juice)
sugar_used = value(lemonade)
lemon_juice_used = value(lemonade)
fruit_puree_used = 2 * value(fruit_juice)

print(f"  Water:        {int(water_used)}/100 units")
print(f"  Sugar:        {int(sugar_used)}/50 units")
print(f"  Lemon Juice:  {int(lemon_juice_used)}/30 units")
print(f"  Fruit Puree:  {int(fruit_puree_used)}/40 units")
