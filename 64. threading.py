import threading
import time


start_time = time.perf_counter()


def eat_breakfast():
    time.sleep(3)
    print("Breakfast")


def drink_coffee():
    time.sleep(4)
    print("Coffee")


def study():
    time.sleep(5)
    print("Study")

# eat_breakfast()   only single thread
# drink_coffee()    is being used
# study()           the functions run in a sequence


x = threading.Thread(target=eat_breakfast, args=())
y = threading.Thread(target=drink_coffee)
z = threading.Thread(target=study)

x.start()  # parallel
y.start()
z.start()

print(threading.active_count())
print(threading.enumerate())
print(time.perf_counter() - start_time)

x.join()  # sequence
y.join()
z.join()

print(threading.active_count())
print(threading.enumerate())
print(time.perf_counter() - start_time)
