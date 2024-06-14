class Car:
  # Initialize attributes
  def __init__(self, brand, color, model):
    # Assign values to attributes
    self.brand = brand
    self.model = model
    self.color = color

  def __str__(self):
    return f"{self.brand} {self.model} ({self.color})"

# Create an object of the Car class
my_car = Car('Audi', 'yellow', 'Q5')

print('Car: ', my_car)
print('Brand: ', my_car.brand)
print('Model: ', my_car.model)
print('Color: ', my_car.color)
