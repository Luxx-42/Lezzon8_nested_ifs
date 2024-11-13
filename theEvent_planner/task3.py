# Task 3 catering choices
attendees = int(input("Enter number of attendees: ")) # added integer

venue = "large hall" if attendees > 100 else "conference room"
print(venue)

which_room = input("What room will you be in based on the number of attendees? ")

if which_room == "large hall": # added additional audio system for large hall
    print("a massive projection screen is needed so that everyone can see.")
elif which_room == "conference room": # added additional project screen for conference
    print("You will a great audio system is needed so that everyone can hear.")

# added a pass statement for an invalid response
else:
    pass
    print('Invalid response. Either "large hall" or "conference room" should be entered.')

# added a user catering input and a shorthand if statement for the input
kater_2_U = input("Would you like vegetarian food for your event? (yes/no): ")

caterer = "Veggie Delight Caterers would be great for your event!" if kater_2_U == "yes" else "Gourmet Meals Caterers would be great for everyone!"
print(caterer)