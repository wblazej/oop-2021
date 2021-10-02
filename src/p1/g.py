from time import sleep
from utils.profiling import profile


@profile
def foo():
    sleep(1)


if __name__ == '__main__':
    foo()