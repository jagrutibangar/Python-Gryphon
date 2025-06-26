num = int("hello")

try:
    result = 10/num
    print(result)
except ZeroDivisionError:
    print("Cannot divide by Zero")
except ValueError:
    print("Invalid value")
except TypeError:
    print("Type Error")
except Exception as e:
    print(e) 



li = ["Hello", 89]

try:
    print(li[9])
except IndexError:
    print("Index out of range")