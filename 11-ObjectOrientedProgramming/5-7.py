import mod_5_7

def main():
   stats = mod_5_7.Statistics()

   stats.add(12)
   stats.add(37)
   stats.add(6)
   stats.add(9)
   stats.add(17)

   stats.display()

   stats.print_stats()

if __name__ == "__main__":
   main()
