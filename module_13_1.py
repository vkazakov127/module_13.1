# -*- coding: utf-8 -*-
# module_13_1.py
import time
import asyncio


async def start_strongman(name, power):
    kettlebell_count = 5  # Количество шаров
    print(f'Силач {name} начал соревнования.')
    await asyncio.sleep(0.2)  # Разминка, приветствие зрителям
    for kettlebell in range(kettlebell_count):
        print(f'Силач {name} поднял {kettlebell + 1}-й шар.')
        await asyncio.sleep(400 / power)
    print(f'Силач {name} закончил соревнования.')


async def start_tournament():
    print('Старт')
    task1 = asyncio.create_task(start_strongman("Вася", 50))
    task2 = asyncio.create_task(start_strongman("Федя", 60))
    task3 = asyncio.create_task(start_strongman("Юра", 70))
    await task1
    await task2
    await task3
    print('Финиш')


start = time.time()  # Время начала
asyncio.run(start_tournament())  # Старт соревнования
finish = time.time()  # Время конца
print(f'Working time = {round(finish - start, 2)} seconds')
print('------- The End -------')