import random
import os
import time
def hh():
 e = str(random.randint(1,1))
 print " [*]please wait... "

 if e in "1":
    os.system("termux-open https://www.youtube.com/channel/UCTlvUAypIKJ2BCUaUHKwrxg")
 else :
    print "error"
 time.sleep(5)
 hh()

hh()
