import threading
from time import sleep, ctime
import logging
import _thread

logging.basicConfig(level=logging.INFO)


def loop0():
    logging.info("start loop0 at" + ctime())
    sleep(4)
    logging.info("end loop0 at" + ctime())


def loop1():
    logging.info("start loop1 at" + ctime())
    sleep(2)
    logging.info("end loop1 at" + ctime())


loops = [0.1, 1, 2, 4]


def loop(n, sec, lock):
    logging.info("start loop{} at {}".format(n, ctime()))
    sleep(sec)
    lock.release()
    logging.info("end loop{} at {}".format(n, ctime()))


def _thread_loop_first():
    logging.info("start all at " + ctime())
    locks = []
    nloop = range(len(loops))
    for i in nloop:
        lock = _thread.allocate_lock()
        lock.acquire()
        locks.append(lock)

    for i in nloop:
        _thread.start_new_thread(loop, (i, loops[i], locks[i]))

    for i in nloop:
        while locks[i].locked(): pass

    # _thread.start_new_thread(loop0, ())
    # _thread.start_new_thread(loop1, ())
    # sleep(6)
    logging.info("end all at " + ctime())


def loop_ting(n, sec):
    logging.info("start loop{} at {}".format(n, ctime()))
    sleep(sec)
    logging.info("end loop{} at {}".format(n, ctime()))


class MyThread(threading.Thread):
    def __init__(self, func, args, name=''):
        threading.Thread.__init__(self)
        self.func = func
        self.args = args
        self.name = name

    def run(self):
        self.func(*self.args)


def threading_loop():
    logging.info("start all at " + ctime())
    threads = []
    nloop = range(len(loops))
    for i in nloop:
        # t = threading.Thread(target=loop_ting, args=(i, loops[i]))
        t = MyThread(loop_ting, (i, loops[i]), loop.__name__)
        threads.append(t)
    for i in nloop:
        threads[i].start()
    for i in nloop:
        # 让主线程等待子线程释放锁
        threads[i].join()
    logging.info("end all at " + ctime())


def main():
    # _thread_loop_first()
    threading_loop()


if __name__ == '__main__':
    main()
