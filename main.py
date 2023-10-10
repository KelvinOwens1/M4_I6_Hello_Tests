def say_hello():
  return "Hello World!"

def hey_you(charName):
  return f"Hey, {charName}!"

def age_in_2050(charYear):
  age = 2050 - charYear
  return f"You are {age} if born in year 2050."

def can_i_take_your_order(charBurgers, charFries, charDrinks):
  totalPriceBurgers = burgersPrice * float(burgersTotal)
  totalPriceFries = friesPrice * float(friesTotal)
  totalPriceDrinks = drinksPrice * float(drinksTotal)
  total = totalPriceBurgers + totalPriceFries + totalPriceDrinks
  print("\n")
  print("Here is your receipt:")
  print(
    f"- Good Burgers ${burgersPrice} x {charBurgers} = ${totalPriceBurgers}")
  print(f"- French Fries ${friesPrice} x {charFries} = ${totalPriceFries}")
  print(f"- Drinks       ${drinksPrice} x {charDrinks} = ${totalPriceDrinks}")
  print(f"TOTAL = ${total}")
  

print(say_hello())

name1 = input("What is your name? ")
print(hey_you(name1))

year1 = int(input("What year were you born? "))
print(age_in_2050(year1))

# burgersPrice = 4.5
# friesPrice = 1.5
# drinksPrice = 1.0
# burgersTotal = input(f"Good Burgers (${burgersPrice}): ")
# friesTotal = input(f"\nFrench Fries (${friesPrice}): ")
# drinksTotal = int(input("\nDrinks       ($1.0): "))

# can_i_take_your_order(burgersTotal, friesTotal, drinksTotal)
