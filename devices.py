class SmartHome:
    def __init__(self):
        self.light = False
        self.fan = False
        self.ac = False

    def show_status(self):
        print("\n------ SMART HOME STATUS ------")
        print(f"💡 Light : {'ON' if self.light else 'OFF'}")
        print(f"🌬 Fan   : {'ON' if self.fan else 'OFF'}")
        print(f"❄ AC     : {'ON' if self.ac else 'OFF'}")
        print("-------------------------------")