import asyncio
n = int(input("Input count of orders: "))
dct = {}
for _ in range(n):
    order = input("Input dish: ")
    time_to = int(input("Input cooking time: "))
    dct[order] = time_to

async def wait():
    tasks = []
    for order, time_to in dct.items():
        task = asyncio.create_task(queue(order, time_to))
        tasks.append(task)
    await asyncio.gather(*tasks)



async def queue(order, time_to):
    print("New order: ",order)
    await asyncio.sleep(time_to)
    print(order + " is ready!")

asyncio.run(wait())