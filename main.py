# -*- coding:utf-8 -*-

from writein import *
from os import *
import platform
import sys

print("\nLoading datas......")
msgs = putdatas()
print("\nFinished!")

cmd_str = "\n> "
grade_data = 0

# help command
help_datas = [
    "loadgrades - include grades and dir in grades.",
    "showgrades - show loaded grades.",
    "showdatas - show loaded datas.",
    "rds - clear your loads.",
    "clear - clear screen.",
    "classnumber - show classrooms number",
    "exit - quit program.",
    "showallstudentsnames - show all current grades student\'s names, please type \"loadgrades\" command first"
]

while True:
    cmd = input(cmd_str)
    if cmd == "loadgrades":
        grades = int(input("Grade:"))
        if grades == 7:
            cmd_str = "\ngrade7> "
            grades_data = msgs[0]['Grade7']
        elif grades == 8:
            cmd_str = "\ngrade8> "
            grades_data = msgs[0]['Grade8']
        elif grades == 9:
            cmd_str = "\ngrade9> "
            grades_data = msgs[0]['Grade9']
        else:
            print("\nCommand Error......")
    elif cmd == "showgrades":
        for grades_name_msg in msgs:
            for grades_name in grades_name_msg.keys():
                print(grades_name)
    elif cmd == "showdatas":
        print(msgs)
    elif cmd == "classnumber":
        print("\n17 classrooms...")
    elif cmd == "rds":
        cmd_str = "\n> "
        grade_data = 0
    elif cmd == "clear":
        if platform.system() == "Windows":
            system("cls")
        else:
            system("clear")
    elif cmd == "exit":
        try:
            sys.exit()
        except SystemExit:
            break
        else:
            sys.exit()
    elif cmd == "help":
        for helping in help_datas:
            print(helping)
    elif cmd == "showallstudentsnames" and grade_data != 0:
        for students_names in grade_data:
            for students_name in students_names.value():
                print(students_name[0])
    else:
        print("\nError command:" + cmd)
