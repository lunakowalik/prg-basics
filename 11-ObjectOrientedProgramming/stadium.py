class C:
   def __init__(self, sectors):
      self.sectors = sectors

   def m1(self, s, n):
      self.sectors[s] = n

   def m2(self, s):
      total = 0
      for sector in s:
         if sector in self.sectors:
            total += self.sectors[sector]
      return total
