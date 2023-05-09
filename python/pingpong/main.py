from threading import Thread, Lock

value = 'ping'

def ping(lock):
    global value

    while True:
        if lock.acquire(blocking = False):
            if value == 'ping':
                print(value)
                value = 'pong'
            
            lock.release()

def pong(lock):
    global value

    while True:
        if lock.acquire(blocking = False):
            if value == 'pong':
                print(value)
                value = 'ping'
            
            lock.release()

if __name__ == "__main__":
    lock = Lock()

    ping_thread = Thread(target=ping, args=[lock])
    pong_thread = Thread(target=pong, args=[lock])

    ping_thread.start()
    pong_thread.start()


