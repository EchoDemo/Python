#coding:utf-8

#1、在列表中存储字典：
alien0={'color':'green','points':5}
alien1={'color':'yellow','points':10}
alien2={'color':'red','points':15}

aliens=[alien0,alien1,alien2]
for alien in aliens:
	print(alien)


#2、在字典中存储列表：
favorite_language={
	'jen':['python','ruby'],
	'sarah':['c','java'],
	'edward':['ruby','html','css'],
	'phil':['python','c#']
}
for name,languages in favorite_language.items():
	print("\n"+name.title()+"'s favorite languages are:")
	for language in languages:
		print(language.title())


#3、在字典中存储字典：
users={
	'aeinstein':{
	    'first':'albert',
	    'last':'einstein',
	    'location':'princeton',
	},

	'mcurie':{
	    'first':'marie',
	    'last':'curie',
	    'location':'paris',
	},
}
for username,userinfo in users.items():
	print("\nUsername:"+username)
	full_name=userinfo['first']+" "+userinfo['last']
	location=userinfo['location']

	print("\tFull name:"+full_name.title())
	print("\tLocation:"+location.title())
