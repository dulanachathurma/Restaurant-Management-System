menu = {
    "coffee": 3,
    "tea": 2,
    "sandwich": 5,
    "salad": 4,
    "soup": 10,

}

print("""
      Welcome to our restaurant!

    coffee: $3,
    tea: $2,
    sandwich: $5,
    salad: $4,
    soup: $10,
      
        """
      )
total_price = 0

item1 = input("What would you like to order? ")
if item1 in menu:
    total_price += menu[item1]
    print(f"{item1} added to your order. Current total: ${total_price}")

another_item = input("Would you like to order anything else? (yes/no) ")
if another_item.lower() == "yes":
    
    item2 = input("What else would you like to order? ")
    if item2 in menu:
        total_price += menu[item2]
        print(f"{item2} added to your order. Current total: ${total_price}")
        print(f"Your final total is: ${total_price}. Thank you for dining with us!")
    else:
        print("Sorry, we don't have that item.")
else:
    print(f"Your final total is: ${total_price}. Thank you for dining with us!")


