import asyncio
import time


async def sleep_coro(duration):
    await asyncio.sleep(duration)


async def main():
    obj1 = sleep_coro(1)
    obj2 = sleep_coro(2)
    obj3 = sleep_coro(3)

    # See that the three object would execute synchronously,
    # so it will take max(1, 2, 3) seconds to execute.
    start = time.time()

    await asyncio.gather(obj1, obj2, obj3)

    time_taken = time.time() - start
    print('Time Taken {0}'.format(time_taken))

asyncio.run(main())
