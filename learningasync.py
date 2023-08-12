import time
import asyncio

async def func1():
    print("...")
    time.sleep(3)
    print("Func 1 Completed.")


async def func2():
    print("...")
    time.sleep(3)
    print("Func 2 Completed.")


async def func3():
    print("...")
    time.sleep(3)
    print("Func 3 Completed. ")

async def main():
    await func1()
    await func2()
    await func3()


asyncio.run(main())