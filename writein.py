# -*- coding:utf-8 -*-

from random import *
from string import *
import time

datas = []

# Date time

date1 = (2005, 1, 1, 0, 0, 0, 0, 0, 0)
date2 = (2008, 12, 31, 23, 59, 59, 0, 0, 0)

stime = time.mktime(date1)
etime = time.mktime(date2)


def classmessages():
    msgs = []
    for schoolclasses in range(1, 18):
        for students in range(1, randint(3, 60) + 1):
            names = [choice(ascii_uppercase) + choice(ascii_lowercase) +
                     choice(ascii_lowercase) + str(randint(1, 9)),
                     choice(ascii_uppercase) + choice(ascii_lowercase) +
                     choice(ascii_lowercase) + str(randint(1, 9)),
                     choice(ascii_uppercase) + choice(ascii_lowercase) +
                     choice(ascii_lowercase) + str(randint(1, 9))
                     ]
            gender = choice(["Boy", "Girl"])
            times = randint(stime, etime)
            date_touple = time.localtime(times)
            borndate = time.strftime("%Y-%m-%d", date_touple)
            msgs.append({"class" + str(schoolclasses): [names[0], gender, borndate, names[1], names[2]]})
    return msgs

# classes read


def putdatas():
    global datas
    for i in range(1, 4):
        if i == 1:
            datas.append({"Grade7": classmessages()})
        elif i == 2:
            datas.append({"Grade8": classmessages()})
        elif i == 3:
            datas.append({"Grade9": classmessages()})
    return datas
