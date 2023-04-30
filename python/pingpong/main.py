from threading import Thread, Lock
import time

value = 'ping'

def ping(lock):
    global value

    while True:
        time.sleep(1)
        if lock.acquire(blocking = False):
            if value == 'ping':
                print(value)
                value = 'pong'
            
            lock.release()

def pong(lock):
    global value

    while True:
        time.sleep(1)
        if lock.acquire(blocking = False):
            if value == 'pong':
                print(value)
                value = 'ping'
            
            lock.release()

if __name__ == "__main__":
    mutex = Lock()

    ping_thread = Thread(target=ping, args=[mutex])
    pong_thread = Thread(target=pong, args=[mutex])

    ping_thread.start()
    pong_thread.start()


