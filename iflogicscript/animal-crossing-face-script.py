# List of possible faces player will receive after answering questions.
face_options = ["Default Villager", "Brown eyes with eyelashes looking straight", "Tired eyes", "Crazy looking, blue eyes", "Crazy looking"]

# List to keep track of player's choices.
user_choices = []

# Rover asks if he can sit wit the player.
sit = int(input("???: Mind if I sit here?\n1. Please!\n2. No way!"))

while sit < 1 or sit > 2:
    sit = int(input("Please enter a valid selection.\n1. Please!\n2. No way!"))

user_choices.append(sit)

if sit == 1:
    print("Rover: Thanks! It sure is nice meeting friendly folk on the train... you aren't psycho right? Just kidding!")
else:
    print("Rover: Rude... Well I'm going to sit here anyway.")

# Rover asks where player is going.
town = input("Rover: Anyway, I'm Rover. Nice to meet you. Where are you headed?")

# Rover asks why player is going to that town.
reason = int(input("Rover: So, what are you going to " + town + " for?\n1. I'm moving!\n2. What's it to ya?"))

while reason < 1 or reason > 2:
    reason = int(input("Please enter a valid selection.\n1. I'm moving!\n2. What's it to ya?"))

user_choices.append(reason)

# Rover asks where player's new place is.
location = int(input("Rover: Where's your new place?\n1. Don't know yet.\n2. Leave me alone! "))

while location < 1 or reason > 2:
    reason = int(input("Please enter a valid selection.\n1. Don't know yet.\n2. Leave me alone!"))

user_choices.append(location)

# Rover asks if player has any money.
money = int(input("Rover: You have money, right?\n1. Just a little...\n2. Oh, yeah!"))

while money < 1 or money > 2:
    money = int(input("Please enter a valid selection.\n1. Just a little...\n2. Oh, yeah!"))

user_choices.append(money)

# Based on player's choices, player will receive a different face model.
if sum(user_choices) == 4:
    print(f"You have the {face_options[0]} character model.")
elif sum(user_choices) == 5:
    print(f"You have the {face_options[1]} character model.")
elif sum(user_choices) == 6:
    print(f"You have the {face_options[2]} character model.")
elif sum(user_choices) == 7:
    print(f"You have the {face_options[3]} character model.")
elif sum(user_choices) == 8:
    print(f"You have the {face_options[4]} character model.")
