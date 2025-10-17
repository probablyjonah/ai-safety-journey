# this program says hello and asks for name

print("Hello there")
print("What is your name?")  # ask for name
my_name = input(">")
print("It is nice to meet you, " + my_name)
print("The length of your name is:")
print(len(my_name))
print("What is your age?")  # ask for age
my_age = input(">")
print("You will be " + str(int(my_age) + 1) + " in a year.")
