def sum_even_nums_in_range(start, stop):
  # Type your code
  return sum(x for x in range(start, stop+1) if x % 2 == 0)
