import time
import datetime

# def multiplication(x, y, z):
#     return round(x * y * z)
#
#
# print('Result:', multiplication(1, 2.575, 3.5))

for i in range(10):
    now = datetime.datetime.now()
    my_name = now.strftime('Report_%H%M%S.txt')
    print('My name:', my_name)
    time.sleep(2)
