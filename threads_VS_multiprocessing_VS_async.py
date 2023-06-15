## timing
import time

def time_of_function(function):
    def wrapped(*args):
        start_time = time.time()
        res = function(*args)
        print('время выполнения '+str(time.time() - start_time))
        return res
    return wrapped

########

## threads
import threading

def Count_smth(int_c):
	#print('start f-'+str(int_c))
	i=0
	while i<10**int_c:
		i+=1
	#print('end f-'+str(int_c)+' '+str(i))
    
#@time_of_function
def main_threads():
	t1 = threading.Thread(target=Count_smth, args=(6,), daemon=True)
	t2 = threading.Thread(target=Count_smth, args=(3,), daemon=True)
	t3 = threading.Thread(target=Count_smth, args=(4,), daemon=True)
	t1.start()
	t2.start()
	t3.start()
	t1.join()
	t2.join()
	t3.join()

########

import asyncio


async def Count_smth_1(int_c):
	#print('start f-'+str(int_c))
	i=0
	while i<10**int_c:
		i+=1
		await asyncio.sleep(0)
	#print('end f-'+str(int_c)+' '+str(i))

async def main_asyncio():
	task_1=asyncio.create_task(Count_smth_1(6))
	task_2=asyncio.create_task(Count_smth_1(3))
	task_3=asyncio.create_task(Count_smth_1(4))
	
	await task_1
	await task_2
	await task_3

########
from multiprocessing import Process
def main_processing():
	p1 = Process(target=Count_smth, args=(6,), daemon=True)
	p2 = Process(target=Count_smth, args=(3,), daemon=True)
	p3 = Process(target=Count_smth, args=(4,), daemon=True)
	p1.start()
	p2.start()
	p3.start()
	p1.join()
	p2.join()
	p3.join()

######## MANY
def main_threads_many(c_c):
	mas=[]
	for i in range(c_c): 
		mas.append(threading.Thread(target=Count_smth, args=(6,), daemon=True))
	for i in mas: 
		i.start()
	for i in mas: 
		i.join()

async def main_asyncio_many(c_c):
	mas=[]
	for i in range(c_c): 
		mas.append(asyncio.create_task(Count_smth_1(6)))
	for i in mas: 
		await i
		
def main_processing_many(c_c):
	mas=[]
	for i in range(c_c): 
		mas.append(Process(target=Count_smth, args=(6,), daemon=True))
	for i in mas:
		i.start()
	for i in mas: 
		i.join()
#####

if __name__ == '__main__':
	print('Потоки')
	start_time = time.time()
	fomain_threads()
	print('время выполнения '+str(time.time() - start_time))
	print('-----')
	print('Asyncio')
	start_time = time.time()
	asyncio.run(main_asyncio())
	print('время выполнения '+str(time.time() - start_time))
	print('-----')
	print('Процессы')
	start_time = time.time()
	main_processing()
	print('время выполнения '+str(time.time() - start_time))
	
	############# Потоки 1000 шт
	start_time = time.time()
	main_threads_many(1000)
	print('время выполнения '+str(time.time() - start_time))
	############# Асинхронные функции 10 шт
	start_time = time.time()
	asyncio.run(main_asyncio_many(10))
	print('время выполнения '+str(time.time() - start_time))
	############ Процессы 10 шт
	start_time = time.time()
	main_processing_many(10)
	print('время выполнения '+str(time.time() - start_time))
	
	
	
