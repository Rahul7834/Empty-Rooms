# Penny Madsen
from Wardrobe import inventory
class Hallway:
  def right(self):
    print("You look down the long hallway and really can't seem to see an end. Well, best start walking.")
    print("You walk for a long time, passing empty room after empty room. After a while, you get quite hungry. Check your pocket?")
    user_input = input().lower()
    if user_input == "yes":
      if "stale toast" in inventory :
        print("You have a piece of stale toast in your pocket from the wardrobe. You eat it and it's surprisingly good. Or maybe you were just hungry")
      elif "bird" in inventory :
        print("You eat the bird from earlier and feel guilty, but less hungry. You wish you were less lonely.")
      elif "bird" in inventory and "stale toast" in inventory :
        print ("You have a piece of stale toast and a dead bird in your pocket. Which do you want to eat?")
        user_input = input().lower()
        if user_input == "toast":
          print ("You eat it and it's surprisingly good. Or maybe you were just hungry")
        elif user_input == "bird":
          print("You eat the bird from earlier and feel guilty, but less hungry. You wish you were less lonely.")
      else:
        print("Nothing but some pieces of lint. If only you'd found food in your room")
    print("Do you want to enter one of the rooms?")
    user_input = input().lower()
    if user_input != "yes":
      print("You walk farther down the hallway, but still nothing changes. Eventually, you give up your stubborn ways.")
    print("Finally you try your luck in one of the empty rooms. Why didn't you earlier?")
    print("You enter the room and the door slams shut behind you. Great. It's eerily similar to ~your~ room, with the same window at the far wall. You go to the window and consider your options")
    user_input = input().lower()
    if user_input == "smash" or user_input == "jump" or user_input == "break":
      print("You smash your way through the window. It hurts much more than you expect, but at least the plummet to the ground is short. You die far too slowly after you land")
    elif user_input == "open" or user_input == "look" or user_input == "examine":
      print("You carefully examine the window and find that it opens quite easily. Things aren't always complicated. Looking out on the ground, you find that it's much closer than you thought. You can't remember going down on your long trek through the hallway, and yet the ground is just a couple feet away.")
      print("You carefully climb and emerge free at last!")
    elif user_input == "help":
      print("You have to go out the window one way! Either smash it or examine it")
    else:
      print("For this last choice, you haven't been given the options. Time to be creative! Or ask for help if you can't figure it out")
      user_input = input().lower()
      if user_input == "smash" or user_input == "jump" or user_input == "break":
        print("You smash your way through the window. It hurts much more than you expect, but at least the plummet to the ground is short. You die far too slowly after you land")
      elif user_input == "open" or user_input == "look" or user_input == "examine":
        print("You carefully examine the window and find that it opens quite easily. Things aren't always complicated. Looking out on the ground, you find that it's much closer than you thought. You can't remember going down on your long trek through the hallway, and yet the ground is just a couple feet away.")
        print("You carefully climb and emerge free at last!")
  