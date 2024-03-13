# Penny Madsen, Rahul Nair
from Wardrobe import inventory
intact = True
window_closed = True
class Window:
    window_closed = True  # Define and initialize the window_closed attribute within the class

    def window_interaction(self):
        if self.window_closed:  # Access the window_closed attribute using self
            print("The window is narrow and tall, with four panels. You see hinges and a small latch, so you try to open it. It won't budge. Outside you can see a bird on a tree, but the angle is such that you can't tell how far from the ground you are. \n")

            if "brass key" in inventory:
                print("Do you wish to unlock the window?. \n")
                user_input = input().lower()  # Convert user input to lowercase

                if user_input == "yes":
                    self.window_closed = False  # Access and update the window_closed attribute using self
                    print("The key fits! You ease the window open and stick your head out. The ground is dizzingly far away. The bird cocks its head at you. Are you a good person?. \n")
                    user_input = input().lower()

                    if user_input == "yes":
                        print("You call to the bird and it hops closer. You just made a friend. \n")
                        inventory.append("bird friend")
                    elif user_input == "no":
                        print("You call to the bird and grab it as it hops closer. You just found a snack. \n")
                        inventory.append("bird")
                    else:
                        print("Questioning your own morality can be a difficult task. Please try again. \n")
                elif user_input == "no":
                    print("You have better things to do with your time and your key than unlock this window. Everyone knows you can only use keys once. \n")
                else:
                    print("A simple yes or no will suffice")
        else:
          print("The breeze from the window raises goosebumps on your arms. \n")