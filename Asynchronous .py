import time
import asyncio
import logging

logging.basicConfig(
        level=logging.INFO,
        format=' %(message)s: %(threadName)10s',
    )

async def get_food(c_id):
   logging.info("Running thread: ")
   print("Customer %s's food is cooking...." % c_id)
   await asyncio.sleep(5)
   print("Customer %s's food is ready" % c_id)


async def make_order(c_id):
   print("Customer %s's food is Ordering...." % c_id)
   await get_food(c_id)


cust = 5
tasks = []

for c in range(cust):
   tasks.append(make_order(c))

print("=======Starting time: " + str(time.ctime()))
loop = asyncio.get_event_loop()
loop.run_until_complete(asyncio.wait(tasks))
loop.close()
print("=======Ending time: " + str(time.ctime()))
