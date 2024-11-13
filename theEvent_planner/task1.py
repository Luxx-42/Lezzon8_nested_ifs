# Task 1 code correction
attendees = int(input("Enter number of attendees: ")) # added integer

venue = "large hall" if attendees > 100 else "conference room"
print(venue)