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
            

# this level 1 choice to go left or right:
#!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!

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

# level 2 if you go right first:
#!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!

#if you go back to the vine cellar
def back_at_right_door():
        
        print("")
        print("-------------------------------------------------------")
        print("")
        print("youre back in the wine cellar")
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
                              back_at_right_door()
                         
                         elif choice == "straight": 
                              straight()

                         elif choice == "left":
                              left_door_2()  
                         
                         else:
                              print("Invalid choice. Please enter back or inventory")
                              back_at_right_door()
                         
                        
        elif choice == "straight":
            straight()
        
        elif choice == "back":
             returend_to_start()

        elif choice == "inventory":
             show_inventory()
             right_door()

        elif choice == "quit":
            print("")
            print("--------------------------------------------------------------------")
            print("Quitting, going to start all over")
            return
        
        else:
            print("")
            print("--------------------------------------------------------------------")
            print("Invalid choice. Please enter left or straight")
            right_door()

#you go straight ahead to level 3
def straight():
            
        print("")
        print("-------------------------------------------------------")
        print("")
        print("you go straight and enter a new room")
        level_3_choices()

# you encounter a dragon, if you have the rubberduck you can do something otherwise you get kicked out
def left_door_2():
            
        print("")
        print("-------------------------------------------------------")
        print("")
        print("you open the left door")
        if "rubberchicken" in inventory:
           print("")
           print("--------------------------------------------------------------------")
           print("")
           print("There is a huge ass Dragon in the middle of the room guarding a chest")
           print("maybe you can distract him somehow")
           print("Choose (run/throw_chicken/throw_any_item")
           
           choice = input().lower()

           if choice == "run":
              print("")
              print("---------------------------------------------------------")
              print("you run back to the room wehre you came from you coward!!")
              back_at_right_door()
           
           elif choice == "throw_any_item":
                print("")
                print("---------------------------------------------------------")
                print("Cmon that would do anything now would it?")
                left_door_2()
           
           elif choice == "throw_chicken":
                inventory["rubberchicken"] = 0
                print("")
                print("--------------------------------------------------------------------")
                print("")
                print("You throw the rubberchicken to the corner and it makes a loud noise")
                print("The dragon instantly charges to the rubberchicken and cuddles with it")
                print("the chest is now unguarded")
                print("you go to the chest and open it, it contains a magical crystal of some sort")
                print("you store it in your inventory and leave the room")
                inventory["magical_crystal"] = 1
                right_door_after_dragon()
               

           elif choice == "inventory":
                show_inventory()
                left_door_2()

           elif choice == "quit":
                print("")
                print("--------------------------------------------------------------------")
                print("Quitting, going to start all over")
                return
        
           else:
                print("")
                print("--------------------------------------------------------------------")
                print("Invalid choice. Please enter run or throw_chicken or throw_key")
                left_door_2()

        else:
               print("")
               print("--------------------------------------------------------------------")
               print("")
               print("There is a huge ass Dragon in the middle of the room guarding a chest")
               print("for now he didnt see you so you slowly close the door and go back to the wine cellar")
               print("maybe you can distract him somehow")
               back_at_right_door()

# when you picked up the crystal the wine cellar you return to a changed version of it and your choices are limitted
def right_door_after_dragon():
    print("")
    print("--------------------------------------------------------------------")
    print("")
    print("The wine is everywhere")
    print("somebody chopped up the barrels with an axe")
    print("who would do something like that? You got to be careful")
    print("somebody else is or was here too")
    print("he also locked the door back to the starting room")
    print("choose straight/left/inventory")
    
    choice = input().lower()

    if choice == "left":
       print("")
       print("--------------------------------------------------------------------")
       print("")
       print("You return to the dragon room")
       print("He is sleeping next to his rubberchicken right now")
       print("theres nothing more to gain here")
       right_door_after_dragon()
    
    elif choice == "straight":
            straight()

    elif choice == "inventory":
             show_inventory()
             right_door_after_dragon()

    elif choice == "quit":
            print("")
            print("--------------------------------------------------------------------")
            print("Quitting, going to start all over")
            return
        
    else:
        print("")
        print("--------------------------------------------------------------------")
        print("Invalid choice. Please enter left or straight or inventory")
        right_door_after_dragon()

