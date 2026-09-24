def repeat_func(func):
    def wrapper(text, count=1):
        for x in range(count):
            func(text)
    return wrapper


@repeat_func
def example(text):
    print(text)


example('print me', count=2)

print("---")


# Задание на декоратор с параметрами


def repeat_me(count):
    def decorator(func):
        def wrapper(text):
            for x in range(count):
                func(text)
        return wrapper
    return decorator


@repeat_me(count=5)
def example(text):
    print(text)


example('print me')
