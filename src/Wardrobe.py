# Penny Madsen, Rahul Nair
wardrobe_toast = True
openned_message = "The drawers are empty"
inventory = []
class Wardrobe:
  def wardrobe_interaction(self):
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
    elif user_input == "no":
        print("You close the dusty wardrobe doors and look around.")

    else:
        print("Sorry, I didn't understand that. Please type 'yes' or 'no'.")

