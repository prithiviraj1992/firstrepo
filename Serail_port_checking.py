import serial
from serial import Serial
import io
import time

FILEPATH = ("C:\\DOC_SCRIPT")

################################################################################################################
RG_ser = serial.Serial('COM1', 115200, timeout=1)
print(RG_ser.name)         # check which port was really used
RG_ser.write(b'version\n')     # write a string
s = RG_ser.read(100000000)
print(s)
RG_ser.close()             # close port

################################################################################################################
CM_ser = serial.Serial('COM4', 115200, timeout=1)
print(CM_ser.name)         # check which port was really used
CM_ser.write(b'version\n')     # write a string
s = CM_ser.read(100000000)
print(s)
CM_ser.write(b'/taskSuspend\n')
time.sleep(5)
CM_ser.write(b'0x83e9aecc\n')
CM_ser.close()             # close port

file = open("%s\\CM_serial.txt"%(FILEPATH),"w")
file.write(s)
file.close()
with open("%s\\CM_serial.txt"%(FILEPATH),"r") as task:
    for line in task:
        try:
            if "Operational " in line:
                print("TRUE")
                return (1)
        except: r=0            

