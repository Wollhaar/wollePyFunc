def greet(name):
    print("Hey", name)

    def account():
        return "Your account is created!"

    message = account()
    return message

print(greet("Bob"))


def greet():
    return "Welcome!"

#takes a function as an argument
def uppercase(func):
    #wrapper function to keep the
    #original function code unchanged
    def wrapper():
        orig_message = func()
        modified_message = orig_message.upper()
        return modified_message
    return wrapper

greet_upper = uppercase(greet)
print(greet_upper())
