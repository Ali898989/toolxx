import random
import os
import time
def hh():
 e = str(random.randint(1,2))
 print " [*]please wait... "

 if e in "1":
    os.system("termux-open https://www.youtube.com/channel/UCTlvUAypIKJ2BCUaUHKwrxg")
 elif e in "2":

  
    os.system("termux-open https://youtu.be/FeFLgWvWrEw")
   
   
   
 else :
    print "error"
 time.sleep(5)
 hh()

hh()
