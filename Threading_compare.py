import threading
import time

def sleep_coro(duration):
    time.sleep(duration)

def Main():
    t1 = threading.Thread(target=sleep_coro, args=(1,))
    t2 = threading.Thread(target=sleep_coro, args=(2,))
    t3 = threading.Thread(target=sleep_coro, args=(3,))

    
    # To see how threading works as compared to asyncio
    # so it will take 1 + 2 + 3 seconds to execute.
    start = time.time()
    t1.start()
    t2.start()
    t3.start()

    t1.join()       #making sure all three have returned before finding time
    t2.join()
    t3.join()

    time_taken = time.time() - start
    print('Time Taken {0}'.format(time_taken))

if __name__=="__main__":
    Main()