import asyncio
import time

# async def greet(name):
#     print("hello")
#     await asyncio.sleep(4)
#     print(name)

# asyncio.run(greet("me"))


# def fun(name):
#     print("hello")
#     time.sleep(4)
#     print(f"{name}")

# fun("shivam")


# async def fun2(task):
#     print("task started")
#     await asyncio.sleep(4)
#     print (f"{task} is completed")

# async def main():
#     await asyncio.gather(
#         fun2("task1"),
#         fun2("task2"),
#         fun2("task3")
#     )

# asyncio.run(main())


async def square(n):
    print(f"square of {n} is")
    await asyncio.sleep(3)
    return n*n

async def main():
    result=await asyncio.gather(
        square(2),
        square(3),
        square(5)
    )
    print(result)

asyncio.run(main())


