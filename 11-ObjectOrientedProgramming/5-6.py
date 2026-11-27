# main program
import bank_account

def main():
   my_account = bank_account.BankAccount("12 3456 5555 9090 1111 0000 7722")

   my_account.display_info()

   my_account.deposit(25.30)
   my_account.display_info()

   my_account.withdraw(31.70)
   my_account.display_info()

   my_account.withdraw(14.00)
   my_account.display_info()

if __name__ == "__main__":
   main()
