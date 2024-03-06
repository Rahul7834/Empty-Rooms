intact = True
shattered_message = "The vase is shattered on the floor."
inventory = []
class Vase:
    def smash(self):
        global intact
        intact = False
        print("You drop the vase to the floor and it shatters. Between the porcelain fragments, you can see a brass key.")

    def examine(self):
        if intact:
            print("The vase is surprisingly heavy and very smooth.")
        else:
            print(shattered_message)
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