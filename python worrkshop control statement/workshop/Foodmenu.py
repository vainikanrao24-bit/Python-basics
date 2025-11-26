Fmenu={
    "Strawberry mousse": 245,"French fries": 90,"Burger":120,"Hot Chocolate milkshake":200,"Butterscotch milkshake":179,"white sauce pasta":230,"BabyCorn Manchoori":300,"Mojito Mocktail":310, "Watermelon juice":135,"corn Sandwich":145
}
print(" WELCOME TO OUR CAFE")
print("---FOOD MENU---")
for food,price in Fmenu.items():
    print(f"{food}:{price}")
user=input("\n Enter the food from the menu :")
if user in Fmenu:
    print(f"The price is {Fmenu[user]}")
else:
    print("the item is not available")
