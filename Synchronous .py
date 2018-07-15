import time

def get_food(c_id):
   print("Customer %s's food is cooking...." % c_id)
   time.sleep(5)
   print("Customer %s's food is ready" % c_id)


def make_order(c_id):
   print("Customer %s's food is Ordering...." % c_id)
   get_food(c_id)


cust = 5

print("=====Starting time: " + str(time.ctime()))
for c in range(cust):
   make_order(c)

print("=====Ending time: " + str(time.ctime()))
