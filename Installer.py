import os
import time
import sys
from threading import Thread

filesToMove = ['Installer.py','Installer.bat','Installer.command','ReGUI.py','ReGUI.bat','ReGUI.command']

commands = "pip3 install remarkable-mouse; pip install remarkable-mouse; pip3 install PySimpleGUI; pip install PySimpleGUI"
commander = Thread(target = lambda: os.system(commands))

commander.start()

time.sleep(5)

def linux():
    fileToMove.remove(1)
    fileToMove.remove(3)
    withoutHome = currentPos[currentPos.find('home')+5:len(currentPos)]
    path = '/home/' + withoutHome[0:withoutHome.find('/')+1]
    toMoveTo = path + 'Documents/ReGUI/'
    moveCommands = ''
    for File in filesToMove:
        prevPos = currentPos + "/" + File
        moveCommands = moveCommands + ('cp ' + prevPos + ' ' + toMoveTo) + ';'
    cmds = ['cd','cd Documents','mkdir ' + toMoveTo,'cd ReGUI',moveCommands]
    for command in cmds:
        reply = os.system(command)


def darwin(): # MacOS
    fileToMove.remove(1)
    fileToMove.remove(3)
    toMoveTo = '/Applications/ReGUI/'
    moveCommands = ''
    for File in filesToMove:
        prevPos = currentPos + "/" + File
        moveCommands = moveCommands + ('cp ' + prevPos + ' ' + toMoveTo) + ';'
    cmds = ['cd','cd Applications','mkdir ' + toMoveTo,'cd ReGUI',moveCommands]
    for command in cmds:
        reply = os.system(command)

def win32():
    fileToMove.remove(2)
    fileToMove.remove(4)
    toMoveTo = '/Documents/ReGUI/'
    moveCommands = ''
    for File in filesToMove:
        prevPos = currentPos + "/" + File
        moveCommands = moveCommands + ('cp ' + prevPos + ' ' + toMoveTo) + ';'
    cmds = ['cd','cd Documents','mkdir ' + toMoveTo,'cd ReGUI',moveCommands]
    for command in cmds:
        reply = os.system(command)

OS = sys.platform   
currentPos = str(os.path.abspath(os.getcwd()))

if OS == 'linux':
    linux()
elif OS == 'win32':
    win32()
elif OS == 'darwin':
    darwin()

print("Download complete")