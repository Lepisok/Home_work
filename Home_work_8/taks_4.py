from functools import wraps
import inspect


def true_checker(lst):
    for e in lst:
        if not e:
            return False
    return True


def val_checker(f_check):
    f_name = val_checker.__name__

    def _val_checker(func):
        @wraps(func)
        def wrapper(*args, **kwargs):
            if true_checker(map(f_check, args)):
                return func(*args, **kwargs)
            raise ValueError(f'{args} не все элементы подходят условию '
                             f'{inspect.getsourcelines(f_check)[0][0].strip().replace(f"@{f_name}", "")}')

        return wrapper

    return _val_checker


@val_checker(lambda x: x > 0)
def f_1(*n):
    print(*n)


x = f_1(2, -5, 4)
