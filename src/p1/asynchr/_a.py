class UnauthorizedError(RuntimeError):
    pass
try:
    raise UnauthorizedError(':(')
except UnauthorizedError as e:
    print(str(e))