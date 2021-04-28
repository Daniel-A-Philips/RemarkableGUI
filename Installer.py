import os
import sys
from threading import Thread

filesToMove = ['Installer.py','ReGUI.py']
remouse3__Installer = Thread(target = lambda: os.system("pip3 install remarkable-mouse"))
remouse__Installer = Thread(target = lambda: os.system("pip install remarkable-mouse"))
pysimplegui3__Installer = Thread(target = lambda: os.system("pip3 install PySimpleGUI"))
pysimplegui__Installer = Thread(target = lambda: os.system("pip install PySimpleGUI"))

remouse3__Installer.start()
remouse__Installer.start()
pysimplegui3__Installer.start()
pysimplegui__Installer.start()

def linux():
    withoutHome = currentPos[currentPos.find('home')+5:len(currentPos)]
    path = '/home/' + withoutHome[0:withoutHome.find('/')+1]
    print(path)
    toMoveTo = path + 'Documents/ReGUI/'
    InstallerPos = currentPos + "/" + filesToMove[0]
    ReGUIPos = currentPos + "/" + filesToMove[1]
    moveInstaller = 'cp ' + InstallerPos + ' ' + toMoveTo
    moveReGUI = 'cp ' + ReGUIPos + ' ' + toMoveTo
    cmds = ['cd','cd Documents','mkdir ' + toMoveTo,'cd ReGUI',moveInstaller,moveReGUI]
    for command in cmds:
        print(command)
        reply = os.system(command)


def darwin(): # MacOS
    toMoveTo = '/Applications/ReGUI/'
    InstallerPos = currentPos + "/" + filesToMove[0]
    ReGUIPos = currentPos + "/" + filesToMove[1]
    moveInstaller = 'cp ' + InstallerPos + ' ' + toMoveTo
    moveReGUI = 'cp ' + ReGUIPos + ' ' + toMoveTo
    cmds = ['cd','cd /Applications','mkdir ReGUI','cd ReGUI',]
    cmds = ['cd','cd Documents','mkdir ' + toMoveTo,'cd ReGUI',moveInstaller,moveReGUI]
    for command in cmds:
        print(command)
        reply = os.system(command)

def win32():
    toMoveTo = '/documents/ReGUI/'
    InstallerPos = currentPos + "/" + filesToMove[0]
    ReGUIPos = currentPos + "/" + filesToMove[1]
    moveInstaller = 'cp ' + InstallerPos + ' ' + toMoveTo
    moveReGUI = 'cp ' + ReGUIPos + ' ' + toMoveTo
    cmds = ['cd','cd /documents','mkdir ReGUI','cd ReGUI',]
    cmds = ['cd','cd Documents','mkdir ' + toMoveTo,'cd ReGUI',moveInstaller,moveReGUI]
    for command in cmds:
        print(command)
        reply = os.system(command)

OS = sys.platform   
currentPos = str(os.path.abspath(os.getcwd()))

if OS == 'linux':
    linux()
elif OS == 'win32':
    win32()
elif OS == 'darwin':
    darwin()