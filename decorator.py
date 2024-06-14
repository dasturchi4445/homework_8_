def simple_decorator(func):
    def wrapper():
        print("Function is being called")
        func()
        print("Function has been called")
    return wrapper()


@simple_decorator
def say_hello():
    print("hello")


say_hello()



