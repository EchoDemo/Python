#coding:utf-8

#1、Python位list提供了切片（Slice）操作符L[0:3]表示，从索引0开始取，直到索引3为止，但不包括索引3。即索引0，1，2，
#正好是3个元素。如果第一个索引是0，还可以省略：L[:3] 也可以从索引1开始，取出2个元素出来：L[1:3] 只用一个 : 
#表示从头到尾。因此，L[:]实际上复制出了一个新list。切片操作还可以指定第三个参数：L[::2]第三个参数表示每N个取一个，
#上面的 L[::2] 会每两个元素取出一个来，也就是隔一个取一个。把list换成tuple，切片操作完全相同，只是切片的结果也变成了tuple。
L=range(1,101) #创建一个数列：[1,2,...,100]
print L[:10] #输出前10个数
print L[2::3] #输出3的倍数
print L[4:50:5] #从5开始，每隔4个取一个，且小于等于50


#2、对于list，既然Python支持L[-1]取倒数第一个元素，那么它同样支持倒数切片，
L = ['Adam', 'Lisa', 'Bart', 'Paul']
print L[-2:]
print L[:-2]
print L[-3:-1]
print L[-4:-1:2]
#记住倒数第一个元素的索引是-1。倒序切片包含起始索引，不包含结束索引。


#3、字符串 'xxx'和 Unicode字符串 u'xxx'也可以看成是一种list，每个元素就是一个字符。因此，字符串也可以用切片操作，
#只是操作结果仍是字符串
def firstCharUpper(s):
	return s[:1].upper()+s[1:]
print firstCharUpper('hello')
print firstCharUpper('sunday')
print firstCharUpper('september')


#4、复制列表：
L = ['Adam', 'Lisa', 'Bart', 'Paul']
M=L[:] #创建了一个副本给M，此后它们便没有关联。
N=L #这是让两个变量都同时指向同一个列表，无论谁发生变化，列表都将发生变化。
