def start_game():
    while True:
        print("Welcome to my mystical adventure")
        print("--------------------------------")
        print("... You wake up in a strange room it smells like mold and a torch lights up a room ...")
        print("... Slowly you remember who you are ... youre Madam Bumblebum... ")
        print("... and youre were on a Party with the other elves to celebrate that your little strawberry jam store is now the most renown in the whole elve Kingdom...")
        print("... you cant remember how you got in this situation tho, maybe somebody mixed something in your drink ...")
        print("... but that doesnt matter now you have to get out of this dungeon back to the surface...")
        print("... youre famous Strawberryjam doesnt produce itself and soon the school vacation is over you cant let the young elves go to school without their strawberry jam. ")
        print("... You inspect the room further and see two doors one to the left and one to the right ...")
        print("    Which one will you choose? (left/right) or quit")

        choice = input().lower()

    
        if choice == "left":
            left_door()
        elif choice == "right":
            right_door()
        elif choice == "quit":
            print("Quitting")
            return
        else:
            print("Invalid choice. Please enter `left` or `right`")
        
def left_door():
    while True:
        print("you open the left door")
        print("another empty room this time without doors")
        print("but wait there is something on the floor something ")
def right_door():
    while True:

            
            












start_game()