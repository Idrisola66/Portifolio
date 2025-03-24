my_list = [1,2,3,4,5,7,6,]
print(my_list)
my_list.append(9)
print(my_list)
my_list.extend([8,10])
print(my_list)
my_list.insert(4,5)
print(my_list)
my_list.remove(7)
print(my_list)
my_list.pop(7)
print(my_list)
index = my_list[7]
print(index)
count = my_list.count(5)
print(count)
my_list.sort()
print(my_list)
my_list.reverse()
print(my_list)

new_list = my_list.copy()
print(my_list)

# my_list.clear()
print(my_list)
length = len(new_list)
print(new_list)

minimum = min(new_list)
maximum = max(new_list)
print(minimum, maximum)

adjustment = new_list + [20,30,40,50,60]
print(adjustment)

multiply = new_list * 2
print(multiply)

present = 40 in adjustment
absent = 60 not in adjustment
print(present, absent)
length1 = len(adjustment)
print(length1)

slicing = adjustment[2:-1:2]
print(slicing)

del adjustment [1]
print(adjustment)