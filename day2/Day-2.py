#using Map() calculate lenght of each string in list

li = ["hello", 'i', "am"]
print(list(map(len, li)))

#add to list by map()

l1 = ["hello", 'i', "am"]
l2 = ["hello", 'i', "am"]
print(list(map(lambda x, y: x + y, l1, l2)))

#Even and Odd numbers
n = [1,2,34,-43,21,-3, -45]
print(list(filter(lambda x: x % 2 == 0,n)))


#Print all positive numbers
print(list(filter(lambda x: x > 0, n)))


li = ['a', 23, -43, "hi"]
print(list(filter(lambda x: isinstance(x, (int)), li)))

#sorted() sort a list of tuples by second element

d = [("abc", 90), ("xyz", 80)]
print(sorted(d, key=lambda x : x[1]))

#sorting dictionaries values

s=[{"name": "Aaditi", "age": 21},
    {"name": "Ishwari", "age": 23}]
print(sorted(s, key=lambda s: s['age']))


##############################################
#reduce function

from functools import reduce
num = [3,45,5,23]
max_value = reduce(lambda x,y: x if x > y else y , num )
print(max_value)

#any and All methods
#returns boolean

nl = [12, 3, -4, 5, -7]
print(any(map(lambda x : x < 0 , nl)))

#exercise

students = [("aswhini", 20, 98, "kopergaon"), 
            ("Rameshwar", 19, 97, "shirdi"), 
            ("aditya", 18, 91, "kopergaon"), 
            ("rohit", 19, 88, "Pune")]

#collect only names
#collect names if marks are more than 90
#highest marks
#Youngest
#How many belongs to "kopergaon"
#list of names not from kopergaon

topper = filter(map(lambda x : max(x[2]) for x in students))
print(topper)

x = int(input())
while(x != 0):
    print(
        "Enter choice : \n"
        "1: Show Names \n"
        "2: Names of marks above 90 \n"
        "3: Show Topper \n"
        "4: Names from kopergaon \n"
        "5: Name NOT from Kopergaon \n"
        "0: Quit \n"
    )

    if x == 1:
        # Show Names
        print([student[0] for student in students])
    elif x == 2:
        # Names of marks above 90
        print([student[0] for student in students if student[2] > 90])
    elif x == 3:
        # Show Topper
        topper = filter(map(lambda x : max(x[2]) for x in students))
        print(topper)
    elif x == 4:
        # Names from kopergaon
        print([student[0] for student in students if student[3].lower() == "kopergaon"])
    elif x == 5:
        # Name NOT from Kopergaon
        print([student[0] for student in students if student[3].lower() != "kopergaon"])
    elif x == 0:
        print("Quitting...")
        break
    else:
        print("Invalid choice")


################################################################

#heapq
# get a heap of value 3
import heapq

L = [232,43,55,211,555]
print(heapq.nlargest(3, L))

#groupby

from itertools import groupby

data = [5,1,1,4,4,3,4,2,1,5,3,6]

groups = [list(group) for key, group in groupby(data, key=lambda x: x)]
print(groups)

#convert loop in list

lst = []
for i in range(9):
    lst.append(i)
print(lst)

print([i**3 for i in range(9)])


