 # Penny Madsen, Rahul Nair, George Huang
from Vase import Vase
from Wardrobe import Wardrobe
from Window import Window
from Door import Door
from Door import room1
from Wardrobe import inventory
from Hallway import Hallway
vase_broken = False
window_closed = True
injury = False
current_location = "start"
visits = 0
gameover = False

print("Hello! Welcome to our storytelling game. You find yourself trapped in a room and must make a series of choices to escape. Make sure to type full words and nothing extra. To start type start!")
user_input = input().lower()
if user_input == "start":
    print("Groggy, you wake up alone. Your head aches slightly and you feel disoriented. Where are you? ")
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
            my_vase = Vase()
            my_vase.vase_interaction()
            visits += 1
        elif choice == "wardrobe":
            current_location = "wardrobe"
            my_wardrobe = Wardrobe()
            my_wardrobe.wardrobe_interaction()
        elif choice == "window":
            current_location = "window"
            my_window = Window()
            my_window.window_interaction()
        elif choice == "door":
            current_location = "door"
            my_door = Door()
            my_door.door_interaction()
    else:
        print("Sorry, I don't understand that command.")
else:
    print("You stare at the ceiling and contemplate your existence. Eventually you fall asleep")

def nextStep():
  print ("where do you want to go?")
  if current_location == "wardrobe":
      print("- Window")
      print("- Vase")
      print("- Door")
  elif current_location == "window":
      print("- Wardrobe")
      print("- Vase")
      print("- Door")
  elif current_location == "door":
      print("- Window")
      print("- Vase")
      print("- Wardrobe")
  elif current_location == "vase":
      print("- Window")
      print("- Door")
      print("- Wardrobe")
  else:
      print ("sorry, I did not understand")

while room1 is True :
  nextStep()
  user_input = input().lower()
  if user_input == "window":
      current_location = "window"
      print("You walk towards the window.")
      my_window = Window()
      my_window.window_interaction()
  elif user_input == "wardrobe":
      current_location = "wardrobe"
      print("You walk towards the wardrobe.")
      my_wardrobe = Wardrobe()
      my_wardrobe.wardrobe_interaction()
  elif user_input == "vase":
    current_location = "vase"
    print("You walk towards the vase.")
    my_vase = Vase()
    my_vase.vase_interaction()
    visits += 1
  elif user_input == "door":
    current_location = "door"
    print("You walk towards the door.")
    my_door = Door()
    my_door.door_interaction()
    room1 = False
  else:
      print("Not an option")
    
# def death():


def stairs():
  if visits >= 2:
    print("You descend down the staircase into the gloom, limping slightly. You hadn't realized how deep the porcelain had pierced you. Ready to look around?")
    user_input = input().lower()
    if user_input == "yes":
      print("At the bottom, you find cold, slightly slimy stone and shadows. As your eyes adjust you realize you're in a dungeon. You can't see anyone, but you hear groans and cries of pain. A sense of primal horror overcomes you. You need to leave now. Will you?")
      user_input = input().lower()
      if user_input == "yes":
        print("You turn to go back up the stairs, but you find your feet won't move. The slime on the stone floor has found its way into your foot wound and is starting to infect your body")
        print("You die slowly, inflitrated by a kind of fungus.")
        gameover = True
      else:
        print("You try to be brave, but your body disobeys and you flee anyway.")
        print("You turn to go back up the stairs, but you find your feet won't move. The slime on the stone floor has found its way into your foot wound and is starting to infect your body")
        print("You die slowly, inflitrated by a kind of fungus.")
        gameover = True
    else:
      print("Ready or not, here we go!")
      print("At the bottom, you find cold, slightly slimy stone and shadows. As your eyes adjust you realize you're in a dungeon. You can't see anyone, but you hear groans and cries of pain. A sense of primal horror overcomes you. You need to leave now. Will you?")
      user_input = input().lower()
      if user_input == "yes":
        print("You turn to go back up the stairs, but you find your feet won't move. The slime on the stone floor has found its way into your foot wound and is starting to infect your body")
        print("You die slowly, inflitrated by a kind of fungus.")
        gameover = True
      else:
        print("You try to be brave, but your body disobeys and you flee anyway.")
        print("You turn to go back up the stairs, but you find your feet won't move. The slime on the stone floor has found its way into your foot wound and is starting to infect your body")
        print("You die slowly, inflitrated by a kind of fungus.")
        gameover = True
# Bird in dungeon
  else:
    print("You descend down the staircase into the gloom. Ready to look around?")
    user_input = input().lower()
    if user_input == "yes":
      print("At the bottom, you find cold, slightly slimy stone and shadows. As your eyes adjust you realize you're in a dungeon.") 
      print("You can't see anyone, but you hear groans and cries of pain. A sense of primal horror overcomes you.")
      if "bird friend" in inventory:
        print("But then your bird chirps on your shoudler. Suddenly everything seems a lighter brighter, a little happy. You continue through the dungeon until you find a door. It opens into the outside world, and you and your bird walk out free!")
        gameover = True
      else:
        print("You need to leave now. Will you?")
        user_input = input().lower()
        if user_input == "yes":
          print("You turn back up the stairs. The ground is tacky from the slime and your feet stick briefly. You run as fast as you can back up the stairs")
          my_hallway = Hallway()
          my_hallway.right()
        else:
          print("You try to be brave, but your body disobeys and you flee anyway. You turn back up the stairs. The ground is tacky from the slime and your feet stick briefly. You run as fast as you can back up the stairs")
          print("Back at the top of the stairs, the staircase is your only choice")
          my_hallway = Hallway()
          my_hallway.right()
    else:
      print("Ready or not, here we go!")
      print("At the bottom, you find cold, slightly slimy stone and shadows. As your eyes adjust you realize you're in a dungeon.") 
      if "bird friend" in inventory:
        print("You can't see anyone, but you hear groans and cries of pain. A sense of primal horror overcomes you.")
        print("But then your bird chirps on your shoudler. Suddenly everything seems a lighter brighter, a little happy. You continue through the dungeon until you find a door. It opens into the outside world, and you and your bird walk out free!")
        gameover = True
      

if gameover is False:
  print ("You emerge into a well lit hallway. The floor is carpet but slightly moist in a disturbing way. To your left, you can see the end of the hallway, while to the right it seems to go on forever")
  user_input = input().lower()
  if user_input == "left":
      print("At the end of the hallway, there's a large window and a staircase.")
      user_input = input().lower()
      if user_input == "window":
        print("You look out through the glass panes and feel a longing for the outdoors. You consider smashing the thin glass and jumping through, but are you that daring?")
        user_input = input().lower()
        if user_input == "yes":
          print("The glass cuts a lot more than you expect. The ground doesn't feel as far away as it looked while you plummet, but you don't have that much time to consider. You die quickly on impact")
          gameover = True
        elif user_input == "no":
          print("The ground is REALLY far away. The stairs seem like a much better escape route")
          stairs()
          user_input = input().lower()
      elif user_input == "staircase":
        stairs()
  elif user_input == "right":
    my_hallway = Hallway()
    my_hallway.right()