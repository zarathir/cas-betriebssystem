from threading import Thread, Lock
import time

value = 'ping'

def ping(lock):
    global value

    while True:
        if not lock.locked():
            lock.acquire()
            if value == 'ping':
                print(value)
                value = 'pong'
                lock.release()
            
            time.sleep(1)

def pong(lock):
    global value

    while True:
        if not lock.locked():
            lock.acquire()
            if value == 'pong':
                print(value)
                value = 'ping'
                lock.release()
            
            time.sleep(1)

if __name__ == "__main__":
    mutex = Lock()

    ping_thread = Thread(target=ping, args=[mutex])
    pong_thread = Thread(target=pong, args=[mutex])

    ping_thread.start()
    pong_thread.start()


