import threading
import time


def timer():
    print()
    count = 0
    while True:
        time.sleep(1)
        count += 1
        print("logged in for: ", count, " seconds")


# x = threading.Thread(target=timer)    this thread runs in the background, the program is waiting for it to complete the task
# x.start()                             before exiting, they cannot normally be killed and stay alive until task is complete

x = threading.Thread(target=timer, daemon=True)
x.start()

# x.daemon = True can change the thread to (non-)daemon before it is run, not during the run
print(x.daemon)  # is the function daemon?

answer = input("Do you wish to exit?: ")
