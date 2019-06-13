from functools import wraps
def log(note=None):
    '''一个log的decorator，它既支持@log(),
        又支持：@log('execute')
    '''
    text = str(note) if note else ''
    def decorator(func):
        @wraps(func)
        def wrapper(*args, **kwargs):
            print(f'begin call {func.__name__}')
            res = func(*args, **kwargs)
            print(f'end call {func.__name__}, {text} finish.')
            return res
        return wrapper
    return decorator

@log()
def f1():
    print('running in f1().')
@log('execute')
def f2():
    print('running in f2().')

if __name__ == '__main__':
    f1()
    print('**'*15)
    f2()

