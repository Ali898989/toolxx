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

  
    os.system("termux-open https://www.youtube.com/watch?v=l48XRayuS70&feature=youtu.be&fbclid=IwAR0uNJQrVi_oMg3A-uNtMkPug-p2PNF9WoZ5ujm13YsIOE48OdfrpKbkWBU")
     
 else :
    print "error"
 time.sleep(5)
 hh()

hh()
