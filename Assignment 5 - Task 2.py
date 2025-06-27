list1 = []
for i in range(1,11):
    list1.append(i)
print('Original list: ',list1)
a = list1[0:5]
print('Extracted first five elements: ',a)
a.reverse()
print('Reversed extracted elements: ',a)