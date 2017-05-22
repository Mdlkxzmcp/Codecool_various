import asyncio
import time
import random
import aiohttp
import urllib.request

"""Modified version of the code provided at
'hackernoon.com/asyncio-for-the-working-python-developer-5c468e6e2e8e'.
To learn better small changes were made.
The deeper into the code the more identical it is."""


def first_test():

    async def additions():
        print('Running in additions()')
        print('1 + 2 =', 1 + 2)
        await asyncio.sleep(0)
        print('Explicit context switch to additions() again')
        print('84 + 6 =', 90)

    async def subtractions():
        print('Explicit context to subtractions()')
        print('1 - 2 =', 1 - 2)
        await asyncio.sleep(0)
        print('Implicit context switch back to subtractions()')
        print('84 - 6 =', 84 - 6)

    ioloop = asyncio.get_event_loop()
    tasks = [ioloop.create_task(additions()), ioloop.create_task(subtractions())]
    wait_tasks = asyncio.wait(tasks)
    ioloop.run_until_complete(wait_tasks)
    # ioloop.close()


def second_test():
    start = time.time()

    def tic():
        return 'at {:.1f} seconds'.format(time.time() - start)

    async def first_task():
        print('First task started work: {}'.format(tic()))
        await asyncio.sleep(2)
        print('First task ended work: {}'.format(tic()))

    async def second_task():
        print('Second task started work: {}'.format(tic()))
        await asyncio.sleep(2)
        print('Second task ended work: {}'.format(tic()))

    async def third_task():
        print('Third task does stuff while the coroutines are blocked, {}'.format(tic()))
        await asyncio.sleep(1)
        print('Third task is done.')

    ioloop = asyncio.get_event_loop()
    tasks = [
        ioloop.create_task(first_task()),
        ioloop.create_task(second_task()),
        ioloop.create_task(third_task())
    ]
    ioloop.run_until_complete(asyncio.wait(tasks))
    # ioloop.close()


def third_test():

    def task(pid):
        """Synchronous non-deterministic task.
        """
        time.sleep(random.randint(0, 2) * 0.001)
        print('Task {} done'.format(pid))

    def synchronous():
        for i in range(1, 10):
            task(i)

    async def task_coroutine(pid):
        """Coroutine non-deterministic task
        """
        await asyncio.sleep(random.randint(0, 2) * 0.001)
        print('Task {} done'.format(pid))

    async def asynchronous():
        tasks = [asyncio.ensure_future(task_coroutine(i)) for i in range(1, 10)]
        await asyncio.wait(tasks)

    print('Synchronous:')
    synchronous()

    ioloop = asyncio.get_event_loop()
    print('Asynchronous:')
    ioloop.run_until_complete(asynchronous())
    # ioloop.close()


def fourth_test():

    URL = 'https://api.github.com/events'
    MAX_CLIENTS = 3

    def fetch_sync(pid):
        print('Fetch sync process {} started'.format(pid))
        start = time.time()
        response = urllib.request.urlopen(URL)
        datetime = response.getheader('Date')

        print('Process {}: {}, took: {:.2f} seconds'.format(
            pid, datetime, time.time() - start))

        return datetime

    def synchronous():
        start = time.time()
        for i in range(1, MAX_CLIENTS + 1):
            fetch_sync(i)
            print("Process took: {:.2f} seconds".format(time.time() - start))

    async def fetch_async(pid):
        print('Fetch async process {} started'.format(pid))
        start = time.time()
        response = await aiohttp.request('GET', URL)
        datetime = response.headers.get('Date')

        print('Process {}: {}, took: {:.2f} seconds'.format(
            pid, datetime, time.time() - start))

        response.close()
        return datetime

    async def asynchronous():
        start = time.time()
        tasks = [asyncio.ensure_future(
            fetch_async(i)) for i in range(1, MAX_CLIENTS + 1)]
        await asyncio.wait(tasks)
        print("Process took: {:.2f} seconds".format(time.time() - start))

    print('Synchronous:')
    synchronous()

    print('Asynchronous:')
    ioloop = asyncio.get_event_loop()
    ioloop.run_until_complete(asynchronous())
    ioloop.close()


def main():
    print('--First test--')
    first_test()
    print('\n--Second test--')
    second_test()
    print('\n--Third test--')
    third_test()
    print('\n--Fourth test--')
    fourth_test()

if __name__ == '__main__':
    main()
