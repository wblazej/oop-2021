from datetime import datetime
from time import sleep


def logged(custom_logger = None):
    def decorator(fn):
        def log(msg: str):
            print(f'[{datetime.now()}] {msg}')

        def wrapper(*args, **kwargs):
            log_function = log if not custom_logger else custom_logger.log

            log_function(f'Started execution of function {fn.__name__} with arguments {args}')
            ret = fn(*args, **kwargs)
            log_function(f'Finished execution of function {fn.__name__} with arguments {args}')
            
            return ret

        return wrapper
    return decorator


def retry(attempts: int, delay: int = 1, backoff_type: str = 'linear', factor: int = 2):
    def decorator(fn):
        def wrapper(*args, **kwargs):
            attempt_delay = delay
            for i in range(attempts):
                try:
                    ret = fn(*args, *kwargs)
                    return ret
                except (Exception, BaseException) as e:
                    print(f'Failed attempt {i + 1}')

                    if i + 1 == attempts:
                        raise e

                    print(f'Waiting {attempt_delay} seconds')
                    sleep(attempt_delay)

                    if backoff_type == 'exponential':
                        attempt_delay **= factor
                    else:
                        attempt_delay *= factor
        return wrapper
    return decorator


def unsafe(ignored_errors: tuple = None):
    def decorator(fn):
        excetpions_to_ignore = ignored_errors if ignored_errors else (Exception, BaseException)
        def wrapper(*args, **kwargs):
            try:
                ret = fn(*args, **kwargs)
                return ret
            except excetpions_to_ignore:
                pass
        return wrapper
    return decorator
