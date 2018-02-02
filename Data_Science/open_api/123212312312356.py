import threading
import time
import ctypes

g_Balcony_Windows = False
g_AI_Mode = False


def terminate_thread(thread):
    """Terminates a python thread from another thread.

    :param thread: a threading.Thread instance
    """
    if not thread.isAlive():
        return

    exc = ctypes.py_object(SystemExit)
    res = ctypes.pythonapi.PyThreadState_SetAsyncExc(
        ctypes.c_long(thread.ident), exc)
    if res == 0:
        raise ValueError("nonexistent thread id")
    elif res > 1:
        # """if it returns a number greater than one, you're in trouble,
        # and you should call it again with exc=NULL to revert the effect"""
        ctypes.pythonapi.PyThreadState_SetAsyncExc(thread.ident, None)
        raise SystemError("PyThreadState_SetAsyncExc failed")



def update_scheduler():
    global g_Balcony_Windows
    debug_index = 0
    while True:
        if g_AI_Mode == True:
            if time.strftime("%S") == '05':
                print('ee')
                time.sleep(1)
                g_Balcony_Windows = not g_Balcony_Windows
        print("Thread 동작중 %d" % debug_index)
        time.sleep(1)
        debug_index = debug_index+1



def my_thread_terminate():
    while t.is_alive():
        try:
            terminate_thread(t)
        except:
            pass

while True:
    print("메뉴를 선택하세요")
    print("1. 장비 상태 조회")
    print("2. 인공지능 모드 변경")
    print("3. 종료")

    menu_num = int(input("메뉴 입력: "))
    if(menu_num==1):
        print("발코니(베란다) 창문: ",end='')
        if g_Balcony_Windows==True: print("열림")
        else: print("닫힘")
    elif(menu_num==2):
        print("인공지능 모드: ", end='')
        g_AI_Mode = not g_AI_Mode
        if g_AI_Mode==True: print("작동")
        else: print("정지")
        if g_AI_Mode == True:
            print('cc')
            t = threading.Thread(target=update_scheduler)
            t.daemon = True
            t.start()
            # update_scheduler()
        else:
            my_thread_terminate()

    else: break




# def print_hello():
#     debug_index = 0
#     while True:
#         print("Thread 동작중 %d" %debug_index )
#         time.sleep(1)
#         debug_index = debug_index+1
#
# t =  threading.Thread(target=print_hello)
# t.daemon = True
# t.start()


# terminate_thread(t)
# while True:
#     input()
#     my_thread_terminate()
#     if not t.is_alive():
#         print("Thread가 종료되었습니다.")
#         input("Main 프로그램을 종료하시겠습니까? (아무값이나 입력하세요)")
#         break
    # else:
    #     print("Thread 미종료")