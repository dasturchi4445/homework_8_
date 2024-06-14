def decorator_with_arguments(arg1, arg2):
    def decorator(func):
        def wrapper(*args, **kwargs):
            print(f"Arguments passed to decorator : {arg1},{arg2}")
            return func(*args, **kwargs)

        return wrapper

    return decorator


@decorator_with_arguments("hello", "teacher")
def greet(name):
    print(f"hello, {name}")


greet("Zoirjon")
