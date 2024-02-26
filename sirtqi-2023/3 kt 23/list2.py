'''b = [5, 4, 'salom', 'biz',True]
print(b[3])
a = 'salom'
print(a[2])
print(b[1:3])
print(b[3:])
print(b[:4])'''
thislist = ["apple", "banana", "cherry"]
thislist[1] = "salom"
print('1- print',thislist)
thislist = ["apple", "banana", "cherry", "orange", "kiwi", "mango"]
thislist[1:3] = ["1", "2",'salom']
print('2- print',thislist)
thislist = ["apple", "banana", "cherry"]
thislist[1:2] = ["1", "22"]
print('3- print',thislist)
thislist = ["apple", "banana", "cherry"]
thislist[1:3] = ["watermelon"]
print('4- print',thislist)
