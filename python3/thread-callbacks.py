from threading import Thread, current_thread, Event
import time

class MainThread(Thread):
    def __init__(self):
        Thread.__init__(self) 
        self.worker = WorkerThread(parent=self)
        self.worker.daemon = True
        self.worker.start()

        self.event_stop = Event()

        print("__init__, in thread %s" % current_thread().name)
    
    def callback(self):
        print("callback executed by: ", current_thread().name)
        self.stop()

    def run(self):
        print("run, in thread %s" % current_thread().name)
        while not self.event_stop.is_set():
            print("main")
            time.sleep(1)
        print("main exited")

    def stop(self):
        self.event_stop.set()

    def __str__(self):
        return "main-thread"


class WorkerThread(Thread):
    def __init__(self, parent):
        Thread.__init__(self)
        self.parent = parent

        print("__init__, in thread %s" % current_thread().name)

    def run(self):
        print("run, in thread %s" % current_thread().name)

        time.sleep(2)
        self.parent.callback()
        print("worker exited")

    def __str__(self):
        return "worker-thread"

if __name__ == "__main__":
    main = MainThread()
    main.daemon = True
    main.start()

    main.join()
    main.worker.join()

    print("Exited...")
