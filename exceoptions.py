prices = [250, 300, "240", 400]
try:
  #block that may cause an exception
  total = sum(prices)
  print(total)

except TypeError:
  # to perform if there is an exception
  print("Invalid data type")

print("Happy Shopping")

rating = 15
if rating > 10 or rating < 0:
  raise ValueError("Rate from 0 to 10")
# except ValueError: TODO: catch exception
