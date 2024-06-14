import funcCtrl
from OOP.Car import Car


def process_order(dish, func):
    print(func(dish))

process_order("Chilli sin carne", funcCtrl.order)
process_order("Chilli sin carne", funcCtrl.prepared)
process_order("Chilli sin carne", funcCtrl.cooked)
process_order("Chilli sin carne", funcCtrl.ready)

car1 = Car('Ford', 'Mustang', 'black')
process_order(str(car1), funcCtrl.order)
process_order("Car " + str(car1), funcCtrl.prepared)
process_order("Car " + str(car1), funcCtrl.ready)
