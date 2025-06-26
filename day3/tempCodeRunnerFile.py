a,b,c = 0

try:
    result = a,b,c/0
    print(result)
except ZeroDivisionError:
    print("Cannot divide by Zero")
except ValueError:
    print("Invalid value")
except TypeError:
    print("Type Error")
except Exception as e:
    print(e) 