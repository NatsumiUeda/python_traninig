# quote = "I love python"

# print(quote[2])
# print(quote[3]) #o

# #slice operator
# #end is not included

# print(quote[2:]) #love python

# print(quote[2:10:3])
# print(quote[-1])

# #revers string
# print(quote[::-1]) #python evol 

# name = "  Natsumi"
# print(name.upper())
# print(name.lower())
# print(name.strip()) #remove space


# secret_message = "   Programming in Python is not only powerful but also fun!"

# upper_secret_message =secret_message.upper()
# print(upper_secret_message[18:24] + "-" + upper_secret_message[37:45])


# Task 1.2
flipped_message = "!nuf sseldnE dna seitinutroppo lufrewop htiw nohtyP"

# Expected Output
# "python 🗡️ powerful 🌸"

reverse = flipped_message[::-1]
python = reverse.lower()
print(f"{python[0:6]}   🗡️ {reverse[12:20] } 🌸".lower())