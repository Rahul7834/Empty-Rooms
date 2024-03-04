pain = 0
hunger = 0
inventory = []
current_location = "start"


def look():
  pass

def vase_interaction():
  print("You pick up the vase. It’s surprisingly heavy and very smooth. An impulsive thought of smashing it flashes across your mind. Do you want to smash it or replace it on the wardrobe?")
  while True:
    user_input = input().lower()

    if user_input == "smash":
      print("You drop the vase to the floor and it shatters. Between the porcelain fragments, you can see a brass key. Do you want to leave it or take it?")

      while True:
        user_input = input().lower()

        if user_input == "take it":
          print("You store it in your pocket")
          inventory.append("brass key")  # Add key to inventory
          break
        elif user_input == "leave it":
          print("You leave it on the floor")
          break
        else:
          print("Sorry, I didn't understand that. Please type 'take it' or 'leave it'.")
      break
    elif user_input == "replace it":
      print("You carefully place the vase back on the wardrobe.")
      break
    else:
      print("Sorry, I didn't understand that. Please type 'smash' or 'replace it'.")


def wardrobe_interaction():
  print("You open the wardrobe. It’s dark and dusty. You can’t see anything but a few drawers. Do you open the drawers?")

  user_input = input().lower()  # Convert user input to lowercase

  if user_input == "yes":
    print("You find a stale piece of toast. Do you want to eat it now? Or save it?")

  user_input = input().lower()  # Convert user input to lowercase

  if user_input == "eat":
    print("You eat the stale piece of toast. It doesn't taste great, but it eases your hunger a little.")
  elif user_input == "save":
    print("You decide to save the stale piece of toast in your pocket.")
    inventory.append("stale toast")  # Add toast to inventory
  else:
    print("Sorry, I didn't understand that. Please type 'eat' or 'save'.")


print("Groggy, you wake up alone. Your head aches slightly and you feel disoriented. Where are you?")
print("Do you want to get up?")
user_input = input().lower()  # Convert user input to lowercase

if user_input == "yes":
    print("You push yourself off of the floor and look around the room. There’s a window on the far wall, a door, a wardrobe, and a table with a vase perched on top. Which one do you want to go to? ")
    choice = input().lower()  # Convert user input to lowercase
    valid_options = ["vase", "wardrobe", "window"]  # Define valid options

    if choice in valid_options:
        print(f"You walk towards the {choice}.")
        if choice == "vase":
            vase_interaction()
        elif choice == "wardrobe":
            wardrobe_interaction()
        else:
            print("You walk towards the window.")
            # Implement code for interacting with the window
    else:
        print("Sorry, I don't understand that command.")
else:
    print("You stare at the ceiling and contemplate your existence. Eventually you fall asleep")

print("What do you want to do next?")
print("1. Go to the window")

if current_location != "wardrobe":
  print("2. Go to the wardrobe")
else:
  print("2. Go to the vase")

user_input = input().lower()  # Convert user input to lowercase

if user_input == "window":
  print("You walk towards the window.")
  # Implement code for interacting with the window
elif user_input == "wardrobe":
  if current_location != "wardrobe":
    print("You walk towards the wardrobe.")
    wardrobe_interaction()
    print("What do you want to do next?")
    print("1. Go to the window")
    user_input = input().lower()  # Convert user input to lowercase

    if user_input == "window":
      print("You walk towards the window.")
      # Implement code for interacting with the window
    else:
      print("Sorry, I didn't understand that command.")
  else:
    print("You walk towards the vase.")
    vase_interaction()
else:
  print("Sorry, I didn't understand that. Please type 'window' or 'wardrobe'")