class C:
   def __init__(self, name, surname, age, seniority):
      self.name = name
      self.surname = surname
      self.age = age
      self.seniority = seniority

   def __str__(self):
      first_letter = self.name[0]
      if self.age >= 18:
         first_letter = first_letter.upper()
      return f"{self.surname}{first_letter}{self.seniority}"
