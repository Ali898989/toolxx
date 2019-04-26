import random
import os
import time
def hh():
 e = str(random.randint(1,3))


 if e in "1":
    os.system("termux-open https://youtu.be/dD8bjB8B0Jw")
 elif e in "2":
    os.system("termux-open https://youtu.be/QJCpdB5MOwE")
 elif e in "3":
    os.system("termux-open https://youtu.be/g05168s3tIw")
 else :
    print "error"
 time.sleep(5)
 hh()

hh()
