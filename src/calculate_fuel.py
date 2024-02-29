def calculate_fuel(distance):
  # Type your code
  fuel = distance * 10
  if distance < 0:
    return False
  elif fuel < 100:
    return 100
  else:
    return fuel