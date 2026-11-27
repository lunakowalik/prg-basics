class Contact_List:
   def __init__(self):
      self.contacts = []

   def add(self, contact):
      self.contacts.append(contact)

   def display(self):
      for contact in self.contacts:
         print(contact)
