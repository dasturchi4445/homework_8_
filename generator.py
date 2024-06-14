# GENERATOR YARATISH

def simple_generator():
    yield 1
    yield 2
    yield 3


generator = simple_generator()
print(next(generator))
print(next(generator))
print(next(generator))

generator = (x * x for x in range(3))
print(next(generator))
print(next(generator))
print(next(generator))
