intact = True
shattered_message = "The vase is shattered on the floor."

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