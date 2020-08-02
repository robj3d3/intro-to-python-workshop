## STEP 1 ##

# print(True and False) # False - it's true if both are true, and false otherwise

# print(True or False) # True - it's true if either of them is true

# print(not True) # False - the opposite of what 'not' is being applied to

# print(not False) # True

# print(True == True) # True - it's true if the first is equivalent to the second

# print(True == False) # False

# print('a' == 'a') # True

## REMEMBER: = is for assignment - assigning new variables. == is for comparison! checking equivalence of 2 values

## STEP 2 ##

hour = int(input("Enter the hour: ")) # converts string input to int

if hour <= 12:
    print("Good morning!")
if (hour >= 12):
    print("Good afternoon!")


## STEP 3 ##

# hour = int(input("Enter the hour: "))

# if hour <= 12:
#     print("Good morning!")
# elif (hour > 12 and hour <= 18):
#     print("Good afternoon!")
# elif (hour > 18):
#     print("Good evening!")


## STEP 4 ##

# hour = int(input("Enter the hour: "))

# if (hour >= 0 and hour <= 12):
#     print("Good morning!")
# elif (hour > 12 and hour <= 18):
#     print("Good afternoon!")
# elif (hour > 18 and hour <= 23):
#     print("Good evening!")
# else:
#     print("Please enter an integer in range 0-23!")

## CHALLENGE ##

# print('''
# Choose any of the three following ice cream flavours...
# 1. Chocolate
# 2. Strawberry
# 3. Vanilla

# If you enter none of the above, you will be given mint.
# ''')

# choice = int(input("Pick your choice (enter number 1-3) > "))

# if (choice == 1):
#     flavour = "chocolate"
# elif (choice == 2):
#     flavour = "strawberry"
# elif (choice == 3):
#     flavour = "vanilla"
# else:
#     flavour = "mint"

# print("You chose {} flavoured ice cream.").format(flavour)

## EXTENSION ##

# print('''
# Choose any two of the three following ice cream flavours...
# 1. Chocolate
# 2. Strawberry
# 3. Vanilla

# If you enter only one or none, you will be given mint.
# ''')

# options = ["chocolate", "strawberry", "vanilla"]

# choices = input("Pick your choice (enter numbers 1-3) > ").split('&')

# giveMint = False

# if len(choices) < 2:
#   giveMint = True

# if giveMint:
#   print("You chose mint flavoured ice cream.")
# else:
#   firstChoice = options[int(choices[0])-1] # must subtract 1 as indexing starts at 0
#   secondChoice = options[int(choices[1])-1]
#   print("You chose {} and {} flavoured ice cream.").format(firstChoice, secondChoice)