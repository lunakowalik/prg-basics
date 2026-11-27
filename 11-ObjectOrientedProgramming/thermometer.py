# class definition
class Thermometer:
   def __init__(self):
      self.temperature = 0.0

   def turn_on(self):
      pass

   def turn_off(self):
      pass

   def measure(self):
      import random
      self.temperature = round(random.uniform(34.0, 42.0), 1)

   def display(self):
      print(f"Temperature: {self.temperature}C", end="")
      if self.temperature >= 37.0:
         print(" (fever)")
      else:
         print()

      if self.temperature >= 41.0:
         print("CRITICAL TEMPERATURE!!")
