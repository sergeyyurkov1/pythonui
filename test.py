import time

import psutil

for i in range(30):
    print([psutil.virtual_memory().percent])
    time.sleep(1)
