import os
from os import path
from termcolor import colored
import ctypes
import sys


os.system('cls')


def Mbox(title, text, style):
    return ctypes.windll.user32.MessageBoxW(0, text, title, style)


def clrscr():
    rep = input('Press ENTER to Proceed'.center(120))
    if rep == '':
        os.system('cls')


def printer(x):
    for _ in range(0, x):
        print()


def welcome():
    printer(2)
    print(colored("Welcome To EZ Shutdown", 'magenta').center(130))
    printer(3)
    colored("!! Note that if you don't wanna rename the folder just press ENTER when it asks you to rename it !!", 'red')


def Done():
    os.system('cls')
    printer(4)
    print(colored("Everything went perfect.. ", 'red'))
    Mbox('task succeeded ', "the process completed successfully", 1)


def ReqNumber(nb, msg):
    while (nb.isdigit() == False):
        nb = input(msg)
    return nb


def RequestDuration():
    printer(4)
    print()
    print('After how much time you want your pc to shutdown ? ')
    hours = minutes = seconds = ''
    hours = int(ReqNumber(hours, 'Number of Hours here => '))
    minutes = int(ReqNumber(minutes, 'Number of minutes here => '))
    seconds = int(ReqNumber(seconds, 'Number of seconds here => '))
    return(hours, minutes, seconds)


def Converter(h, m, s):
    sum = (h*3600)+(m*60)+s
    return sum


def ReqChoice():
    print('1- Config an Auto-Shutdown')
    print('2- Remove an active auto-sutdown')
    print()
    choice = ''
    while choice != '1' and choice != '2':
        choice = input('=> ')
    return choice


    ##Callers##
welcome()
answ = ReqChoice()
if answ == '2':

    os.system('shutdown -a')
else:
    os.system('cls')
    dur = RequestDuration()
    h, m, s = dur
    # h = dur[0]
    # m = dur[1]
    # s = dur[2]
    sum = Converter(h, m, s)
    res = 'shutdown -s -t '+str(sum)
    os.system(res)
Done()
