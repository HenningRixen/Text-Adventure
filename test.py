# start of the Game
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
        print("    Which one will you choose? (left/right/inventory)")
        print("    You can also always quit the game when you write `quit` to the console. This wont be a choice shown but you can always do it")

        choice = input().lower()
        
    
        if choice == "left":
             left_door()
        
        elif choice == "right":
             right_door()
        
        elif choice == "quit":
             print("")
             print("Quitting")
             print("")
             return
        
        elif choice == "inventory":
             show_inventory()
             start_game()
        
        else:
            print("Invalid choice. Please enter left or right and quit")   

# Inventory 
inventory = {}

def show_inventory():
    print("")
    print("-------------------------------------------------------")
    print("")
    print("Inventory:")
    print("")
    
    if inventory == {}:
           print("")
           print("Youre inventory is empty emtpy")
           print("")


    else:
        for item, count in inventory.items():    
            print(f"{item}: {count}")
            print("")
            print("you return to your room now")
            print("")


#if you return to the start from other room it should take you here:
def returend_to_start():
        print("")
        print("-------------------------------------------------------")
        print("")
        print("youre at the Start")
        print("what will you do? (left/right/inventory)")
        
        choice = input().lower()
        
        if choice == "left":
             left_door()
        
        elif choice == "right":
             right_door()
        
        elif choice == "inventory":
             show_inventory()
             returend_to_start()
        
        elif choice == "quit":
             print("")
             print("Quitting, going to start all over")
             print("")
             return
        
        else:
             print("")
             print("-------------------------------------------------------")
             print("")
             print("Invalid choice. Please enter left or right or inventory")            
            

# this is the first choice to go left or right:

# left door you can pick up a key and go back
def left_door():
        print("")
        print("-------------------------------------------------------")
        print("")
        print("you open the left door")
        print("another empty room this time without doors")
        print("but wait there is something on the floor something ")
        print("what will you do? (back/pick_up/inventory)")
        
        choice = input().lower()
        

        if choice == "pick_up":
                    if "key" in inventory:
                         print("")
                         print("-------------------------------------------------------")
                         print("nice try but you cant pick it up twice")
                         print("-------------------------------------------------------")
                         left_door()
                    else:
                         inventory["key"] = 1
                         print("")
                         print("-------------------------------------------------------")
                         print("")
                         print("you pickled up a Key, your Invntory holds 1 Key now")
                         print("what will that be used for?")
                         print("what will you do next? (back/inventory)")
                         
                         choice = input().lower()

                         if choice == "back":
                              returend_to_start()
                         
                         elif choice == "quit":
                              print("")
                              print("Quitting, going to start all over")
                              print("")
                              return
                         
                         elif choice == "inventory":
                              show_inventory()
                              print("")
                              print("-------------------------------------------------------")
                              print("")
                              print("Theres nothing left in this room you return to the start")
                              returend_to_start()
                         
                         else:
                              print("Invalid choice. Please enter back or inventory")
                              left_door()
                              
        
        elif choice == "back":
             returend_to_start()
        
        elif choice == "inventory":
             show_inventory()
             left_door()
        
        elif choice == "quit":
              print("")
              print("Quitting, going to start all over")
              print("")
              return
        
        else:
             print("Invalid choice. Please enter back or pick_up")
             left_door()

# right you can go left or straight or pick_rubberchicken  
def right_door():
        
        print("")
        print("-------------------------------------------------------")
        print("")
        print("you open the right door")
        print("this looks like some kind of wine cellar, it is well lit and there are many barrels")
        print("and theres a magical rubber chicken running around")
        print("you see two doors which one will you choose (left/straight/back/pick_rubberchicken/inventory/")
        
        choice = input().lower()

        if choice == "left":
            left_door_2()
        
        if choice == "pick_rubberchicken":
                    if "rubberchicken" in inventory:
                         print("")
                         print("-------------------------------------------------------")
                         print("nice try but you cant pick it up twice")
                         print("-------------------------------------------------------")
                         left_door()
                    else:
                         inventory["rubberchicken"] = 1
                         print("")
                         print("-------------------------------------------------------")
                         print("")
                         print("you pickled up the rubberchicken, your Invntory holds 1 Chicken now")
                         print("what will that be used for?")
                         print("Next what do you want to do? (back/straight/left/inventory)")
                         
                         choice = input().lower()

                         if choice == "back":
                            returend_to_start()
                         
                         elif choice == "quit":
                              print("")
                              print("Quitting, going to start all over")
                              print("")
                              return
                         
                         elif choice == "inventory":
                              show_inventory()
                              right_door()
                         
                         elif choice == "straight": 
                              straight()

                         elif choice == "left":
                              left_door_2()  
                         
                         else:
                              print("Invalid choice. Please enter back or inventory")
                              right_door()
                         
                        
        elif choice == "straight":
            straight()
        
        elif choice == "back":
             returend_to_start()

        elif choice == "inventory":
             show_inventory()
             right_door()

        elif choice == "quit":
            print("Quitting, going to start all over")
            return
        
        else:
            print("Invalid choice. Please enter left or straight")
            right_door()

