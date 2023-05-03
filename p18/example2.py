# SuperFastPython.com
# пример ожидания завершения всех задач
from random import random
import asyncio


# корутина, которая будет выполняться в новой задаче
async def f1(arg):
	# генерирование случайного значения в диапазоне между 0 и 1
	value = random()
	# блокировка на некоторое время
	await asyncio.sleep(value)
	# вывод значения
	print(f'>task {arg} done with {value}')


# главная корутина
async def main():
	# создание нескольких задач
	tasks = [asyncio.create_task(f1(i)) for i in range(10)]
	# ожидание завершения выполнения всех задач
	done, pending = await asyncio.wait(tasks)
	# done, pending = await asyncio.wait(tasks, return_when=asyncio.FIRST_COMPLETED)
	# вывод результатов
	print('All done', done)

	for task in pending:
		print(task.done())


# запуск asyncio-программы
asyncio.run(main())