import os
import PySimpleGUI as sg
import binascii as bnsci
from threading import Thread
import subprocess

def make_bitseq(s):
     return " ".join(f"{ord(i):08b}" for i in s)

def make_string(s):
     splits = s.split(" ")
     print(splits)
     letters = []
     for a in splits:
         if a == '': continue
         letters.append(chr(int(a,2)))
     finalSTR = ""
     for lttr in letters:
         finalSTR = finalSTR + lttr
     return finalSTR

global layout

layout = [
         [sg.Input("IP")],
         [sg.Input("Password")],
         [sg.Input("Orientation")],
         [sg.Checkbox("evdev", False)],
         [sg.Checkbox("Save Password?",False)],
         [sg.Button("Run")],
         [sg.Button("Run using saved data")],
         [sg.Button("Quit")]
         ]

window = sg.Window("reMouse GUI",layout)

def run(values):
    print(values)
    while "/" in values[2]: values[2] = values[2][:-1]
    cmd = "remouse --address " + values[0] + " --password " + values[1] + " --orientation " + values[2]
    print(len(values))
    if values[4]:
        print("Writing password")
        File = open("data.txt",'w')
        readFile = open("data.txt",'r')
        read = readFile.read()
        toWrite = make_bitseq(values[0] + "," + values[1] + "," + values[2] + "/") #The slash is added to indicate the end of this data
        if toWrite in read:
            print(cmd)
            return cmd
        print(toWrite)
        File.write(toWrite)
        File.close()
    if values[3]:
        cmd += " --evdev"
    print(cmd)
    return cmd

def runWithSavedData(values):
    File = open("data.txt","r")
    lines = File.read()
    lines = lines.split("/")
    print(len(lines))
    if '' in lines:
        lines.remove(len(lines))
    print(lines)
    if len(lines) == 1:
        read = lines[0]
        readString = make_string(read)
        readString = readString.split(",")
        values[0] = readString[0]
        values[1] = readString[1]
        values[2] = readString[2]
        print(values)
        return run(values)

while True:
    event, values = window.read()
    cmd = ""
    if event == "Run":
        numChoice = 1
        cmd = run(values)
        thread = Thread(target = lambda: os.system(cmd))
        thread.start()

    elif event == "Run using saved data":
        cmd = runWithSavedData(values)
        thread = Thread(target = lambda: os.system(cmd))
        thread.start()

    else:

        window.close()
        exit()