# second level if you go right first
def straight():
            
        print("")
        print("-------------------------------------------------------")
        print("")
        print("you open the right door")
        print("this looks like some kind of wine cellar, it is well lit and there are many barrels")
        print("and theres a magical rubber chicken running around")
        print("you see two doors which one will you choose (left/straight/back/pick_rubberchicken/inventory/")
        
        choice = input().lower()

        if choice == "left":
            left_door_2()
        
        if choice == "pick_rubberchicken":
                    if "rubberchicken" in inventory:
                         print("")
                         print("-------------------------------------------------------")
                         print("nice try but you cant pick it up twice")
                         print("-------------------------------------------------------")
                         left_door()
                    else:
                         inventory["rubberchicken"] = 1
                         print("")
                         print("-------------------------------------------------------")
                         print("")
                         print("you pickled up the rubberchicken, your Invntory holds 1 Chicken now")
                         print("what will that be used for?")
                         print("Next what do you want to do? (back/straight/left/inventory)")
                         
                         choice = input().lower()

                         if choice == "back":
                            returend_to_start()
                         
                         elif choice == "quit":
                              print("")
                              print("Quitting, going to start all over")
                              print("")
                              return
                         
                         elif choice == "inventory":
                              show_inventory()
                              right_door()
                         
                         elif choice == "straight": 
                              straight()

                         elif choice == "left":
                              left_door_2()  
                         
                         else:
                              print("Invalid choice. Please enter back or inventory")
                              right_door()
                         
                        
        elif choice == "straight":
            straight()
        
        elif choice == "back":
             returend_to_start()

        elif choice == "inventory":
             show_inventory()
             right_door()

        elif choice == "quit":
            print("Quitting, going to start all over")
            return
        
        else:
            print("Invalid choice. Please enter left or straight")
            right_door()  

def left_door_2():
            
        print("")
        print("-------------------------------------------------------")
        print("")
        print("you open the left door")
        if "chicken" in inventory
        else:
               print("")
               print("There is a huge ass Dragon in the middle of the room guarding a chest")
               print("for now he didnt see you but you slowly close the door and go back to the wine cellar")
               print("maybe you can distract him somehow")
               right_door()
        
        choice = input().lower()

        if choice == "left":
            left_door_2()
        
        if choice == "pick_rubberchicken":
                    if "rubberchicken" in inventory:
                         print("")
                         print("-------------------------------------------------------")
                         print("nice try but you cant pick it up twice")
                         print("-------------------------------------------------------")
                         left_door()
                    else:
                         inventory["rubberchicken"] = 1
                         print("")
                         print("-------------------------------------------------------")
                         print("")
                         print("you pickled up the rubberchicken, your Invntory holds 1 Chicken now")
                         print("what will that be used for?")
                         print("Next what do you want to do? (back/straight/left/inventory)")
                         
                         choice = input().lower()

                         if choice == "back":
                            returend_to_start()
                         
                         elif choice == "quit":
                              print("")
                              print("Quitting, going to start all over")
                              print("")
                              return
                         
                         elif choice == "inventory":
                              show_inventory()
                              right_door()
                         
                         elif choice == "straight": 
                              straight()

                         elif choice == "left":
                              left_door_2()  
                         
                         else:
                              print("Invalid choice. Please enter back or inventory")
                              right_door()
                         
                        
        elif choice == "straight":
            straight()
        
        elif choice == "back":
             returend_to_start()

        elif choice == "inventory":
             show_inventory()
             right_door()

        elif choice == "quit":
            print("Quitting, going to start all over")
            return
        
        else:
            print("Invalid choice. Please enter left or straight")
            right_door()           
            












start_game()