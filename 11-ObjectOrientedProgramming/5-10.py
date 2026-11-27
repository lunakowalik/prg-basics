# main program
import stadium

def main():
   stadium_obj = stadium.C({"A": 120, "D": 150, "G": 90, "K": 110})

   stadium_obj.m1("G", 130)

   print(f"C({stadium_obj.sectors!r})")
   print("m1(\"G\",130)")
   print(f"m2(\"GD\") returns {stadium_obj.m2('GD')}")
   print(f"m2(\"KEJ\") returns {stadium_obj.m2('KEJ')}")

if __name__ == "__main__":
   main()
