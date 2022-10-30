first_name = input("What is your first name? ")
first_name = first_name.lower().capitalize()

last_name = input("What is you last name? ")
last_name = last_name.lower().capitalize()

print("Hello there", first_name, last_name, "(" + first_name[0].capitalize() + "." + last_name[0].capitalize() + ")")

print("The length of your first name is", len(first_name), "characters")
print("The length of your last name is", len(last_name), "characters")
print("The length of your full name is", len(first_name + last_name), "characters")
