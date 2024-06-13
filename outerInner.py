def greet(name):
    print("Hey", name)

    def account():
        return "Your account is created!"

    message = account()
    return message

print(greet("Bob"))



#takes a function as an argument
def uppercase(func):
    #wrapper function to keep the
    #original function code unchanged
    def wrapper():
        orig_message = func()
        modified_message = orig_message.upper()
        return modified_message
    return wrapper

@uppercase
def greet():
    return "Welcome!"

greet_upper = uppercase(greet)
print(greet_upper())


def stock_status_decorator(func):
    def wrapper(item):
        result = func(item)
        print(result, ": stock status for", item)
        return result
    return wrapper

@stock_status_decorator
def restock_item(item):
    return "Restocked"

@stock_status_decorator
def sell_item(item):
    return "Sold"

print(restock_item("Laptop"))
print(sell_item("Smartphone"))



#It's  a good practice to use *args and **kwargs in the signature of a wrapper function
# within a decorator. This approach ensures that the decorator is versatile and can be applied
# to any function, regardless of the number and type of its arguments.

# Code a wrapper function signature with args and kwargs
# def some_decorator(func):
#   def wrapper(*args, **kwargs):

