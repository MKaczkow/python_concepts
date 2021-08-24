import time
import multiprocessing


start = time.perf_counter()


def do_something(seconds=2):
    print(f'Sleeping {seconds} second(s)...')
    time.sleep(seconds)
    return f'Done sleeping... {seconds}'


p1 = multiprocessing.Process(target=do_something)
p2 = multiprocessing.Process(target=do_something)

p1.start()
p2.start()

p1.join()
p2.join()

finish = time.perf_counter()

print(f'Finished in {round(finish-start, 2)} second(s)')
