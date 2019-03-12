
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


