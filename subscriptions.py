import random
import os
import time
def hh():
 e = str(random.randint(1,4))
 print " [*]please wait... "

 if e in "1":
    os.system("termux-open https://www.youtube.com/channel/UCTlvUAypIKJ2BCUaUHKwrxg")
 elif e in "2":

  
    os.system("termux-open https://youtu.be/FeFLgWvWrEw")
   
 elif e in "3":

    os.system("termux-open https://www.youtube.com/channel/UCxN7bGIwvi3eT5jxW1VqFHw")
 
 elif e in "4":

  
    os.system("termux-open https://www.youtube.com/channel/UCzdVh7wEiDGqIdv1f5sQfiA")
     
 else :
    print "error"
 time.sleep(5)
 hh()

hh()
