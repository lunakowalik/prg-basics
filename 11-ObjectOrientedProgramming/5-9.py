# main program
import employee

def main():
   emp1 = employee.C("Anna", "May", 17, 7)
   emp2 = employee.C("George", "Brown", 21, 4)

   print(f"C({emp1.name!r},{emp1.surname!r},{emp1.age},{emp1.seniority}) returns {str(emp1)!r}")
   print(f"C({emp2.name!r},{emp2.surname!r},{emp2.age},{emp2.seniority}) returns {str(emp2)!r}")

if __name__ == "__main__":
   main()
