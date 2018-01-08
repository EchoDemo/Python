#coding:utf-8

#1、Python中，迭代永远是取出元素本身，而非元素的索引。对于有序集合，元素确实是有索引的。有的时候，我们可以
#使用 enumerate() 函数在 for 循环中拿到索引。实际上，enumerate() 函数把：['Adam', 'Lisa', 'Bart', 'Paul']
#变成了类似：[(0, 'Adam'), (1, 'Lisa'), (2, 'Bart'), (3, 'Paul')]因此，迭代的每一个元素实际上是一个tuple。
L = ['Adam', 'Lisa', 'Bart', 'Paul']
for index, name in enumerate(L):
    print index, '-', name

#for t in enumerate(L):
#    index = t[0]
#    name = t[1]
#    print index, '-', name


#2、dict 对象有一个 values() 方法，这个方法把dict转换成一个包含所有value的list，这样，我们迭代的就是 dict的每一个 value：
#d = { 'Adam': 95, 'Lisa': 85, 'Bart': 59 }
#print d.values()
#[85, 95, 59]
#dict除了values()方法外，还有一个itervalues()方法，用 itervalues()方法替代values()方法，迭代效果完全一样。
# itervalues()不同于values()，它会在迭代过程中依次从dict中取出value，所以itervalues()比values()节省了生成 list 所需的内存。
#在Python中，for循环可作用的迭代对象远不止 list，tuple，str，unicode，dict等，任何可迭代对象都可以作用于for循环。
d = { 'Adam': 95, 'Lisa': 85, 'Bart': 59, 'Paul': 74 }
sum=0.0
for x in d.values():
	sum=sum+x
print sum/len(d)


#3、items()方法把dict对象转换成了包含tuple的list，我们对这个list进行迭代，可以同时获得key和value。
#items() 也有一个对应的 iteritems()，iteritems() 不把dict转换成list，而是在迭代过程中不断给出 tuple，
#所以，iteritems()不占用额外的内存。
for k,v in d.items():
	sum=sum+v
	print k,':',v
print 'average',':',sum/len(d)
