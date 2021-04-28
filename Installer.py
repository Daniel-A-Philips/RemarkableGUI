import os
import time
import sys
from threading import Thread

filesToMove = ['Installer.py','ReGUI.py']

commands = "pip3 install remarkable-mouse; pip install remarkable-mouse; pip3 install PySimpleGUI; pip install PySimpleGUI"
commander = Thread(target = lambda: os.system(commands))

commander.start()

time.sleep(5)

def linux():
    withoutHome = currentPos[currentPos.find('home')+5:len(currentPos)]
    path = '/home/' + withoutHome[0:withoutHome.find('/')+1]
    toMoveTo = path + 'Documents/ReGUI/'
    InstallerPos = currentPos + "/" + filesToMove[0]
    ReGUIPos = currentPos + "/" + filesToMove[1]
    moveInstaller = 'cp ' + InstallerPos + ' ' + toMoveTo
    moveReGUI = 'cp ' + ReGUIPos + ' ' + toMoveTo
    cmds = ['cd','cd Documents','mkdir ' + toMoveTo,'cd ReGUI',moveInstaller,moveReGUI]
    for command in cmds:
        reply = os.system(command)


def darwin(): # MacOS
    toMoveTo = '/Applications/ReGUI/'
    InstallerPos = currentPos + "/" + filesToMove[0]
    ReGUIPos = currentPos + "/" + filesToMove[1]
    moveInstaller = 'cp ' + InstallerPos + ' ' + toMoveTo
    moveReGUI = 'cp ' + ReGUIPos + ' ' + toMoveTo
    cmds = ['cd','cd Documents','mkdir ' + toMoveTo,'cd ReGUI',moveInstaller,moveReGUI]
    for command in cmds:
        reply = os.system(command)

def win32():
    toMoveTo = '/documents/ReGUI/'
    InstallerPos = currentPos + "/" + filesToMove[0]
    ReGUIPos = currentPos + "/" + filesToMove[1]
    moveInstaller = 'cp ' + InstallerPos + ' ' + toMoveTo
    moveReGUI = 'cp ' + ReGUIPos + ' ' + toMoveTo
    cmds = ['cd','cd Documents','mkdir ' + toMoveTo,'cd ReGUI',moveInstaller,moveReGUI]
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