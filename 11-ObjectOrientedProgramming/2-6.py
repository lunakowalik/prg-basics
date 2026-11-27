# class definition
class Phone:
    def __init__(self):
        self.battery_level = 100
        self.volume = 50
        self.is_on = False
        self.screen_brightness = 70

    def turn_on(self):
        self.is_on = True
        print("Phone turned on")

    def turn_off(self):
        self.is_on = False
        print("Phone turned off")

    def adjust_volume(self, change):
        self.volume = self.volume + change
        if self.volume > 100:
            self.volume = 100
        if self.volume < 0:
            self.volume = 0
        print(f"Volume adjusted to {self.volume}%")

    def adjust_brightness(self, change):
        self.screen_brightness = self.screen_brightness + change
        if self.screen_brightness > 100:
            self.screen_brightness = 100
        if self.screen_brightness < 0:
            self.screen_brightness = 0
        print(f"Screen brightness adjusted to {self.screen_brightness}%")

    def get_status(self):
        print(f"Phone Status:")
        print(f"  Battery: {self.battery_level}%")
        print(f"  Volume: {self.volume}%")
        print(f"  Screen brightness: {self.screen_brightness}%")
        if self.is_on:
            print("  Power: ON")
        else:
            print("  Power: OFF")


def main():
    # object creation based on the Phone class
    phone = Phone()
    print("Initial phone status:")
    phone.get_status()
    print()

    # object manipulation
    phone.turn_on()
    print()
    phone.adjust_volume(20)
    phone.adjust_brightness(-15)
    phone.get_status()
    print()

if __name__ =="__main__":
    main()
