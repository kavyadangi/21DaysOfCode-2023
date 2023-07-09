n = int(input("Enter the number of numbers you want to enter: "))
list1 = []
for i in range(n):
    num = int(input("Enter the number: "))
    list1.append(num)
print("The largest number from the list is:", max(list1))
