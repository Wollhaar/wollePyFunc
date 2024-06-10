import funcCtrl

def process_user(name, func):
    return func(name)

print(process_user("Alice", funcCtrl.welcome))
print(process_user("Alice", funcCtrl.bye))
