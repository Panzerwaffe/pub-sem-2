import asyncio
from time import sleep


async def f1():
	print('context to f1')
	await asyncio.sleep(2)
	print('context switch to f1 again')
	return 1

async def f2():
	print('context to f2')
	await asyncio.sleep(1)
	print('context switch back to f2')
	return 2


# async def main():
# 	tasks = [asyncio.create_task(foo()), asyncio.create_task(bar())]
# 	wait_tasks = await asyncio.gather(*tasks)
# 	print(wait_tasks)

async def main():
	# tasks = [f1(), f2()]
	# wait_tasks = await asyncio.gather(*tasks)
	# print(wait_tasks)

	t1 = asyncio.create_task(f1())
	t2 = asyncio.create_task(f2())

	tasks = [t1, t2]
	finished, pending = await asyncio.wait(tasks, return_when=asyncio.FIRST_COMPLETED)
	for task in finished:
		print(task.result(), task.done())

	res = await t1
	print(res)


asyncio.run(main())
