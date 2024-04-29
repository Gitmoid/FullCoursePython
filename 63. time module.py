import time


print(time.ctime(1000000))  # 0 = epoch (when time began for PC, 1970). 1000 = 1000 seconds after epoch, converts to format

print(time.time())  # time passed since epoch

print(time.ctime(time.time()))  # current date and time in a readable format

time_object = time.localtime()  # keyword arguments of year, month, day, hour, min...
print(time_object)
local_time = time.strftime('%B %d %Y %H:%M:%S', time_object)
print(local_time)

time_string = "20 April, 2020"
time_object1 = time.strptime(time_string, '%d %B, %Y')
print(time_object1)

time_tuple = (2020, 4, 20, 4, 20, 0, 0, 0, 0)
time_string1 = time.asctime(time_tuple)
print(time_string1)

time_since_epoch = time.mktime(time_tuple)
print(time_since_epoch)
