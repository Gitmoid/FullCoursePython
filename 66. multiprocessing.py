from multiprocessing import Process, cpu_count
import time


def counter(num):
    count = 0
    while count < num:
        count += 1


def main():
    start_time = time.perf_counter()

    print(cpu_count())

    a = Process(target=counter, args=(1000000/4,))
    b = Process(target=counter, args=(1000000/4,))
    c = Process(target=counter, args=(1000000/4,))
    d = Process(target=counter, args=(1000000/4,))

    a.start()
    b.start()
    c.start()
    d.start()
    a.join()
    b.join()
    c.join()
    d.join()

    print("finished in:", time.perf_counter() - start_time, "seconds")


if __name__ == '__main__':
    main()
