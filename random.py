from random import randint
import time
a= randint(1,6)
while(a>0 and a<7):
    print(a)
    a= randint(1,6)
    time.sleep(1)