class Statistics:
   def __init__(self):
      self.numbers = []

   def add(self, number):
      self.numbers.append(number)

   def display(self):
      print(" ".join(map(str, self.numbers)))

   def max(self):
      return max(self.numbers)

   def min(self):
      return min(self.numbers)

   def mean(self):
      return sum(self.numbers) / len(self.numbers)

   def median(self):
      sorted_nums = sorted(self.numbers)
      n = len(sorted_nums)
      if n % 2 == 0:
         return (sorted_nums[n//2 - 1] + sorted_nums[n//2]) / 2
      else:
         return sorted_nums[n//2]

   def print_stats(self):
      print(f"Min: {self.min()}")
      print(f"Max: {self.max()}")
      print(f"Mean: {self.mean():.2f}")
      print(f"Median: {self.median():.2f}")
