import json

max_purchase_quantity = 0
max_purchase_user = []
max_purchase_value = 0
max_purchase_customer = []
total_cost_sum = 0
total_quantity_sum = 0
products_sales = {}

with open("data.txt", "r") as file:
    for line in file:
        user_name, product_name, amount, price = line.strip().split(',')
        amount = int(amount)
        price = float(price)

        total_cost = amount * price

        if amount > max_purchase_quantity:
            max_purchase_quantity = amount
            max_purchase_user = [user_name]
        elif amount == max_purchase_quantity:
            max_purchase_user.append(user_name)

        if total_cost > max_purchase_value:
            max_purchase_value = total_cost
            max_purchase_customer = [user_name]
        elif total_cost == max_purchase_value:
            max_purchase_customer.append(user_name)

        total_cost_sum += total_cost
        total_quantity_sum += amount

        if product_name in products_sales:
            products_sales[product_name] += amount
        else:
            products_sales[product_name] = amount

mean_purchase_cost = total_cost_sum / len(products_sales)
mean_purchase_quantity = total_quantity_sum / len(products_sales)

stats_data = {
    "user_with_max_purchase_quantity": max_purchase_user,
    "customer_with_max_purchase_value": max_purchase_customer,
    "mean_cost": mean_purchase_cost,
    "mean_quantity": mean_purchase_quantity
}

with open("stats.json", 'w') as stats_file:
    json.dump(stats_data, stats_file, indent=4)
