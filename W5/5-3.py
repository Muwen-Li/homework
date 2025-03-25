class Engine:
    def __init__(self,power):
        self.power=power

class Vehicle:
    def __init__(self,wheels,engine):
        self.wheels=wheels
        self.engine=Engine(engine)

    def display_info(self):
        print(f"轮子数量:{self.wheels}")
        print(f"发动机动力：{self.engine.power}")

engine=input()
vehicle=Vehicle(4,engine)
vehicle.display_info() 