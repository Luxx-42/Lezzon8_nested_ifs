# Task 3 default path
place = input("Choose a place: forest or cave? ")

if place == "forest":
    action = input("climb a tree or cross a river? ")
    if action == "climb a tree":
        print("You found a bird's nest!")
    elif action == "cross a river":
        print("You found a boat!")
    else:
        pass # added pass statement
        print("Invalid choice. Try again.")
elif place == "cave":
    need_a_light = input("Do you want to light a torch or proceed in the dark? ")
    if need_a_light == "light a torch":
        print("you can now get to the treasure faster!")
    elif need_a_light == "proceed in the dark":
        print("It's risky business, but you still have a slim chance at finding a hidden treasure!")
    else:
        pass # added pass statement
        print("Invalid choice. Try again.")