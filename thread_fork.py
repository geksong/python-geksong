# -*- encoding: utf-8 -*-
import os

print "Processor is (%s) start..." % (os.getpid())

ch_thread_pid = os.fork()

if ch_thread_pid == 0:
    print "child thread (%s) is runing..." % os.getpid()
else:
    print "parent thread (%s) is runing..." % ch_thread_pid
