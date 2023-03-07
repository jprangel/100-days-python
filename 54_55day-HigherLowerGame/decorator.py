import time

def delay_decorator(function):
    def wrapper_function(*args, **kwargs):
        print(f'Decorator...')
        time.sleep(2)
        function()
    return wrapper_function

@delay_decorator
def say_hi():
    print('Hi Hi...')

def say_bye():
    print("bye, bye...")

say_hi()