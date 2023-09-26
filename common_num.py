list1 = [1,2,3,4,5]
list2 = [6,7,8,5,10]

result = False

for  i in list1:
    for j in list2:
        if i == j:
            result = True
            print(result)

if result:
    print("List have at least one common member")
else:
    print("List do not have any common members")
