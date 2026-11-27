# main program
import contact
import contact_list

def main():
   contact_list_obj = contact_list.Contact_List()

   contact_list_obj.add(contact.Contact("John Brown", "brown@onet.pl", "555234000"))
   contact_list_obj.add(contact.Contact("Anna May", "am@o2.pl", "232000199"))
   contact_list_obj.add(contact.Contact("George Small", "smallg@google.pl", "222999100"))
   contact_list_obj.add(contact.Contact("Paola Big", "bigpaola@poczta.pl", "100200300"))

   contact_list_obj.display()

if __name__ == "__main__":
   main()
