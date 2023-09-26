numbers = [1,2,3,4,5,6,7,8,9,10]
even_number = []
odd_number = []

for i in numbers:
    if i % 2 == 0:
        even_number.append(i)
    else:
        odd_number.append(i)

print("Even_Number : " + str(even_number))
print("Odd Number : " + str(odd_number))
