
# if ...else

#indentation(tab)

# x = 10
# y = 4


# if x > y:
#     print(f"{x} is greater")
# else:
#     print(f"{y} is greater")


# Task
# Get two person name
# Case 1:
# Yuma, Yoshi
# 173cm, 163cm
# Expected
# Yuma is taller than Yoshi by 10cm

# Case 2:
# Yuma, Yoshi
# 173cm, 185cm
# Expected
# Yoshi is taller than Yuma by 12cm


yuma_name = input("please tell me your name?")
yoshi_name = input("please tell me your name?")
yuma_height = input("please tell me your height?")
yoshi_height = input("please tell me your height?")
int_yuma_height = int(yuma_height)
int_yoshi_height = int(yoshi_height)
height_difference1 = int_yuma_height - int_yoshi_height
height_difference2 = int_yoshi_height - int_yuma_height


if  int_yuma_height> int_yoshi_height:
    print(f"yuma is taller than yoshi by {height_difference1} cm")

elif height1 == height2:
    (f"yuma and yoshi are of same height")

else:
    print(f"yoshi is taller than yuma by {height_difference2} cm")

#elif is many




