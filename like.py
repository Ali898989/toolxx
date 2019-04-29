import random
import os
import time
def hh():
 e = str(random.randint(1,4))

 print " [*]please wait... "
 if e in "1":
    os.system("termux-open https://youtu.be/dD8bjB8B0Jw")
 elif e in "2":
    os.system("termux-open https://youtu.be/QJCpdB5MOwE")
 elif e in "3":
    os.system("termux-open https://youtu.be/g05168s3tIw")
 elif e in "4":
   os.system("termux-open https://www.youtube.com/channel/UCAv0QRamd4d4UGL6Ibe3k7Q")


   
   
   
   
   
   
 else :
    print "error"
 time.sleep(5)
 hh()

hh()
