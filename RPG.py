def showInstructions():
    # Print a main menu and the commands
    print("""
RPG Game
========

Get to the Garden with a key and a potion.
Avoid the monsters!

You are getting tired; each time you move you lose one health point.

Commands:
    go [north | south | east | west]
    get [item]
""")

def showStatus():
    # Print the player's current status
    print("---------------------------")
    print(name + " is in the " + currentRoom)
    print("Health : " + str(health))
    # Print the current inventory
    print("Inventory : " + str(inventory))
    # Print an item if there is one
    if "item" in rooms[currentRoom]:
        print("You see a " + rooms[currentRoom]["item"])
    print("---------------------------")

# Set up a new game
name = None
health = 5
currentRoom = "Hall"
inventory = []

# A dictionary linking a room to other room positions
rooms = {
          "Hall" : { "south" : "Kitchen",
                     "east"  : "Dining Room",
                     "item"  : "key"
                   },

          "Kitchen" : { "north" : "Hall",
                        "item"  : "monster"
                      },

          "Dining Room" : { "west"  : "Hall",
                            "south" : "Garden",
                            "item"  : "potion"
                          },

          "Garden" : { "north" : "Dining Room" }
        }

# Ask the player their name
if name is None:
    name = input("What is your name, Wanderer? ")
    showInstructions()

# Loop forever
while True:

    showStatus()

    # Get the player's next "move"
    # .split() breaks it up into an list array
    # e.g. typing "go east" would give the list:
    # ["go","east"]
    move = ""
    while move == "":
        move = input(">")

    move = move.lower().split()

    # If they type "go" first
    if move[0] == "go":
        health = health - 1
        # Check that they are allowed wherever they want to go
        if move[1] in rooms[currentRoom]:
            # Set the current room to the new room
            currentRoom = rooms[currentRoom][move[1]]
        # or, if there is no door (link) to the new room
        else:
            print("You can't go that way!")

    # If they type "get" first
    if move[0] == "get" :
        # If the room contains an item, and the item is the one they want to get
        if "item" in rooms[currentRoom] and move[1] in rooms[currentRoom]["item"]:
            # Add the item to their inventory
            inventory += [move[1]]
            # Display a helpful message
            print(move[1] + " got!")
            # Delete the item from the room
            del rooms[currentRoom]["item"]
        # Otherwise, if the item isn't there to get
        else:
            # Tell them they can't get it
            print("Can't get " + move[1] + "!")

    # Player loses if they enter a room with a monster
    if "item" in rooms[currentRoom] and "monster" in rooms[currentRoom]["item"]:
        print("A monster has got you ... GAME OVER!")
        break

    if health == 0:
        print("You collapse from exhaustion ... GAME OVER!")
        break

    # Player wins if they get to the garden with a key and a potion
    if currentRoom == "Garden" and "key" in inventory and "potion" in inventory:
        print("You escaped the house ... YOU WIN!")
        break

