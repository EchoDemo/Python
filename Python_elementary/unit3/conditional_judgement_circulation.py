#coding:utf-8

#1、Python代码的缩进规则。具有相同缩进的代码被视为代码块，上面的3，4行 print 语句就构成一个代码块
#（但不包括第5行的print）。如果 if 语句判断为 True，就会执行这个代码块。缩进请严格按照Python的习惯写法：
#4个空格，不要使用Tab，更不要混合Tab和空格，否则很容易造成因为缩进引起的语法错误。
# if 语句后接表达式，然后用:表示代码块开始。
age = 20
if age >= 18:
    print 'your age is', age
    print 'adult'
print 'END'


#2、if-else
if age >= 18:
    print 'adult'
else:
    print 'teenager'


#3、if ... 多个elif ... else ... 结构
if age >= 18:
    print 'adult'
elif age >= 6:
    print 'teenager'
elif age >= 3:
    print 'kid'
else:
    print 'baby'


#4、 for循环依次把list或tuple的每个元素遍历出来
Q = ['Adam', 'Lisa', 'Bart']
for name in Q:
    print name
#name这个变量是在for循环中定义的，意思是：依次取出list中的每一个元素，并把元素赋值给 name，然后执行for
#循环体（就是缩进的代码块）。


#5、while循环：从 0 开始打印不大于 N 的整数
N = 10
x1 = 0
while x1 < N:
    print x1
    x1 = x1 + 1


#6、break
sum = 0
x2 = 1
while True:
    sum = sum + x2
    x2 = x2 + 1
    if x2 > 100:
        break
print sum


#7、continue：统计及格分数的平均分
L = [75, 98, 59, 81, 66, 43, 69, 85]
sum = 0.0
n = 0
for x in L:
    if x < 60:
        continue
    sum = sum + x
    n = n + 1
print sum/n


#8、多重循环：
for x in ['A', 'B', 'C']:
    for y in ['1', '2', '3']:
        print x + y
