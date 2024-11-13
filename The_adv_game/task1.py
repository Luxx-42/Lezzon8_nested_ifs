# Task 1 code correction
place = input("Choose a place: forest or cave? ")

# changed the assignment operator = to a comparison operator ==
if place == "forest":
    action = input("climb a tree or cross a river?")

    # changed the assignment operator = to a comparison operator ==
    if action == "climb a tree":
        print("You found a bird's nest!")

    # removed the unnessecary conditional 
    else:
        print("You found a boat!")

# changed the assignment operator = to a comparison operator ==
elif place == "cave":
    print("You find a hidden treasure!")