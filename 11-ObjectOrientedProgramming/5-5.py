# main program
import thermometer

def main():
   my_thermometer = thermometer.Thermometer()

   my_thermometer.turn_on()
   my_thermometer.measure()
   my_thermometer.display()
   my_thermometer.turn_off()

if __name__ == "__main__":
   main()
