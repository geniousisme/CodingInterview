import time

def print_string(string):
    def callback():
        print string
    return callback

class EventLoop(object):
    def __init__(self):
        self.tasks = []

    def schedule(self, time_stamp, func):
        self.tasks.append((time_stamp, func))

    def run(self):
        tasks = sorted(self.tasks, key=lambda x: x[0])
        for i in xrange(len(tasks)):
            time.sleep(tasks[i][0] - 0 if i < 1 else tasks[i - 1][0])
            tasks[i][1]()

if __name__ == "__main__":
    eventLoop = EventLoop()
    eventLoop.schedule(3, print_string("World"))
    eventLoop.schedule(2, print_string("Big"))
    eventLoop.schedule(1, print_string("Hello"))
    eventLoop.run()
    print "done"
