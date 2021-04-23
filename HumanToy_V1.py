from human import HumanToy


class HumanToy_v1(HumanToy):
    def __init__(self, hand, legs):
        super().__init__(hand, legs)

    def drive(self):
        print("I can drive")

humanToy1 = HumanToy_v1(2,2)
humanToy1.getHandAndLegs()
humanToy1.drive()
