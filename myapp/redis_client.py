import redis

client = redis.Redis('localhost','6379',0)


#demo 

client.set('language', 'python')
print(client.get('language'))
