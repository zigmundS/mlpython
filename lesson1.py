# This is a sample Python script.

# Press ⌃R to execute it or replace it with your code.
# Press Double ⇧ to search everywhere for classes, files, tool windows, actions, and settings.


def print_hi(name):
    # Use a breakpoint in the code line below to debug your script.
    print(f'Hi, {name}')  # Press ⌘F8 to toggle the breakpoint.


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    print_hi('PyCharm')

# See PyCharm help at https://www.jetbrains.com/help/pycharm/

name = 'test'
a = f'1312 {name} 23423'
print(a)

b = lambda a: lambda b: a + b
c = b(5)
print(c(3))

d = 7 if b else 9

print(d)

L = [1, 2, 3, 4]
e = list(map(lambda x: x ** 2, L))
print(e)

print(list(filter(lambda x: x % 2 == 0, [1, 3, 2, 5, 20, 21])))


# --------

class Employee:
    def __init__(self, name, age):
        self.name = name
        self.age = age


Alex = Employee('Alex', 20)
Amanda = Employee('Amanda', 30)
David = Employee('David', 15)
L = [Alex, Amanda, David]

L.sort(key=lambda x: x.age)
print([item.name for item in L])

# -------

nums = [n for n in range(1, 6)]
print(nums)

[print(i) for i in range(1, 40, 10)]

print("----------")

x = 'h f g kk llll a'
# if isinstance(x, str):
#     words = x.split()
#     if len(words) > 1:
#         print(len(words))
#         print(sorted(words))

if isinstance(x, str) and len(x.split()) > 1:
    print(len(x.split()), sorted(x.split()))
print('----------- 9')
a = [i for i in range(501) if i % 7 == 0 and '8' in str(i)]
print(a)

print('----------- 8')

x = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
y = x[::-1]
mod = 1 if len(x) % 2 == 0 else 0
z = []
for i, j in enumerate(x):
    z.append(j if i % 2 == 0 else y[i - mod])
print(z)

print('----------- 10')
a = ['ewq', 'qweqe', 'xcvsd', '123', 'qqq']
b = [1, 4, 6, 7, 9]
print([(i, (j, b[i])) for i, j in enumerate(a)])

print('----------- 11')
mas = ['dasd', 'yt', 'werwer wfsdf', 'aaa']
print(dict(zip(mas, [(i, len(j)) for i, j in enumerate(mas)])))

print('----------- 12')
func = lambda *args, **kwargs: sum(args) + sum(kwargs.values())
print(func(1, 2, 3, a=4, b=5))

print('----------- 13')
summ = 0
names = []


def another_func(*args, **kwargs):
    global summ
    summ = sum(args)
    global names
    names = [k for k in kwargs.keys()]


another_func(1, 2, 3, a=4, b=5)

print(f'Cумма {summ}, названия {names}')

print('----------- 14')


class Solution:
    def __init__(self):
        self.sum = 0
        self.names = []

    def another_func(self, *args, **kwargs):
        self.sum = sum(args)
        self.names = [k for k in kwargs.keys()]

    def print_args_kwargs(self):
        print(f'Cумма {self.sum}, названия {self.names}')


class_obj = Solution()
class_obj.another_func(1, 2, 3, a=4, b=5)
class_obj.print_args_kwargs()
