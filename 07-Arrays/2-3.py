# Weekly expenses for different categories
# [Food, Transport, Utilities]
monthly_expenses = [
    [200, 50, 100],  # Week 1
    [180, 60, 110],  # Week 2
    [220, 55, 105],  # Week 3
    [210, 65, 95],   # Week 4
]

# Initialize totals
num_categories = len(monthly_expenses[0])
category_totals = [0] * num_categories
week_totals = []
monthly_total = 0

# Calculate weekly, category, and monthly totals using loops
for week in monthly_expenses:
    week_sum = 0
    for i in range(num_categories):
        amount = week[i]
        category_totals[i] += amount
        week_sum += amount
    week_totals.append(week_sum)
    monthly_total += week_sum

food_total, transport_total, utilities_total = category_totals

# Print expenses
print('MONTHLY EXPENSES')
print('----------------')
print('Food:', food_total)
print('Transport:', transport_total)
print('Utilities:', utilities_total)
print('Week 1:', week_totals[0])
print('Week 2:', week_totals[1])
print('Week 3:', week_totals[2])
print('Week 4:', week_totals[3])
print('---------------')
print('TOTAL:', monthly_total)