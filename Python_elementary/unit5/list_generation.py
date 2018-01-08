#coding:utf-8

#L=[]
#for x in range(1,11):
#    L.append(x*x)
#print L #打印出[1,4,9,...,100]
print [x*x for x in range(1,11)] #列表生成式
#range(1, 100, 2) 可以生成list [1, 3, 5, 7, 9,...]


#2、复杂表达式
d = { 'Adam': 95, 'Lisa': 85, 'Bart': 59 }
tds = ['<tr><td>%s</td><td>%s</td></tr>' % (name, score) for name, score in d.iteritems()]
print '<table>'
print '<tr><th>Name</th><th>Score</th><tr>'
print '\n'.join(tds)
print '</table>'
#字符串可以通过%进行格式化，用指定的参数替代%s。字符串的join()方法可以把一个list拼接成一个字符串。
#把打印出来的结果保存为一个html文件，就可以在浏览器中看到效果了
#<table border="1">
#<tr><th>Name</th><th>Score</th><tr>
#<tr><td>Lisa</td><td>85</td></tr>
#<tr><td>Adam</td><td>95</td></tr>
#<tr><td>Bart</td><td>59</td></tr>
#</table>


#3、列表生成式的for循环后面还可以加上if判断。例：[x * x for x in range(1, 11) if x % 2 == 0]只有 if 判断为 True 的时候
#才把循环的当前元素添加到列表中。
def toUppers(L):
	return [x.upper() for x in L if isinstance(x,str)]
print toUppers(['Hello','World'])


#4、for循环可以嵌套，因此，在列表生成式中，也可以用多层for循环来生成列表。对于字符串'ABC'和'123'，可以使用两层循环，生成全排列：
#print [m + n for m in 'ABC' for n in '123']
#['A1', 'A2', 'A3', 'B1', 'B2', 'B3', 'C1', 'C2', 'C3']
print [x*100+y*10+z for x in range(1,10) for y in range(0,10) for z in range(0,10) if x==z]