#if you go straight without the dragon
def right_door_if_you_went_straight():
    
    print("")
    print("--------------------------------------------------------------------")
    print("")
    print("The wine is everywhere")
    print("somebody chopped up the barrels with an axe")
    print("who would do something like that? You got to be careful")
    print("somebody else is or was here too")
    print("he also locked the door back to the starting room")
    print("the rubber duck still floats on the wine")
    print("choose straight/left/pick_rubberchicken/inventory")
    
    choice = input().lower()

    if choice == "pick_rubberchicken":
                    if "rubberchicken" in inventory:
                         print("")
                         print("-------------------------------------------------------")
                         print("nice try but you cant pick it up twice")
                         print("-------------------------------------------------------")
                         right_door_if_you_went_straight()
                    else:
                         inventory["rubberchicken"] = 1
                         print("")
                         print("-------------------------------------------------------")
                         print("")
                         print("you pickled up the rubberchicken, your Invntory holds 1 Chicken now")
                         print("what will that be used for?")
                         right_door_if_you_went_straight()

    if choice == "left":
       if "rubberchicken" in inventory:
           print("")
           print("--------------------------------------------------------------------")
           print("")
           print("There is a huge ass Dragon in the middle of the room guarding a chest")
           print("you take the rubberchicken throw it in the corner and open the chest")
           inventory["rubberchicken"] = 0
           print("it contains a magical crystal of some sort")
           print("you store it in your inventory and leave the room")
           inventory["magical_crystal"] = 1 
           right_door_after_dragon()
       else:
           print("")
           print("--------------------------------------------------------------------")
           print("")
           print("Severe dragon in this room you have to distract him somehow")
           print("you go back to where you came from")
           right_door_if_you_went_straight()

    
    elif choice == "straight":
            straight()

    elif choice == "inventory":
             show_inventory()
             right_door_if_you_went_straight()

    elif choice == "quit":
            print("")
            print("--------------------------------------------------------------------")
            print("Quitting, going to start all over")
            return
        
    else:
        print("")
        print("--------------------------------------------------------------------")
        print("Invalid choice. Please enter left or straight or inventory")
        right_door_if_you_went_straight()
    
        
# level 3:
#!!!!!!!!!!!!!!!!!!!!!!!!!!!!!

def level_3_choices():
    print("")
    print("--------------------------------------------------------------------")
    print("")
    print("You enter a large room with a podium in the middle")
    print("Everywhere are mushrooms in every kind of shape and size")
    print("The room also has three doors")
    print("What do you do ? (podium/left/right/back/straight/inventory)")

    choice = input().lower()

    if choice == "podium":
       if "magical_crystal" in inventory and "fragment_left" in inventory and "fragment_right" in inventory:
          inventory["magical_crystal"] = 0
          inventory["fragment_left"] = 0
          inventory["fragment_right"] = 0
          inventory["magical_key"] = 1          
          print("")
          print("--------------------------------------------------------------------")
          print("")
          print("you step to the podium and something strange happens")
          print("the magical crystal in your pocket starts vibrating and flys to the podium ")
          print("the two fragments also do that")
          print("there is a loud POW!!!! and the components combine into a magical key")

          print("there is only one way to go now")
          level_3_choices()

       else:
          print("")
          print("--------------------------------------------------------------------")
          print("")
          print("you step to the podium but nothing happes")
          level_3_choices()

    elif choice == "left":
         level_3_left()
    
    elif choice == "right":
         level_3_right()
    
    elif choice == "straight":
         level_3_straight()
     
    elif choice =="back":
         right_door_if_you_went_straight()
    
    elif choice == "inventory":
          show_inventory()
          level_3_choices()

    elif choice == "quit":
          print("")
          print("--------------------------------------------------------------------")
          print("Quitting, going to start all over")
          return
        
    else:
        print("")
        print("--------------------------------------------------------------------")
        print("Invalid choice. Please enter left or straight or podium or inventory")
        level_3_choices()

