import os
import time
import sys
from threading import Thread

filesToMove = ['Installer.py','Install.bat','Install.command','ReGUI.py','ReGUI.bat','ReGUI.command']

commands = "pip3 install remarkable-mouse; pip install remarkable-mouse; pip3 install PySimpleGUI; pip install PySimpleGUI"
commander = Thread(target = lambda: os.system(commands))

commander.start()

time.sleep(5)

def linux():
    filesToMove.remove('Install.bat')
    filesToMove.remove('ReGUI.bat')
    withoutHome = currentPos[currentPos.find('home')+5:len(currentPos)]
    path = '/home/' + withoutHome[0:withoutHome.find('/')+1]
    toMoveTo = path + 'Documents/ReGUI/'
    moveCommands = ''
    for File in filesToMove:
        prevPos = currentPos + "/" + File
        moveCommands = moveCommands + ('cp ' + prevPos + ' ' + toMoveTo) + ';'
    cmds = ['cd','cd Documents','mkdir ' + toMoveTo,'cd ReGUI',moveCommands,'chmod +x ReGUI.command','chmod +x Install.command']
    for command in cmds:
        reply = os.system(command)


def darwin(): # MacOS
    filesToMove.remove('Install.bat')
    filesToMove.remove('ReGUI.bat')
    toMoveTo = '/Applications/ReGUI/'
    moveCommands = ''
    for File in filesToMove:
        prevPos = currentPos + "/" + File
        moveCommands = moveCommands + ('cp ' + prevPos + ' ' + toMoveTo) + ';'
    cmds = ['cd','cd Applications','mkdir ' + toMoveTo,'cd ReGUI',moveCommands,'chmod +x ReGUI.command','chmod +x Install.command']
    for command in cmds:
        reply = os.system(command)

def win32():
    filesToMove.remove('Install.command')
    filesToMove.remove('ReGUI.command')
    toMoveTo = '/Documents/ReGUI/'
    moveCommands = ''
    for File in filesToMove:
        prevPos = currentPos + "/" + File
        moveCommands = moveCommands + ('cp ' + prevPos + ' ' + toMoveTo) + ';'
    cmds = ['cd','cd Documents','mkdir ' + toMoveTo,'cd ReGUI',moveCommands,'chmod +x ReGUI.bat','chmod +x Install.bat']
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