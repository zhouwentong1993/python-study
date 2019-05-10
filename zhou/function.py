# 函数参数可以设置默认值，挺牛逼的
def func1(param1, param2=123, param3='abc'):
    print(param1, param2, param3)


func1(1)


# L 的默认值只初始化一次。
def func2(a, L=[]):
    L.append(a)
    print(L)


func2(1)
func2(2)
func2(3)


# 这样就行了
def func3(a, L=None):
    if L == None:
        L = []
    L.append(a)
    print(L)


func3(1)
func3(2)
func3(3)


def func4(param1, param2='string', param3=123, param4=4):
    print(param1, param2, param3, param4, end=" ")


# 关键字参数，如果有多个可变参数，匹配规则是按照传入参数顺序匹配的，如果想要跳着匹配，可以采用这种手动指定的方式
# 注意，不能重复地指定参数。
func4(123, 'aaa', param3=321)

# 「*」代表列表类型，「**」,问题：
def func5(type, *arguments, **keywords):
    print(type)
    for key in arguments:
        print(key)

    for keyword in keywords:
        print(keyword, ":", keywords[keyword])


func5("123", "1", "2", '3', '4', jack="杰克", luck='赖')
