with open("data.txt", "r") as file:
    for line in file:
        user_name, product_name, amount, price = line.strip().split(',')
        amount = int(amount)
        price = float(price)

        total_cost = amount * price

        purchase_data = f"{user_name}, {product_name}, {amount}, {price:.2f}, {total_cost:.2f}"

        if total_cost < 10:
            with open("small.txt", "a") as small_file:
                small_file.write(purchase_data + '\n')

        else:
            with open("high.txt", "a") as high_file:
                high_file.write(purchase_data + '\n')
