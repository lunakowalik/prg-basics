# main program
import points

def main():
   points_obj = points.C([[2,3],[1,8],[-6,4],[3,-7]])

   print(f"C({points_obj.coordinates!r})")
   print(f"m(2) returns {str(points_obj.m(2))!r}")
   print(f"m(5) returns {str(points_obj.m(5))!r}")

if __name__ == "__main__":
   main()
