#coding:utf-8

#1、使用json.dump()存储一组数据：
import json
numbers=[2,3,5,7,11,13]
filename='numbers.json'
with open(filename,'w') as f:
	json.dump(numbers,f)


#2、使用json.load()将数据读取到内存当中：
with open(filename) as f:
	outs=json.load(f)
print(outs)