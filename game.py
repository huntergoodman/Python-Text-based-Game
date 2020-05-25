#Start prompt
answer = input("This is game is a test of strategy. Type 'yes' if you are up to the task. ")

if answer.lower().strip() == "yes":

    answer = input("You wake up in the middle of the forest. " + 
                   "Nothing around you. " +
                   "There is a path to the south or you can delve deeper into the forest. " + 
                   "The decision is up to you. ")
    #Road prompt
    if answer.lower().strip() == "road":
        answer = input("You walk south towards the road. " + 
                       "You make it safely. " +
                       "The road is made of cobblestone and it is well constructed. " + 
                       "There is a crossroad up the road. You can go left or you can go right. ")
    #Second option for road prompt
    elif answer.lower().strip() == "south":
        answer = input("You walk south towards the road. " + 
                       "You make it safely. " +
                       "The road is made of cobblestone and it is well constructed. " + 
                       "There is a crossroad up the road. You can go left or you can go right. ")
    #Forest prompt dead end, player dies
    else:
        answer = print("The forest is dense with trees and other vegitation. " + 
                       "It is pretty dark due to the treetops. " + 
                       "It is rather quiet.")

        answer = input("As you walk through the forest it begins getting darker and darker. " + 
                       "The ground gets more and more soft. " + 
                       "It reaches a point where every step is a challenge. " + 
                       "Do you turn back toward the road or keep going? ")
        
        if answer == "keep going":
            answer = print("You keep trudging through the muck. " + 
                           "It eventually hardens around your feet. " + 
                           "You find yourself stuck in the muck. " +
                           "Your eyes begin to grow heavy. " +
                           "You fade away into an eternal slumber. Game Over!")

       




else:
    print("It was obvious that you were would not be up to the task. " + 
          "With those arms... " + 
          "You couldn't lift a pebble off the ground.")
