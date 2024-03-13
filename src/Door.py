# Penny Madse, Rahul Nair     
from Wardrobe import inventory
locked=True
room1 = True

class Door:
  def door_interaction(self):
    print("""   
           ,-' ;  ! `-.
         |_ ;   __:  ; |
         )| .  :)(.  ! |
         |"    (##)  _ |
         |  :  ;`'  (_)(
         |  :  :  .    |
          )_ !  ,  ;  ;|
         || .  .  :  : |
         |" .  |  :  . |
         |mt-2_;----.__|
         """)
    print("The door is cheaply painted white with a metal doorknob. You try to open it, but it's locked.")
    if "brass key" in inventory:
        print("Try your key in this hole?")
        user_input = input().lower() 
        if user_input == "yes":
            print("The key clicks as it turns the lock. Yes! The door opens")
            room1 = False
        else:
            print("You might need this key for something else, and everyone knows you can only use keys once")
    else:
        print("This door is useless to you at the moment")