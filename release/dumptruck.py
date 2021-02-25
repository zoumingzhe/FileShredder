import time
import threading
from ztools import tprint
from collections import namedtuple
from concurrent.futures import ThreadPoolExecutor

def test(value1, value2=None):
    tprint.std("%s threading is printed %s, %s"%(threading.current_thread().name, value1, value2))
    time.sleep(2)
    return True

threads = []
thdclass = namedtuple('thread', 'tno future')
thdpool = ThreadPoolExecutor(max_workers=4, thread_name_prefix="THD")
for i in range(0,10):
    future = thdpool.submit(test,i,i+1)
    tclass = thdclass(i,future)
    threads.append(tclass)
for t in threads:
    tprint.std(t.tno,t.future.result())
thdpool.shutdown(wait=True)
print('main finished')

input("按回车（Enter）继续")
