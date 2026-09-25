def finish_func(func):
    def wrapper(args):
        func(args)
        print("finished")
    return wrapper


@finish_func
def greet_func(text):
    print(text)


greet_func('Hello')
