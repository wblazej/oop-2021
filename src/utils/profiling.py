import time


def profile(funct):
    def wrapper(*args, **kw):
        start = time.time()
        ret = funct(*args, **kw)
        print(f'Function {funct.__name__} done in {time.time() - start:.3f}s')
        return ret

    return wrapper
