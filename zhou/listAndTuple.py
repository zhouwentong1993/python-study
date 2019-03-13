# 假设 list 中共有 n 个元素，那可访问的下标为 [0,n-1][-1,-n]，如果超出限制，会报错。
classmate = ["s1", "s2", "s3"]
print(classmate[-3])

# append 是从尾部添加的
classmate.append("s4")
print(classmate)

# pop 也是从尾部弹出的
classmate.pop()
print(classmate)

classmate.pop(-1)
print(classmate)

students = ("a", "b", "c", "d")
print(students.count("a"))

if 5 < 6 < 7:
    print("yes")

list1 = [1, 2, 3, 4, 5, 6]
list2 = [7, 8, 9, 10, 1, 2]
# python 支持加操作，不支持减操作
list3 = list1 + list2
print(list3)

for i in range(4, 10):
    print(i, end=" ")

s1 = "abcdefg"
for ch in s1:
    print(ch, end=" ")

# 元组也可以用这种方法实现
tuple1 = 1, 2, 3, 4, 65
print(tuple1)
