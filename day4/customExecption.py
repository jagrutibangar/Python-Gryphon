class MyError(Exception):
    pass

try:
    raise MyError("Some custom went wrong!")
except MyError as e:
    print("Error caught:" , e)


