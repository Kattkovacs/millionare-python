true = ["True", "t", "T", "true", "TRUE"]
false = ["False", "f", "F", "false", "FALSE"]
correct = 0  # The score you reach
print("What's your name dear adventurer?")
name = input("My name is: ")  # Here goes the player's name


print('\n'"Okay then dear", name, "let's get our little quiz started.")
print('\n'"The rules are simple: ", '\n', "1. You can answer only with True, or False.")

print('\n', "So, first of all. Matthias Corvinus was a polish king.")
choice = input("Is it True or False?: ")
if choice in false:
    correct += 1
    print("Great answer, keep it up!")
else:
    correct += 0
    print("That was wrong.. He was hungarian. Better learn more!")

print('\n', "John Fitzerald Kennedy was the 35th president of the USA.")
choice = input("Is it True or False?: ")
if choice in true:
    correct += 1
    print("You are almost at the end, good job!")
else:
    correct += 0
    print("That was wrong, I don't blame you, it's fine...")

print('\n', "Last statement is: The Pulp Fiction movie was presented in 1994 for the very first time.")
choice = input("Is it True or False?: ")
if choice in true:
    correct += 1
    print("How would you know that?? Great work.")
else:
    correct += 0
    print("Ah, you missed that..")

print("So dear", name, "you got", correct, "points of out the 3.")
if correct == 0:
    print("You got literally 0 points of this quiz. Don't you think it's a shame? You get no rewards...")
elif correct == 1:
    print("You reached 1 point, your reward will be a little something.")
elif correct == 2:
    print("You managed to get 2 points out there! Some good rewards are on the way to you.")
elif correct == 3:
    print("You answered all the questions correct! Good job, you will get a very nice reward.")
