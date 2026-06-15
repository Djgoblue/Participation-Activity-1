#Create list of sandwiches and make an empty list called finished_sandwiches.
sandwich_orders = ["Tuna", "Meatball sub", "Cheesesteak", "Egg salad", "PB&J"]
finished_sandwiches = []

#Loop though the list of sandwich orders and print a message for each order.
while sandwich_orders:
    current_sandwich = sandwich_orders.pop(0)
    print(f"I made your {current_sandwich} sandwich.")
    finished_sandwiches.append(current_sandwich)

print("\nI have made the following sandwiches:")
for sandwich in finished_sandwiches:
    print(f"{sandwich} sandwich")