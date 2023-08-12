import time
import threading

start = time.perf_counter()

def doingWork(seconds):
    print(f"Sleeping for {seconds} secs")
    time.sleep(seconds)
    print("Done Sleeping...")


threads = []

for i in range(10):
    t = threading.Thread(target=doingWork, args = [1.5])
    t.start()
    threads.append(t)

for thread in threads:
    thread.join()


finish = time.perf_counter()

print(f"Finished in {round(finish-start, 2)} second(s).")





#! Normal Method of execution
# doingWork()
# doingWork()

#! Execution using threading
# t1 = threading.Thread(target=doingWork)
# t2 = threading.Thread(target=doingWork)

# t1.start()
# t2.start()

# t2.join()
# t2.join()