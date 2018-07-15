import time
from threading import Thread
import threading
def get_food(c_id):
   print("Customer %s's food is cooking...." % c_id)
   time.sleep(5)
   print("Customer %s's food is ready" % c_id)
   print("=======Ending time: " + str(time.ctime()))

def make_order(c_id):
   print("Running Thread: " + str(threading.current_thread().name))
   print("Customer %s's food is Ordering...." % c_id)
   get_food(c_id)

cust = 5
threads = []
print("=======Starting time: " + str(time.ctime()))
for c in range(cust):
   thread = Thread(target=make_order, args=(c,))
   thread.start()
for t in threads:
   t.join()
