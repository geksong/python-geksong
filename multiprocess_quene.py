# -*- encoding: utf-8 -*-

from multiprocessing import Process, Queue
import os, time, random

def writer(que):
    for i in ["A","B","C","D"]:
        print "put %s in queue" % i
        que.put(i)
        time.sleep(random.random())

def reader(que):
    while True:
        v = que.get(True)
        print "get %s from queue" % v

if __name__ == "__main__":
    q = Queue()
    pw = Process(target=writer, args=(q,))
    pr = Process(target=reader, args=(q,))
    pw.start()
    pr.start()
    pw.join()
    pr.terminate()
