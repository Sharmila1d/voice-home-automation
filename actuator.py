from devices import SmartHome

class Actuator:
    def __init__(self, home):
        self.home = home

    def execute(self, command):

        if command == "LIGHT_ON":
            self.home.light = True

        elif command == "LIGHT_OFF":
            self.home.light = False

        elif command == "FAN_ON":
            self.home.fan = True

        elif command == "FAN_OFF":
            self.home.fan = False

        elif command == "AC_ON":
            self.home.ac = True

        elif command == "AC_OFF":
            self.home.ac = False

        else:
            print("❌ Unknown Command")