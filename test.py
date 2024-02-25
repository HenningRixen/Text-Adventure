def start_game():
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
            print("Invalid choice. Please enter left or right and quit")
    

def returend_to_start():
        
        print("youre at the Start")
        print("what will you do? (left/right)")
        
        choice = input().lower()
        
        if choice == "left":
             left_door()
        elif choice == "right":
             right_door()
        
        elif choice == "quit":
             print("Quitting, going to start all over")
             return
        
        else:
             print("Invalid choice. Please enter left or right")            
            



def left_door():

        print("you open the left door")
        print("another empty room this time without doors")
        print("but wait there is something on the floor something ")
        print("what will you do? (back/pick_up)")
        
        choice = input().lower()
        
        Inventory = {
            "Key": 0
        }

        if choice == "pick_up":
             Inventory["Key"] = 1
             print("you pickled up a Key, your Invntory holds 1 Key now")
             print("what will that be used for?")
             print("what will you do next? (back/inventory)")
             
             choice = input().lower()

             if choice == "back":
                 returend_to_start()
             
             if choice == "inventory":
                for item,count in Inventory:
                    print(f"Item: {item}, Count: {count}")
                    print("theres nothing more to do in this room, you go back to the start")
                returend_to_start()
             else:
                  print("Invalid choice. Please enter left or right")
                  left_door()
        
        elif choice == "back":
             returend_to_start()
        
        elif choice == "quit":
             print("Quitting, going to start all over")
             return
        
        else:
             print("Invalid choice. Please enter left or right")
             left_door()

        
def right_door():

        print("you open the right door")
        print("this looks like some kind of wine cellar, it is well lit and there are many barrels")
        print("you see two doors which one will you choose (left/straight")
        
        if choice == "left":
            left_door_2()
        
        elif choice == "straight":
            straight()
        
        elif choice == "quit":
            print("Quitting, going to start all over")
            start_game()
        
        else:
            print("Invalid choice. Please enter left or straight")

def straight():
    print("yup")   

def left_door_2():
    print("hey")            
            












start_game()