class HumanToy:
    def __init__(self, hand, legs):
        self.hand = hand
        self.legs = legs

    def wolkForward(self):
        pass

    def run(self):
        userinput = int(input("Left or Rignt!! If Left press 1 and for Right Press 2:"))
        if userinput == 1:
            print("Order Copied !! Running Left")
        elif userinput == 2:
            print("Order Copied !! Running Right")
        else:
            print("Did not undertsand")

    def talk(self):
        print("Yes Boss I am Talking")

    def getHandAndLegs(self):
        self.eyes = 2
        print("I have {}s and {}s and {} eyes".format(self.hand, self.legs, self.eyes))

    def Fight(self):
        pass


if __name__ == "__main__":
    toy1 = HumanToy(2, 3)
    toy1.getHandAndLegs()
    toy1.run()
