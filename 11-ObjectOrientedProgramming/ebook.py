class EBook:
   def __init__(self, title, author, num_pages):
      self.title = title
      self.author = author
      self.num_pages = num_pages
      self.current_page = 1
      self.is_open = False

   def open(self):
      self.is_open = True

   def close(self):
      self.is_open = False

   def read(self, pages):
      if self.is_open:
         self.current_page += pages
      else:
         print("The book is closed")

   def show_status(self):
      print(f"Title: {self.title}")
      print(f"Author: {self.author}")
      print(f"Pages: {self.num_pages}")
      print(f"Current page: {self.current_page}")
