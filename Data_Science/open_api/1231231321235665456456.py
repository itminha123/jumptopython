import threading
import time
aaaa = False

def doit(arg):
    t = threading.currentThread()
    while getattr(t, "do_run", True):
        print("working on %s" % arg)
        time.sleep(1)
        print("Stopping as you wish.")

# def main():
t = threading.Thread(target=doit, args=("task",))
t.start()
# time.sleep(10)
if aaaa == False:
    t.do_run = False
else:
    t.start()
    # t.join()
# if __name__ == "__main__":
#     main()

while True:
    bb =input('1.2.')
    if bb == '1':
        aaaa = True
    if bb == '2':
        aaaa = False
