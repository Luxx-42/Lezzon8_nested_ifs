# Task 2 setting the scene
place = input("Choose a place: forest or cave? ")

if place == "forest":
    action = input("climb a tree or cross a river?")
    if action == "climb a tree":
        print("You found a bird's nest!")
    else:
        print("You found a boat!")
elif place == "cave":

    # added a optional light input for the user
    need_a_light = input("Do you want to light a torch or proceed in the dark?")
    if need_a_light == "light a torch":
        print("you can now get to the treasure faster!")
    elif need_a_light == "proceed in the dark":
        print("It's risky business, but you still have a slim chance at finding a hidden treasure!")
    print("You found a hidden treasure!")
