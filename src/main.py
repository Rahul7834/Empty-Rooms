from Vase import Vase
vase_broken = False
window_closed = True
pain = 0
hunger = 0
inventory = []
current_location = "start"
room1 = True

def look():
    pass

def vase_interaction():
  global vase_broken
  if vase_broken:
      print("Ouch. A piece of the shattered porcelain pierces the bottom of your foot. ")
      return

  print("You pick up the vase. It’s surprisingly heavy and very smooth. An impulsive thought of smashing it flashes across your mind. Do you want to smash it or replace it on the table?")
  while True:
      user_input = input().lower()

      if user_input == "smash" or user_input == "smash it":
          print("You drop the vase to the floor and it shatters. Between the porcelain fragments, you can see a brass key. Do you want to leave it or take it?")

          while True:
              user_input = input().lower()

              if user_input == "take" or user_input == "take it":
                  print("You store it in your pocket")
                  inventory.append("brass key")  # Add key to inventory
                  break
              elif user_input == "leave" or user_input == "leave it":
                  print("You leave it on the floor")
                  break
              else:
                  print("Sorry, I didn't understand that. Please type 'take it' or 'leave it'.")
          vase_broken = True
          break
      elif user_input == "replace it" or user_input == "replace":
          print("You carefully place the vase back on the table.")
          break
      else:
          print("Sorry, I didn't understand that. Please type 'smash' or 'replace it'.")

def wardrobe_interaction():
  print("You open the wardrobe. It’s dark and dusty. You can’t see anything but a few drawers. Do you open the drawers?")
  user_input = input().lower()  # Convert user input to lowercase
  if user_input == "yes":
      print("You find a stale piece of toast. Do you want to eat it now? Or save it?")

      user_input = input().lower()  # Convert user input to lowercase

      if user_input == "eat" or user_input == "eat it":
          print("You eat the stale piece of toast. It doesn't taste great, but it eases your hunger a little.")
      elif user_input == "save" or user_input == "save it":
          print("You decide to save the stale piece of toast in your pocket.")
          inventory.append("stale toast")  # Add toast to inventory
      else:
          print("Sorry, I didn't understand that. Please type 'eat' or 'save'.")
  elif user_input == "no":
      print("You close the dusty wardrobe doors and look around.")
  else:
      print("Sorry, I didn't understand that. Please type 'yes' or 'no'.")

  wardrobe_opened = True
  return


def window_interaction():
    global window_closed
    if window_closed:
        print("The window is narrow and tall, with four panels. You see hinges and a small latch, so you try to open it. It won't budge. Outside you can see a bird on a tree, but the angle is such that you can't tell how far from the ground you are")
    
        if "brass key" in inventory:
            print("Do you wish to unlock the window?")
            user_input = input().lower()  # Convert user input to lowercase
    
            if user_input == "yes":
                window_closed = False
                print("The key fits! You ease the window open and stick your head out. The ground is dizzingly far away. The bird cocks its head at you. Are you a good person?")
                user_input = input().lower() 
    
                if user_input == "yes":
                    print("You call to the bird and it hops closer. You just made a friend")
                elif user_input == "no":
                    print("You call to the bird and grab it as it hops closer. You just found a snack")
                else:
                    print("Questioning your own morality can be a difficult task. Please try again")
            elif user_input == "no":
                print("You have better things to do with your time and your key than unlock this window. Everyone knows you can only use keys once")
            else:
                print("A simple yes or no will suffice ")
    else:
      print("The breeze from the window raises goosebumps on your arms. ")
def door_interaction():
  global room1
  print("The door is cheaply painted white with a metal doorknob. You try to open it, but it's locked.")
  if "brass key" in inventory:
    print("Try your key in this hole?")
    user_input = input().lower() 
    if user_input == "yes":
      print("The key clicks as it turns the lock. Yes! The door opens. Are you ready to leave the room?")
      user_input = input().lower() 
      if user_input == "yes":
        room1 = False
        print("You step out into a hall") #I'm going to add more details
      else:
        print("You close the door and turn back to the room. There might be more things to find, and besides, you're an introvert")
    else:
      print("You might need this key for something else, and everyone knows you can only use keys once")
  else:
    print("This door is useless to you at the moment")

print("Groggy, you wake up alone. Your head aches slightly and you feel disoriented. Where are you?")
print("Do you want to get up?")
user_input = input().lower()  # Convert user input to lowercase

if user_input == "yes":
    print("You push yourself off of the floor and look around the room. There’s a window on the far wall, a door, a wardrobe, and a table with a vase perched on top. Which one do you want to go to? ")
    choice = input().lower()  # Convert user input to lowercase
    valid_options = ["vase", "wardrobe", "window", "door"]  # Define valid options

    if choice in valid_options:
        print(f"You walk towards the {choice}.")

        if choice == "vase":
            current_location = "vase"
            vase_interaction()
        elif choice == "wardrobe":
            current_location = "wardrobe"
            wardrobe_interaction()
        elif choice == "window":
            current_location = "window"
            window_interaction()
        elif choice == "door":
            current_location = "door"
            door_interaction()
    else:
        print("Sorry, I don't understand that command.")
else:
    print("You stare at the ceiling and contemplate your existence. Eventually you fall asleep")

def nextStep():
  print ("where do you want to go?")
  
  if current_location == "wardrobe":
      print("1. Go to the window")
      print("2. Go to the vase")
      print("3. Go to the door")
  elif current_location == "window":
      print("1. Go to the wardrobe")
      print("2. Go to the vase")
      print("3. Go to the door")
  elif current_location == "door":
      print("1. Go to the window")
      print("2. Go to the vase")
      print("3. Go to the wardrobe")
  elif current_location == "vase":
      print("1. Go to the window")
      print("2. Go to the door")
      print("3. Go to the wardrobe")
  else:
      print ("sorry, I did not understand")

while True:
  room1 = True
  nextStep()
  user_input = input().lower()
  if user_input == "window":
      current_location = "window"
      print("You walk towards the window.")
      window_interaction()
  elif user_input == "wardrobe":
      current_location = "wardrobe"
      print("You walk towards the wardrobe.")
      wardrobe_interaction()
  elif user_input == "vase":
    current_location = "vase"
    print("You walk towards the vase.")
    vase_interaction()
  elif user_input == "door":
    current_location = "door"
    print("You walk towards the door.")
    door_interaction()
  else:
      print("Not an option")