import ebook

def main():
   my_book = ebook.EBook("The Great Gatsby", "F. Scott Fitzgerald", 180)

   my_book.open()

   my_book.show_status()

   my_book.read(10)
   my_book.show_status()

   my_book.close()

   my_book.read(5)
   my_book.show_status()

if __name__ == "__main__":
   main()