# rooms you can enter in level 3:

#gets u fragment
def level_3_left():
     print("")
     print("--------------------------------------------------------------------")
     print("you open the left door")
     print("another empty room this time without doors put it is extremly hot")
     print("but wait there is something on the floor a key like fragment ")
     print("what will you do? (back/pick_up/inventory)")
        
     choice = input().lower()
        

     if choice == "pick_up":
          if "fragment_left" in inventory:
               print("")
               print("-------------------------------------------------------")
               print("nice try but you cant pick it up twice")
               print("-------------------------------------------------------")
               level_3_left()
          else:
               inventory["fragment_left"] = 1
               print("")
               print("-------------------------------------------------------")
               print("")
               print("you pickled up a fragment, your Invntory holds 1 fragment now")
               print("what will that be used for?")
               level_3_left()
                         
                         
        
     elif choice == "back":
          level_3_choices()
        
     elif choice == "inventory":
          show_inventory()
          level_3_left()
        
     elif choice == "quit":
          print("")
          print("Quitting, going to start all over")
          print("")
          return
        
     else:
          print("Invalid choice. Please enter back or pick_up")
          level_3_left()

#gets u fragment
def level_3_right():
     print("")
     print("--------------------------------------------------------------------")
     print("you open the right door")
     print("another empty room this time without doors put it is extremly cold")
     print("but wait there is something on the floor a key like fragment ")
     print("what will you do? (back/pick_up/inventory)")
        
     choice = input().lower()
        

     if choice == "pick_up":
          if "fragment_right" in inventory:
               print("")
               print("-------------------------------------------------------")
               print("nice try but you cant pick it up twice")
               print("-------------------------------------------------------")
               level_3_right
          
          else:
               inventory["fragment_right"] = 1
               print("")
               print("-------------------------------------------------------")
               print("")
               print("you pickled up a fragment, your Invntory holds 1 fragment now")
               print("what will that be used for?")
               level_3_right()
                         
                         
        
     elif choice == "back":
          level_3_choices()
        
     elif choice == "inventory":
          show_inventory()
          level_3_right()
        
     elif choice == "quit":
          print("")
          print("Quitting, going to start all over")
          print("")
          return
        
     else:
          print("Invalid choice. Please enter back or pick_up")
          level_3_right()

#gets u free if you have the key
def level_3_straight():
     print("")
     print("--------------------------------------------------------------------")
     print("")
     if "magical_key" in inventory:
        print("")
        print("--------------------------------------------------------------------")
        print("")
        print("you open the door and fresh air blows you in the nose")
        print("it is a warm nice day and you have to get used to the brightness first")
        end()
     else:
          print("")
          print("--------------------------------------------------------------------")
          print("")
          print("There is a huge wooden door and you can see the sun lickering through")
          print("but it is locked you got to get the key first")
          print("you return to the big room")
          level_3_choices()

# the endings
def end():
    print("you open the door and the sunlight shines in your face")
    print("you cant believe youve made it through this")
    print("youre suprised to see somebody covered in wine standing in youre reach")
    print("It is Mr.Fusselbuss and he is glancing at you")
    print("------------------------------------------------------------------------")
    print("")
    print("Fusselbuss: I didnt think you would make it through")
    print("You: So you locked me in here!!! ")
    print("Fusselbuss: Yes i wanted the production of jam to stop")
    print("Fusselbuss: i just cant take it youre so famous for your jam and i try to mage my own products out of mushrooms but nobody likes them")
    print("You: ")
    print("------------------------------------------------------------------------")
    print("")
    print("i hope you liked the adventure")
    print("paypal me lol (quit)")

    choice = input().lower()
    
    if choice == "quit":
       start_game()         
            
start_game()