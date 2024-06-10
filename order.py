import funcCtrl

def process_order(dish, func):
    print(func(dish))

process_order("Chilli sin carne", funcCtrl.order)
process_order("Chilli sin carne", funcCtrl.prepared)
process_order("Chilli sin carne", funcCtrl.cooked)
process_order("Chilli sin carne", funcCtrl.ready)
