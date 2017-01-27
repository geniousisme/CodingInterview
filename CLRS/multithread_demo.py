import time, datetime
import threading
import Queue

JOB_NUM = 20

class Job(object):
    def __init__(self, name):
        self.name = name

    def do(self):
        time.sleep(2)
        print "\t[info] Job-{0} is done!".format(self.name)

def get_que_with_x_jobs(x):
    que = Queue.Queue()
    for i in xrange(x):
        que.put(Job(str(i)))
    return que

def do_job(*args):
    queue = args[0]
    while queue.qsize() > 0:
        job = queue.get()
        job.do()

class SingleThread(object):
    def __init__(self):
        print "Single Thread !!"

    def run(self):
        que = get_que_with_x_jobs(JOB_NUM)

        start_time = datetime.datetime.now()

        do_job(que)

        total_time = datetime.datetime.now() - start_time
        print "\t[info] All Jobs are done in {0} secconds!".format(total_time)

class MultiThread(object):
    def __init__(self):
        print "Multi Thread !!"

    def run(self):
        que = get_que_with_x_jobs(JOB_NUM)

        start_time = datetime.datetime.now()

        # init three threads
        thrd1 = threading.Thread(target=do_job, name="Thrd-1", args=(que,))
        thrd2 = threading.Thread(target=do_job, name="Thrd-2", args=(que,))
        thrd3 = threading.Thread(target=do_job, name="Thrd-3", args=(que,))
        thrd4 = threading.Thread(target=do_job, name="Thrd-4", args=(que,))

        thrd1.start()
        thrd2.start()
        thrd3.start()
        thrd4.start()

        while thrd1.is_alive() or thrd2.is_alive() or thrd3.is_alive() or thrd4.is_alive():
            time.sleep(0.01)

        total_time = datetime.datetime.now() - start_time
        print "\t[info] All Jobs are done in {0} secconds!".format(total_time)

if __name__ == "__main__":
     st = SingleThread()
     st.run()

     mt = MultiThread()
     mt.run()

