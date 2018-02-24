def my_decorator(some_function):
    def wrapper():
        print("vijay")
        some_function()
        print('csgeeks')

    return wrapper

@my_decorator
def just_some_function():
    print('youtube')
just = my_decorator(just)
just_some_function()

