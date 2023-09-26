# list1 = [23,54,24,23,54,67,87,24]
# print(list(set(list1)))

a = [10,20,30,40,10,50,20,50,30]
dup_items = set()
uniq_items = []
for x in a:
    if x not in dup_items:
        uniq_items.append(x)
        dup_items.add(x)
print(dup_items)