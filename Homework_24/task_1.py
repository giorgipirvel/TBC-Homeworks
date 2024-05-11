import json

with open("markets.json", "r") as markets_file:
    markets_data = json.load(markets_file)

with open("recipes.json", "r") as recipes_file:
    recipes_data = json.load(recipes_file)

print("Available dishes:")
for dish in recipes_data:
    print("-", dish)
selected_dish = input("Enter the name of dish you are preparing: ")

if selected_dish not in recipes_data:
    print("Selected dish isn't available")

else:
    ingredients = recipes_data[selected_dish]["ingredients"]
    stores = {ingredient: [] for ingredient in ingredients}
    for store, products in markets_data.items():
        for ingredient in ingredients:
            if ingredient in products:
                stores[ingredient].append(store)
    
    print(f"\ningredinets for {selected_dish}")
    for ingredient, available_markets in stores.items():
        print(f" - {ingredient}:", ", ".join(available_markets) or "Not available in store")

    common_markets = set.intersection(*map(set, stores.values()))
    print("Common markets:", common_markets)
    if all(len(available_markets) > 0 for available_markets in stores.values()):
        print(f"\nAll ingredients of {selected_dish} are available in aboved mentioned markets")
        for store in common_markets:
            print("-", store)
    else:
        print(f"\nYou cannot prepare {selected_dish}")
