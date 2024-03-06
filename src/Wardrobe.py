wardrobe_toast = True
intact = True
openned_message = "The drawers are empty"
class Wardrobe:
  def smash(self):
      global intact
      intact = False
      print("You drop the vase to the floor and it shatters. Between the porcelain fragments, you can see a brass key.")

  def examine(self):
      if intact:
          print("The vase is surprisingly heavy and very smooth.")
      else:
          print(openned_message)
        
def wardrobe_interaction():
  global wardrobe_toast
  print("You open the wardrobe. It’s dark and dusty. You can’t see anything but a few drawers. Do you open the drawers?")
  user_input = input().lower()  # Convert user input to lowercase
  if user_input == "yes":
    if wardrobe_toast:
      print("You find a stale piece of toast. Do you want to eat it now? Or save it?")
      wardrobe_toast = False
      user_input = input().lower()  # Convert user input to lowercase

      if user_input == "eat" or user_input == "eat it":
          print("You eat the stale piece of toast. It doesn't taste great, but it eases your hunger a little.")
      elif user_input == "save" or user_input == "save it":
          print("You decide to save the stale piece of toast in your pocket.")
          inventory.append("stale toast")  # Add toast to inventory
      else:
          print("Sorry, I didn't understand that. Please type 'eat' or 'save'.")
      vase_broken = True
      break
  elif user_input == "no":
      print("You close the dusty wardrobe doors and look around.")
  else:
      print("Sorry, I didn't understand that. Please type 'yes' or 'no'.")

  wardrobe_opened = True
  return