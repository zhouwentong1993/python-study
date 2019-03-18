import random

random_number = random.randrange(100)
if random_number % 2 == 0:
    print(random_number, "is even")
else:
    print(random_number, "is odd")

for i in range(10):
    if i % 2 != 0:
        print(i)

# Python 的语法挺硬啊，if else 之间还可以插入代码的，牛逼 ……
for n in range(2, 100):
    if n == 2:
        print(n)
        continue
    for i in range(2, int(n ** 0.5) + 1):  #为什么要 +1 以后再说…… n 的 1/2 次方，相当于根号 n。
        if (n % i) == 0:
            break
    else:
        print(n)

a = abs(-0.2123)
print(a)
