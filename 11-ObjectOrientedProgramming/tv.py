# class definition
class TV:
   def __init__(self):
      self.is_on = False
      self.channel_no = 1
      self.channels = []

   def turn_off(self):
      self.is_on = False

   def turn_on(self):
      self.is_on = True

   def show_status(self):
      if self.is_on:
         print(f"TV is on, channel {self.channel_no}")
      else:
         print("TV is off")

   def set_channel(self, new_channel_no):
      self.channel_no = new_channel_no

   def set_channels(self, channels_list):
      self.channels = channels_list

   def show_channels(self):
      print("Channel list:")
      for i, channel in enumerate(self.channels, 1):
         print(f"{i}. {channel}")
