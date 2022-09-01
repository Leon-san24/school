import time


class Traffic_light:

    def __init__(self, model, colors, country):
        self.model: str = model
        self.colors: list = colors
        self.lamps: list = len(colors)
        self.country: str = country
        self.status: int = 1


    def set_status(self):
        lamps = self.lamps
        flag = 1
        while lamps > flag:
            self.status += 1
            self.show()
            flag += 1

    def get_status(self):
        status = self.status
        return status

    def switch(self):
        self.set_status()

    def show(self):
        status = self.get_status()
        colors = self.colors
        print(f"Die Ample ist {colors[status-1]}")


newAmpel = Traffic_light("1.01", ["Rot", "Gelb", "Grün", "Blau"], "Germany")

newAmpel.show()
newAmpel.switch()






