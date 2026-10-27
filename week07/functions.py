# Self-Assessment Questions
# 1. The first bug I found was a lack of a colon on a for loop, which I found through the traceback.
# This tells me I am getting more familiar with loops adn how they are structured
# 2. "apply_discounts" is a function that calculates a discount for a price based on an order's tier
# The two inputs for it are of course "price" and "tier"
# Just looking at the function describes what it does, so I believe a colleague could use it without needing the body 
# 3. ChatGPT was used to debug and locate errors in exercise 5. 
# I will admit that AI mainly shortcut my understanding for the most part, but when the error is given to it, it does help my understanding 


# ---Exercise 1---

# Define the function
def calculate_tax(price, rate): 
    return price * rate

# Call the function
tax1 = calculate_tax(100, 0.07)
tax2 = calculate_tax(250, 0.08)

print(f"Tax for $100 at 7%: ${tax1:.2f}")
print(f"Tax for $250 at 8%: ${tax2:.2f}")
print(f"Tax for $350 at 5%: ${calculate_tax(350, 0.05):.2f}")

# ---Exercise 2---
 # Define the function
def apply_discount(price, tier):
    if tier == "gold":
        return price * 0.85
    elif tier == "silver":
        return price * 0.90
    elif tier == "bronze":
        return price * 0.95
    else:
        return price

# Calling the function with different tiers
original_price = 200

for tier in ["gold", "silver", "bronze", "none"]:
    print(f"{tier}: ${apply_discount(original_price, tier):.2f}")


# ---Exercise 3---
def final_price(price, tax_rate, discount_tier):
    discounted_price = apply_discount(price, discount_tier)
    tax = calculate_tax(discounted_price, tax_rate)
    return discounted_price + tax

# Calling the final_price function
print(f"final_price(200, 0.07, 'gold') = ${final_price(200, 0.07, 'gold'):.2f}")

#---Exercise 4---

orders = [(200, 'gold'), (150, 'silver'), (80, 'bronze'), (500, 'none')]
rate = 0.07 

for price, tier in orders:
    total = final_price(price, rate, tier)
    print(f"Price: ${price} | Tier: {tier} | Total: ${total}")

#---Exercise 5---
sales = [120, 80, 250, 175, 90]

total = 0
for sale in sales:
    total = sale
print(f"Total: ${total}")

count = 0
for sale in sales:  # The for loop was missing a colon at the end
    count += 1
print(f"Count: {count}")

i = 0
while i in range(len(sales)): # The while statement needed to specify that "i" needed to be in range
    print(sales[i])
    i += 1


#---Exercise 6---
x = 100  # Global x

def double_it():
    x = 999 # Local x
    return x* 2

print(x) # Taking from the global x
print(double_it()) # Taking from the local x
print(x) # Taking from global x