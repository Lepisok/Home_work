from functools import wraps


def type_logger(func):

    @wraps(func)
    def wrapper(*args, **kwargs):
        result = func(*args, **kwargs)
        print(', '.join(map(lambda x: f'{func.__name__}({x}: {str(type(x))}) -> {str(type(result))}', args)))
        print(', '.join(map(lambda x: f'{x}: {kwargs.get(x)} {str(type(kwargs.get(x)))}', kwargs)))
        return result

    return wrapper


@type_logger
def some_func(*args, **kwargs):
    pass


a = some_func(3, (2, 2), 'abc', some_func, param_1='a', param_2=[324, ])