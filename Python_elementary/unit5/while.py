#coding:utf-8


#使用while循环来处理列表和字典：要在遍历列表是对其进行修改，尽量使用while循环。
unconfirmed_users=['alice','brian','candance']
confirmed_users=[]
while unconfirmed_users:
	current_user=unconfirmed_users.pop()
	print("Verifying user:"+current_user.title())
	confirmed_users.append(current_user)

print("\nThe following users have been confirmed:")
for confirmed_user in confirmed_users:
	print(confirmed_user)


#2、删除包含特定值的所有列表元素：
pets=['dog','cat','dog','goldfish','cat','rabbit','cat']
print(pets)

while 'cat' in pets:
	pets.remove('cat')
print(pets)


/3、使用用户数据来填充字典：
responses={}
flag=True #这样定义的True或False首字母需要大写

while flag:
	name=raw_input("\nWhat is your name?\n")
	response=raw_input("Which mountain would you like to climb someday?\n")
	responses[name]=response
	repeat=raw_input("Do you want let another person respond?\n(yes/no)")
	if repeat=='no': flag=False
print("\n---Poll Result---")
for name,response in responses.items():
	print(name+"would like to climb "+response)
