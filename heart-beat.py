# heart beat example

import time
from threading import Timer


def action():
    global t
    print "\n--------->>>>> You are late !!!"
    t.cancel()
    t = Timer(10.0, action)
    t.start()


# after 10 seconds, "You are late" will be printed
def listen_sth():
    global t
    while True:
        t = Timer(10.0, action)
        t.start()
        user_input = raw_input('\nEnter an input before 10 seconds : ')
        t.cancel()
        print "\nTime is restarted again !!!"


listen_sth()
