def log_decorator(func):
    def wrapper(*args, **kwargs):
        print(f'calling {func.__name__} with {args}, {kwargs}')
        return func(*args, **kwargs)
    return wrapper

@log_decorator
def add_num(a,b):
    print (f'sum:{a+b}')
if __name__ == '__main__':
    add_num(a=4,b=6)
    add_num(5,6)
