# # Read from the User
# # fav_flavour = "vanilla"  # Satoshi

# # Shop
# stock1 = "chocolate mint"
# stock2 = "vanilla"
# stock3 = "coffee"
# stock4 = "green tea"

# # Expected Output
# # Yes, we have vanilla in stock

# # Sorry, we ran out strawberry

# users_fav = input("Which flavpor do you like? : ")

# if  users_fav == stock1 :
#     print(f"Yes, we have {users_fav} in stock")

# elif  users_fav == stock2 : 
#     print(f"Yes, we have {users_fav} in stock")

# elif users_fav == stock3 : 
#     print(f"Yes, we have {users_fav} in stock")

# elif users_fav == stock4 : 
#     print(f"Yes, we have {users_fav} in stock")

# else:
#     print(f"Sorry, we ran out {users_fav}")

#task 1.2
# Shop
stock1 = "chocolate mint"
stock2 = "vanilla"
stock3 = "coffee"
stock4 = "green tea"

# Expected Output
# Yes, we have vanilla in stock

# Sorry, we ran out strawberry

users_fav = input("Which flavpor do you like? : ").lower()

if  users_fav == stock1 or users_fav == stock2 or users_fav == stock3 or users_fav == stock4 :
    print(f"Yes, we have {users_fav} in stock")

else:
    print(f"Sorry, we ran out {users_fav}")

