#coding:utf-8

#1、dict 表示“名字”-“成绩”的查找表如下：
d = {
    'Adam': 95,
    'Lisa': 85,
    'Bart': 59
}
#我们把名字称为key，对应的成绩称为value，dict就是通过 key 来查找 value。
#花括号 {} 表示这是一个dict，然后按照 key: value, 写出来即可。最后一个 key: value 的逗号可以省略。
#由于dict也是集合，len() 函数可以计算任意集合的大小。

#2、使用 d[key] 的形式来查找对应的 value，这和 list 很像，不同之处是，list 必须使用索引返回对应的元素，而dict
#使用key。通过 key 访问 dict 的value，只要 key 存在，dict就返回对应的value。如果key不存在，会直接报错：KeyError。
#要避免 KeyError 发生，有两个办法：

#一是先判断一下 key 是否存在，用 in 操作符：
#if 'Paul' in d:
    #print d['Paul']
#如果 'Paul' 不存在，if语句判断为False，自然不会执行 print d['Paul'] ，从而避免了错误。

#二是使用dict本身提供的一个 get 方法，在Key不存在的时候，返回None：
#print d.get('Bart')
#59
#print d.get('Paul')
#None
print 'Adam:',d['Adam']
print 'Lisa:',d.get('Lisa')
if 'Bart' in d:
    print 'Bart:',d['Bart']


#3、dict的第一个特点是查找速度快，无论dict有10个元素还是10万个元素，查找速度都一样。而list的查找速度随着元素
#增加而逐渐下降。不过dict的查找速度快不是没有代价的，dict的缺点是占用内存大，还会浪费很多内容，list正好相反，
#占用内存小，但是查找速度慢。由于dict是按 key 查找，所以，在一个dict中，key不能重复。

#dict的第二个特点就是存储的key-value序对是没有顺序的！这和list不一样。因此打印的顺序不一定是我们创建时的顺序，
#而且，不同的机器打印的顺序都可能不同，这说明dict内部是无序的，不能用dict存储有序的集合。

#dict的第三个特点是作为 key 的元素必须不可变，Python的基本类型如字符串、整数、浮点数都是不可变的，都可以作为
# key。但是list是可变的，就不能作为 key。
e={
    '123': [1, 2, 3],  # key 是 str，value是list
    123: '123',  # key 是 int，value 是 str
    ('a', 'b'): True  # key 是 tuple，并且tuple的每个元素都是不可变对象，value是 boolean
}


#4、更新dict
d['Paul'] = 72 #把新同学'Paul'的成绩 72 加进去
d['Bart'] = 60 #如果 key 已经存在，则赋值会用新的 value 替换掉原来的 value
print d


#5、遍历dict
for key in d:
	print key,':',d[key]
