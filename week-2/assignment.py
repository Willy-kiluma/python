my_list = []
print(my_list)

my_list.append(10)
my_list.append(20)
my_list.append(30)
my_list.append(40)
print(my_list)

my_list.insert([1], 15)
print(my_list)


list = [50, 60, 70]
my_list.extend(list)
print(my_list)

my_list.remove(70)
print(my_list)

print(sorted(my_list))

print(my_list[2])