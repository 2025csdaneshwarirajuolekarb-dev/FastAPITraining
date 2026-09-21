#concept=decorator is a python function that
#lets you modify a function without rewriting the whole codeusing @ symbol
def my_decorator(func):
    def wrapper():
        print(" before ")
        func()
        print(" after ")
    return wrapper


@my_decorator
def say_hello():
    print("Hello!")
say_hello()