# -*- coding:utf-8 -*-

from writein import *
from os import *

print("\nLoading datas......")
msgs = putdatas()
print("\nFinished!")

cmd_str = "\n>"

while True:
    cmd = input(cmd_str)
    if cmd == "loadgrades":
        grades = int(input("Grade:"))
