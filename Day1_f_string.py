# # name = input("enter your name:")
# # age = 20

# # print("hello my name is" + str(name))
# # print("hello my name is" + name)

# # print("hello," + name + "Nice to meet you." + "Your age is" +str(age))


# # # aoutomatic type convers
# # print(f"hello, {name}. Nice to meet you. your age is {age}")

# #       # {} interplation?


# radius = input("plaese thell me radius of the circle?")
# pie = 3.14
# area_of_circle=pie*float(radius)**2
# print(f"the area of the circle is {area_of_circle}")

# Task 2: With f-string
# Fahrenheit to Celcius
# Please provide your Fahrenheit: 98.6
# The 98.6°F is 37°C
# °C = (°F - 32) × 5/9

F = input("please tell me your Fahrenhait?")
C = (float(F) - 32)*(5/9)
C2 = round(C ,2)
print(f"The 100°F is {C2}°C.")