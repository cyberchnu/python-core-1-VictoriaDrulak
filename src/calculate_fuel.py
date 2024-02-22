def calculate_fuel(distance):
  # Type your code
  fuel_needed = distance * 10
  if fuel_needed < 0:
    print(100)
  else:
    return fuel_needed
