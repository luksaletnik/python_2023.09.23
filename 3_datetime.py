import datetime

now = datetime.datetime.now()
print(now)
print(type(now))

_time = now.strftime('Date: %d-%m-%y\nTime: %H:%M:%S')
print(_time)

my_name = now.strftime('File_%H%M%S.txt')
print('My name:', my_name)
