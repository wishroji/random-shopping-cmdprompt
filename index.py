import time
import random
stock = ["apple", "WHAT?", "banan", "pineapple"]
# append if you want

for i in stock:
    print(f"-=| {i} |=-")
print("")
cents = float(round(random.uniform(.15, .99),2))
fanum = round(random.uniform(1.15, 3.99), 2)
amount = int(len(stock))
x = str(input("Chosen Item?: "))

def checkout():
    print("")
    print("===========================")
    print(f"{x} cost: ${float_assigned_price}")
    print(f"quantity: x{multiplier}")
    print(f"anti-fanum tax: +${fanum}")
    print("===========================")
    print(f"subtotal: ${x_price}")
    print(f"total: ${float(x_price)+fanum}")
    print("===========================")
    print("")


#------------------

def decider():
    global float_assigned_price, multiplier, x_price
    assigned_price = int(y_prices[random.randrange(0,amount+1)])
    float_assigned_price = round(float(assigned_price) + cents, 2)
    multiplier = int(input(f"how much {x} do you want? "))
    print("")
    x_price = assigned_price*multiplier+cents
    print(f"{multiplier} counts of {x} will be ${x_price}")
    print(f"(one count of {x} is ${float_assigned_price})")
    print("")
    checkout_prompt = input("proceed to checkout? (y/n) ")
    if checkout_prompt == "y":
        checkout()
    elif checkout_prompt == "n":
        print("outa my store son")
    else:
        print("huh? didnt get that one.")
    
#------------------

def price():
    global y_prices
    y_prices = []
    for i in range(amount+1):   
        y_prices.append(random.uniform(1.15, 7.99))
    decider()

#--------------------

if stock.count(x) > 0:
    print("")
    print("checking inventory...")
    time.sleep(1.5)
    print("")
    print(f"{x} is in stock!")
    x_stock = True
    price()
else:
    print("")
    print("checking inventory...")
    time.sleep(1.5)
    print("")
    print(f"{x} is not in stock or isnt an item!")
    
