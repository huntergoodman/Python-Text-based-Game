#Start prompt
answer = input("This is game is a test of strategy. Type 'yes' if you are up to the task.> ")

if answer.lower().strip() == "yes":

    answer = input("You wake up in the middle of the forest. " + 
                   "Nothing around you. " +
                   "There is a path to the south or you can delve deeper into the forest. " + 
                   "The decision is up to you.> ")
    #Road prompt
    if answer.lower().strip() == "road":
        answer = input("You walk south towards the road. " + 
                       "You make it safely. " +
                       "The road is made of cobblestone and it is well constructed. " + 
                       "There is a crossroad up the road. You can go left or you can go right.> ")
    #Second option for road prompt
    elif answer.lower().strip() == "south":
        answer = input("You walk south towards the road. " + 
                       "You make it safely. " +
                       "The road is made of cobblestone and it is well constructed. " + 
                       "There is a crossroad up the road. You can go left or you can go right.> ")
        
        if answer.lower().strip() == "left":
            answer = input("You decided to head left. " +
                         "The road seems to strech forever onward. " +
                         "It certainly has no sign of ending soon. " +
                         "There is a road sign up ahead. " +
                         "Do you stop to read it?")
        
        elif answer.lower().strip() == "right":
            answer = input("You decided to head right. " +
                           "This road seems short. " + 
                           "You make haste to a small village up the road. " +
                           "How do you treat the villagers once you get there?")
            
        else:
            answer = input("You decided to head right. " +
                           "This road seems short. " + 
                           "You make haste to a small village up the road. " +
                           "How do you treat the villagers once you get there?")
            
            answer = input("You decided to head right. " +
                           "")
            
            if answer.lower().strip() == "yes":
                answer = print("The roadsign points in the direction you're going. " +
                               "The arrow says nothing but 'Dentar'")
                
                answer = input("Do you wish to head to Dentar or " + 
                               "turn back and head to the fork in the road?")
                
    #Forest prompt dead end
    else:
        answer = print("The forest is dense with trees and other vegitation. " + 
                       "It is pretty dark due to the treetops. " + 
                       "It is rather quiet.")

        answer = input("As you walk through the forest it begins getting darker and darker. " + 
                       "The ground gets more and more soft. " + 
                       "It reaches a point where every step is a challenge. " + 
                       "Do you turn back toward the road or keep going?> ")
        #player keeps going, player dies.
        if answer == "keep going":
            answer = print("You keep trudging through the muck. " + 
                           "It eventually hardens around your feet. " + 
                           "You find yourself stuck in the muck. " +
                           "Your eyes begin to grow heavy. " +
                           "You fade away into an eternal slumber. Game Over!")
        
        else :
            answer = print("That was probably for the best. " + 
                  "Who knows how bad that could have gotten.")
            
            answer = input("You come back to the road. " +
                           "There is a fork in the road. " +
                           "You can choose to go left or right.> ")

       
else:
    answer = print("It was obvious that you were would not be up to the task. " + 
          "With those arms... " + 
          "You couldn't lift a pebble off the ground.")
