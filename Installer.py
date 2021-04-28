import os
import sys
import PySimpleGUI as sg
import binascii as bnsci
from threading import Thread

filesToMove = ['Installer.py','ReGUI.py']
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
        if(reply == 'mkdir: cannot create directory ‘ReGUI’: File exists'):
            print("Error, file already exists")


def darwin():
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
        if(reply == 'mkdir: cannot create directory ‘ReGUI’: File exists'):
            print("Error, file already exists")

OS = sys.platform   
currentPos = str(os.path.abspath(os.getcwd()))

if OS == 'linux':
    linux()
#elif OS == 'win32':
    #win32()
elif OS == 'darwin':
    darwin()