import telnetlib
import serial
from serial import Serial
import io
import time
import pysnmp
from pysnmp.hlapi import *

FILEPATH = ("C:\\DOC_SCRIPT\\WDOG")

MAC = ("d43f.cbf7.06b5")
IP = "10.237.138.17"
MAC_1 = ("7823.aea6.70bd")
IP_1 = "10.237.138.14"

E6000 = "10.237.129.210"
B = "show cable modem %s\n"%MAC
B_1 = "show cable modem %s\n"%MAC_1

def E6k_TEST(B):    
    try:        
        tn = telnetlib.Telnet(E6000,timeout = 10)
        tn.read_until(b'Login:')
        tn.write(b'admin\n')    
        tn.write(b'\n')    
        tn.read_until(b'Password:')
        tn.write(b'admin\n')    
        tn.write(b'\n')    
        tn.read_until(b'E6000K-BLR>')
        tn.write(b'ena\r\n')    
        tn.write(b'\n')    
        tn.write(b'%s'%(B).encode())
        tn.write(b'    ')    
        tn.write(b'exit\r\n')
        k = (tn.read_all().decode('ascii'))
        file = open("%s\\IP_FROM_E6k.txt"%(FILEPATH),"w")
        file.write(k)
        file.close()
        with open("%s\\IP_FROM_E6k.txt"%(FILEPATH),"r") as task:        
            for line in task:
                try:
                    if "Operational " in line:                    
                        return (1)                               
                except: r=0
    except:
        pass

def flip_1():
        CM_ser = serial.Serial('COM5', 115200, timeout=1)
        for x in range (0,20):
            time.sleep(1)
            CM_ser.write(b'\x03\n')             
        CM_ser.write(b'setenv -p DT_IDX 1\n')
        time.sleep(1) 
        CM_ser.write(b'setenv -p KL_IDX 1\n')
        time.sleep(1) 
        CM_ser.write(b'setenv -p RG_IDX 1\n')
        time.sleep(1) 
        CM_ser.write(b'setenv -p CM_IDX 1\n')
        time.sleep(1)        
        CM_ser.close()             # close port

def flip_0():
        CM_ser = serial.Serial('COM5', 115200, timeout=1)
        for x in range (0,20):
            time.sleep(1)
            CM_ser.write(b'\x03\n')            
        CM_ser.write(b'setenv -p DT_IDX 0\n')
        time.sleep(1) 
        CM_ser.write(b'setenv -p KL_IDX 0\n')
        time.sleep(1) 
        CM_ser.write(b'setenv -p RG_IDX 0\n')
        time.sleep(1) 
        CM_ser.write(b'setenv -p CM_IDX 0\n')
        time.sleep(1)        
        CM_ser.close()   

def flip_1_1():
        CM_ser = serial.Serial('COM4', 115200, timeout=1)
        for x in range (0,20):
            time.sleep(1)
            CM_ser.write(b'\x03\n')             
        CM_ser.write(b'setenv -p DT_IDX 1\n')
        time.sleep(1) 
        CM_ser.write(b'setenv -p KL_IDX 1\n')
        time.sleep(1) 
        CM_ser.write(b'setenv -p RG_IDX 1\n')
        time.sleep(1) 
        CM_ser.write(b'setenv -p CM_IDX 1\n')
        time.sleep(1)        
        CM_ser.close()             # close port

def flip_0_1():
        CM_ser = serial.Serial('COM4', 115200, timeout=1)
        for x in range (0,20):
            time.sleep(1)
            CM_ser.write(b'\x03\n')            
        CM_ser.write(b'setenv -p DT_IDX 0\n')
        time.sleep(1) 
        CM_ser.write(b'setenv -p KL_IDX 0\n')
        time.sleep(1) 
        CM_ser.write(b'setenv -p RG_IDX 0\n')
        time.sleep(1) 
        CM_ser.write(b'setenv -p CM_IDX 0\n')
        time.sleep(1)        
        CM_ser.close()
        
def SNMP(IP):
    for (errorIndication,
        errorStatus,
        errorIndex,
        varBinds) in setCmd(SnmpEngine(),
            CommunityData('public'),
            UdpTransportTarget((IP, 161)),                    
            ContextData(),        
            ObjectType(ObjectIdentity('1.3.6.1.2.1.69.1.1.3.0'), Integer32(1))):                
        if errorIndication or errorStatus:
            pass
        
################################################################################################################
k = 0
m = 0
while k < 5000000000000000000000000000000000:    
    if E6k_TEST(B) == 1 and E6k_TEST(B_1) == 1:
        if m == 0:
            SNMP(IP)            
            flip_1()
            SNMP(IP_1)
            flip_1_1()
            print("Flip from 0 to 1 in BOLT")                                 
            m = 1
    if E6k_TEST(B) == 1 and E6k_TEST(B_1) == 1:
        if m == 1:
            SNMP(IP)            
            flip_0()
            SNMP(IP_1)
            flip_0_1()
            print("Flip from 1 to 0 in BOLT")                                  
            m = 0
            k = k+1
            print("Total flip count is %s"%k)

print("PROCESS COMPLETED PRESS ENTER TO CLOSE THIS WINDOW")
os.system("pause")
