# Penny Madsen
from Wardrobe import inventory
# from main import injury
global vase_broken
vase_broken=False

class Vase:
    def vase_interaction(self):
      global vase_broken
      if not vase_broken:
            print("""   
                ________
              .:________:.
               \        /
                )      (  
               /        \\
             ,'          `.
             /             \\
            /               \\
            (               )
            \\               /
             `.            ,'
               `.________,'""")
            print("You pick up the vase. It’s surprisingly heavy and very smooth. An impulsive thought of smashing it flashes across your mind. Do you want to smash it or replace it on the table?")
            user_input = input().lower()
            if user_input == "smash" or user_input == "smash it":
              print("You drop the vase to the floor and it shatters. Between the porcelain fragments, you can see a brass key. Do you want to leave it or take it?")
              user_input = input().lower()
              if user_input == "take" or user_input == "take it":
                    print("You store it in your pocket")
                    inventory.append("brass key")  # Add key to inventory
                          
              elif user_input == "leave" or user_input == "leave it":
                    print("You leave it on the floor")
                          
              elif user_input == "help":
                    print("You can type 'take it' to take the brass key or 'leave it' to leave it on the floor.")
              else:
                    print("Sorry, I didn't understand that. Please type 'take it' or 'leave it'.")
              vase_broken = True
              
            elif user_input == "replace it" or user_input == "replace":
                  print("You carefully place the vase back on the table.")
                  
            elif user_input == "help":
                print("You can type 'smash' to smash the vase or 'replace it' to put it back on the table.")
            else:
                 print("Sorry, I didn't understand that. Please type 'smash' or 'replace it'.")
      else:
          print("Ouch. A piece of the shattered porcelain pierces the bottom of your foot.")
          injury = True
  
  