# main program
import tv

def main():
   # object creation
   my_tv = tv.TV()

   # object usage
   my_tv.show_status()
   my_tv.turn_on()
   my_tv.show_status()
   my_tv.show_channels()
   my_tv.set_channels(["TVP1", "TVP2", "Polsat", "TVN", "Filmbox", "Discovery"])
   my_tv.show_channels()
   my_tv.show_status()
   my_tv.turn_off()
   my_tv.show_status()

if __name__ == "__main__":
   main()
