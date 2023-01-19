import pysnmp
from pysnmp.hlapi import *
import telnetlib
import time
import datetime
import os
import glob
import time
import datetime


print("SOFTWARE DOWNLOAD")
C = input("Please enter the IP address of the CM :")
today = datetime.date.today()

FILEPATH = ("C:\\DOC_SCRIPT")

directory=("%s"%(FILEPATH))
os.chdir(directory)
files=glob.glob('SW_DOWNLOAD_OUTPUT.txt')
for test in files:
    os.unlink(test)
    
def getErrorReport(C,k):
        t1 = time.time()
        for (errorIndication,
             errorStatus,
             errorIndex,
             varBinds) in getCmd(SnmpEngine(),
                CommunityData('public'),
                UdpTransportTarget((C, 161)),
                ContextData(),
                ObjectType(ObjectIdentity('1.3.6.1.2.1.1.1.0')),
                ObjectType(ObjectIdentity('1.3.6.1.2.1.69.1.3.7.0')),
                ObjectType(ObjectIdentity('1.3.6.1.2.1.69.1.3.8.0')),
                ObjectType(ObjectIdentity('1.3.6.1.2.1.69.1.5.8.1.7.1')),
                ObjectType(ObjectIdentity('1.3.6.1.2.1.69.1.5.8.1.7.2')),
                ObjectType(ObjectIdentity('1.3.6.1.2.1.69.1.5.8.1.7.3')),
                ObjectType(ObjectIdentity('1.3.6.1.2.1.69.1.5.8.1.7.4')),
                ObjectType(ObjectIdentity('1.3.6.1.2.1.69.1.5.8.1.7.5')),
                ObjectType(ObjectIdentity('1.3.6.1.2.1.69.1.5.8.1.7.6')),
                ObjectType(ObjectIdentity('1.3.6.1.2.1.69.1.5.8.1.7.7')),
                ObjectType(ObjectIdentity('1.3.6.1.2.1.69.1.5.8.1.7.8')),
                ObjectType(ObjectIdentity('1.3.6.1.2.1.69.1.5.8.1.7.9')),
                ObjectType(ObjectIdentity('1.3.6.1.2.1.69.1.5.8.1.7.10')),
                ObjectType(ObjectIdentity('1.3.6.1.2.1.69.1.5.8.1.7.11')),
                ObjectType(ObjectIdentity('1.3.6.1.2.1.69.1.5.8.1.7.12')),
                ObjectType(ObjectIdentity('1.3.6.1.2.1.69.1.5.8.1.7.13')),
                ObjectType(ObjectIdentity('1.3.6.1.2.1.69.1.5.8.1.7.14')),
                ObjectType(ObjectIdentity('1.3.6.1.2.1.69.1.5.8.1.7.15')),
                ObjectType(ObjectIdentity('1.3.6.1.2.1.69.1.5.8.1.7.16')),
                ObjectType(ObjectIdentity('1.3.6.1.2.1.69.1.5.8.1.7.17')),
                ObjectType(ObjectIdentity('1.3.6.1.2.1.69.1.5.8.1.7.18')),
                ObjectType(ObjectIdentity('1.3.6.1.2.1.69.1.5.8.1.7.19')),
                ObjectType(ObjectIdentity('1.3.6.1.2.1.69.1.5.8.1.7.20')),
                ObjectType(ObjectIdentity('1.3.6.1.2.1.69.1.5.8.1.7.21')),
                ObjectType(ObjectIdentity('1.3.6.1.2.1.69.1.5.8.1.7.22')),
                ObjectType(ObjectIdentity('1.3.6.1.2.1.69.1.5.8.1.7.23')),
                ObjectType(ObjectIdentity('1.3.6.1.2.1.69.1.5.8.1.7.24')),
                ObjectType(ObjectIdentity('1.3.6.1.2.1.69.1.5.8.1.7.25')),
                ObjectType(ObjectIdentity('1.3.6.1.2.1.69.1.5.8.1.7.26')),
                ObjectType(ObjectIdentity('1.3.6.1.2.1.69.1.5.8.1.7.27')),
                ObjectType(ObjectIdentity('1.3.6.1.2.1.69.1.5.8.1.7.28')),
                ObjectType(ObjectIdentity('1.3.6.1.2.1.69.1.5.8.1.7.29')),
                ObjectType(ObjectIdentity('1.3.6.1.2.1.69.1.5.8.1.7.30')),
                ObjectType(ObjectIdentity('1.3.6.1.2.1.69.1.5.8.1.7.31')),
                ObjectType(ObjectIdentity('1.3.6.1.2.1.69.1.5.8.1.7.32')),
                ObjectType(ObjectIdentity('1.3.6.1.2.1.69.1.5.8.1.7.33')),
                ObjectType(ObjectIdentity('1.3.6.1.2.1.69.1.5.8.1.7.34')),
                ObjectType(ObjectIdentity('1.3.6.1.2.1.69.1.5.8.1.7.35')),
                ObjectType(ObjectIdentity('1.3.6.1.2.1.69.1.5.8.1.7.36')),
                ObjectType(ObjectIdentity('1.3.6.1.2.1.69.1.5.8.1.7.37')),
                ObjectType(ObjectIdentity('1.3.6.1.2.1.69.1.5.8.1.7.38')),
                ObjectType(ObjectIdentity('1.3.6.1.2.1.69.1.5.8.1.7.39')),
                ObjectType(ObjectIdentity('1.3.6.1.2.1.69.1.5.8.1.7.40')),
                ObjectType(ObjectIdentity('1.3.6.1.2.1.69.1.5.8.1.7.41')),
                ObjectType(ObjectIdentity('1.3.6.1.2.1.69.1.5.8.1.7.42')),
                ObjectType(ObjectIdentity('1.3.6.1.2.1.69.1.5.8.1.7.43')),
                ObjectType(ObjectIdentity('1.3.6.1.2.1.69.1.5.8.1.7.44')),
                ObjectType(ObjectIdentity('1.3.6.1.2.1.69.1.5.8.1.7.45')),
                ObjectType(ObjectIdentity('1.3.6.1.2.1.69.1.5.8.1.7.46')),
                ObjectType(ObjectIdentity('1.3.6.1.2.1.69.1.5.8.1.7.47')),
                ObjectType(ObjectIdentity('1.3.6.1.2.1.69.1.5.8.1.7.48')),
                ObjectType(ObjectIdentity('1.3.6.1.2.1.69.1.5.8.1.7.49')),
                ObjectType(ObjectIdentity('1.3.6.1.2.1.69.1.5.8.1.7.50')),
                ObjectType(ObjectIdentity('1.3.6.1.2.1.69.1.5.8.1.7.51')),
                ObjectType(ObjectIdentity('1.3.6.1.2.1.69.1.5.8.1.7.52')),
                ObjectType(ObjectIdentity('1.3.6.1.2.1.69.1.5.8.1.7.53')),
                ObjectType(ObjectIdentity('1.3.6.1.2.1.69.1.5.8.1.7.54')),
                ObjectType(ObjectIdentity('1.3.6.1.2.1.69.1.5.8.1.7.55')),
                ObjectType(ObjectIdentity('1.3.6.1.2.1.69.1.5.8.1.7.56')),
                ObjectType(ObjectIdentity('1.3.6.1.2.1.69.1.5.8.1.7.57')),
                ObjectType(ObjectIdentity('1.3.6.1.2.1.69.1.5.8.1.7.58')),
                ObjectType(ObjectIdentity('1.3.6.1.2.1.69.1.5.8.1.7.59')),
                ObjectType(ObjectIdentity('1.3.6.1.2.1.69.1.5.8.1.7.60')),
                ObjectType(ObjectIdentity('1.3.6.1.2.1.69.1.5.8.1.7.61')),
                ObjectType(ObjectIdentity('1.3.6.1.2.1.69.1.5.8.1.7.62')),
                ObjectType(ObjectIdentity('1.3.6.1.2.1.69.1.5.8.1.7.63')),
                ObjectType(ObjectIdentity('1.3.6.1.2.1.69.1.5.8.1.7.64')),
                ObjectType(ObjectIdentity('1.3.6.1.2.1.69.1.5.8.1.7.65')),
                ObjectType(ObjectIdentity('1.3.6.1.2.1.69.1.5.8.1.7.66')),
                ObjectType(ObjectIdentity('1.3.6.1.2.1.69.1.5.8.1.7.67')),
                ObjectType(ObjectIdentity('1.3.6.1.2.1.69.1.5.8.1.7.68')),
                ObjectType(ObjectIdentity('1.3.6.1.2.1.69.1.5.8.1.7.69')),
                ObjectType(ObjectIdentity('1.3.6.1.2.1.69.1.5.8.1.7.70')),
                ObjectType(ObjectIdentity('1.3.6.1.2.1.69.1.5.8.1.7.71')),
                ObjectType(ObjectIdentity('1.3.6.1.2.1.69.1.5.8.1.7.72')),
                ObjectType(ObjectIdentity('1.3.6.1.2.1.69.1.5.8.1.7.73')),
                ObjectType(ObjectIdentity('1.3.6.1.2.1.69.1.5.8.1.7.74')),
                ObjectType(ObjectIdentity('1.3.6.1.2.1.69.1.5.8.1.7.75')),
                ObjectType(ObjectIdentity('1.3.6.1.2.1.69.1.5.8.1.7.76')),
                ObjectType(ObjectIdentity('1.3.6.1.2.1.69.1.5.8.1.7.77')),
                ObjectType(ObjectIdentity('1.3.6.1.2.1.69.1.5.8.1.7.78')),
                ObjectType(ObjectIdentity('1.3.6.1.2.1.69.1.5.8.1.7.79')),
                ObjectType(ObjectIdentity('1.3.6.1.2.1.69.1.5.8.1.7.80')),
                ObjectType(ObjectIdentity('1.3.6.1.2.1.69.1.5.8.1.7.81')),
                ObjectType(ObjectIdentity('1.3.6.1.2.1.69.1.5.8.1.7.82')),
                ObjectType(ObjectIdentity('1.3.6.1.2.1.69.1.5.8.1.7.83')),
                ObjectType(ObjectIdentity('1.3.6.1.2.1.69.1.5.8.1.7.84')),
                ObjectType(ObjectIdentity('1.3.6.1.2.1.69.1.5.8.1.7.85')),
                ObjectType(ObjectIdentity('1.3.6.1.2.1.69.1.5.8.1.7.86')),
                ObjectType(ObjectIdentity('1.3.6.1.2.1.69.1.5.8.1.7.87')),
                ObjectType(ObjectIdentity('1.3.6.1.2.1.69.1.5.8.1.7.88')),
                ObjectType(ObjectIdentity('1.3.6.1.2.1.69.1.5.8.1.7.89')),
                ObjectType(ObjectIdentity('1.3.6.1.2.1.69.1.5.8.1.7.90')),
                ObjectType(ObjectIdentity('1.3.6.1.2.1.69.1.5.8.1.7.91')),
                ObjectType(ObjectIdentity('1.3.6.1.2.1.69.1.5.8.1.7.92')),
                ObjectType(ObjectIdentity('1.3.6.1.2.1.69.1.5.8.1.7.93')),
                ObjectType(ObjectIdentity('1.3.6.1.2.1.69.1.5.8.1.7.94')),
                ObjectType(ObjectIdentity('1.3.6.1.2.1.69.1.5.8.1.7.95')),
                ObjectType(ObjectIdentity('1.3.6.1.2.1.69.1.5.8.1.7.96')),
                ObjectType(ObjectIdentity('1.3.6.1.2.1.69.1.5.8.1.7.97')),
                ObjectType(ObjectIdentity('1.3.6.1.2.1.69.1.5.8.1.7.98')),
                ObjectType(ObjectIdentity('1.3.6.1.2.1.69.1.5.8.1.7.99')),
                ObjectType(ObjectIdentity('1.3.6.1.2.1.69.1.5.8.1.7.100')),
                ObjectType(ObjectIdentity('1.3.6.1.2.1.69.1.5.8.1.7.101')),
                ObjectType(ObjectIdentity('1.3.6.1.2.1.69.1.5.8.1.7.102')),
                ObjectType(ObjectIdentity('1.3.6.1.2.1.69.1.5.8.1.7.103')),
                ObjectType(ObjectIdentity('1.3.6.1.2.1.69.1.5.8.1.7.104')),
                ObjectType(ObjectIdentity('1.3.6.1.2.1.69.1.5.8.1.7.105')),
                ObjectType(ObjectIdentity('1.3.6.1.2.1.69.1.5.8.1.7.106')),
                ObjectType(ObjectIdentity('1.3.6.1.2.1.69.1.5.8.1.7.107')),
                ObjectType(ObjectIdentity('1.3.6.1.2.1.69.1.5.8.1.7.108')),
                ObjectType(ObjectIdentity('1.3.6.1.2.1.69.1.5.8.1.7.109')),
                ObjectType(ObjectIdentity('1.3.6.1.2.1.69.1.5.8.1.7.100')),
                ObjectType(ObjectIdentity('1.3.6.1.2.1.69.1.5.8.1.7.111')),
                ObjectType(ObjectIdentity('1.3.6.1.2.1.69.1.5.8.1.7.112')),
                ObjectType(ObjectIdentity('1.3.6.1.2.1.69.1.5.8.1.7.113')),
                ObjectType(ObjectIdentity('1.3.6.1.2.1.69.1.5.8.1.7.114')),
                ObjectType(ObjectIdentity('1.3.6.1.2.1.69.1.5.8.1.7.115')),
                ObjectType(ObjectIdentity('1.3.6.1.2.1.69.1.5.8.1.7.116')),
                ObjectType(ObjectIdentity('1.3.6.1.2.1.69.1.5.8.1.7.117')),
                ObjectType(ObjectIdentity('1.3.6.1.2.1.69.1.5.8.1.7.118')),
                ObjectType(ObjectIdentity('1.3.6.1.2.1.69.1.5.8.1.7.119')),
                ObjectType(ObjectIdentity('1.3.6.1.2.1.69.1.5.8.1.7.120'))):       
            if errorIndication or errorStatus:
                print(errorIndication or errorStatus)
                break
            else:
                for varBind in varBinds:                        
                        u = str(varBind)
                        #print(u)
                        file = open("%s\\SW_ERROR_REPORT_FOR_REBOOT_COUNT_%s.txt"%(FILEPATH,k),"a")
                        file.write(u)
                        file.write("\n")
                        file.close()  

#k = 1
#getErrorReport(C,k)

def DocsResetNow(C):
    #print("inside docsdev")
    t1 = time.time()
    for (errorIndication,
            errorStatus,
            errorIndex,
             varBinds) in setCmd(SnmpEngine(),
                CommunityData('public'),
                UdpTransportTarget((C, 161)),
                ContextData(),
        #0, 25,  # fetch up to 25 OIDs one-shot
                ObjectType(ObjectIdentity('1.3.6.1.2.1.69.1.1.3.0'), Integer32(1))):
                
            if errorIndication or errorStatus:
               pass
    

def getSNMP(C,k):
        for (errorIndication,
             errorStatus,
             errorIndex,
             varBinds) in getCmd(SnmpEngine(),
                CommunityData('public'),
                UdpTransportTarget((C, 161)),
                ContextData(),
                ObjectType(ObjectIdentity('1.3.6.1.2.1.69.1.3.5.0')),
                ObjectType(ObjectIdentity('1.3.6.1.2.1.69.1.3.2.0')),                                 
                ObjectType(ObjectIdentity('1.3.6.1.2.1.69.1.3.4.0')),
                ObjectType(ObjectIdentity('1.3.6.1.2.1.69.1.3.7.0'))):                      
            if errorIndication or errorStatus:
                print(errorIndication or errorStatus)
                break
            else:
                for varBind in varBinds:
                        print(varBind)

def setSNMP1(C,k):
        t1 = time.time()
        for (errorIndication,
             errorStatus,
             errorIndex,
             varBinds) in setCmd(SnmpEngine(),
                CommunityData('public'),
                UdpTransportTarget((C, 161)),
                ContextData(),        
                ObjectType(ObjectIdentity('1.3.6.1.2.1.69.1.3.2.0'), OctetString("AB01.01.009.06_022819_183.0A.NSH.MAC14.NA.img")),                
                ObjectType(ObjectIdentity('1.3.6.1.2.1.69.1.3.8.0'), Integer32(2)),                
                ObjectType(ObjectIdentity('1.3.6.1.2.1.69.1.3.3.0'), Integer32(1))):                
            if errorIndication or errorStatus:
               pass


def getAdminStatus(C,k):
        for (errorIndication,
             errorStatus,
             errorIndex,
             varBinds) in getCmd(SnmpEngine(),
                CommunityData('public'),
                UdpTransportTarget((C, 161)),
                ContextData(),              
                ObjectType(ObjectIdentity('1.3.6.1.2.1.69.1.3.4.0'))):
                        
            if errorIndication or errorStatus:
                print(errorIndication or errorStatus)             
                break
            else:
                for varBind in varBinds:
                        u = str(varBind)
                        file = open("%s\\SW_RAW_DATA.txt"%(FILEPATH),"w")
                        file.write(u)
                        file.close()  
                        with open("%s\\SW_RAW_DATA.txt"%(FILEPATH),"r") as task:
                                for line in task:
                                        try:
                                            if "SNMPv2-SMI::mib-2.69.1.3.4.0 = 4" in line:                    
                                                getErrorReport(C,k)                                                
                                                setSNMP1(C,k)
                                                return (1)
                                            if "SNMPv2-SMI::mib-2.69.1.3.4.0 = 2" in line:                    
                                                return (1)                               
                                            if "SNMPv2-SMI::mib-2.69.1.3.4.0 = 3" in line:                    
                                                return (1)
                                            if "SNMPv2-SMI::mib-2.69.1.3.4.0 = 5" in line:                                                
                                                return (1)                                          
                                        except: r=0


def setSNMP2(C,k):
        t1 = time.time()
        for (errorIndication,
             errorStatus,
             errorIndex,
             varBinds) in setCmd(SnmpEngine(),
                CommunityData('public'),
                UdpTransportTarget((C, 161)),
                ContextData(),        
                ObjectType(ObjectIdentity('1.3.6.1.2.1.69.1.3.2.0'), OctetString("AB01.01.009.06_022819_183.0A.NSH.NA.img")),                
                ObjectType(ObjectIdentity('1.3.6.1.2.1.69.1.3.8.0'), Integer32(2)),                
                ObjectType(ObjectIdentity('1.3.6.1.2.1.69.1.3.3.0'), Integer32(1))):
                
            if errorIndication or errorStatus:
               pass
    
k = 1
m = 0
while k < 601:
    t1 = time.time()
    if getAdminStatus(C,k) == 1:
        if m == 0:
                getSNMP(C,k)
                setSNMP1(C,k)
                getSNMP(C,k)
                #if P == 1:
                #        print("MAC14 S/W DOWNLOAD COUNT : %s "%k)
                o = ("MAC14 S/W DOWNLOAD COUNT : %s "%k)        
                file = open("%s\\SW_DOWNLOAD_OUTPUT.txt"%(FILEPATH),"a")
                file.write("%s\n"%o)
                file.close()
                m = 1
                #k = k+1
    if getAdminStatus(C,k) == 1:
        if m == 1:
                getSNMP(C,k)
                setSNMP2(C,k)
                getSNMP(C,k)
                #if  == 1:
                #        print("NOSH S/W DOWNLOAD COUNT : %s "%k)
                o = ("NOSH S/W DOWNLOAD COUNT : %s "%k)        
                file = open("%s\\SW_DOWNLOAD_OUTPUT.txt"%(FILEPATH),"a")
                file.write("%s\n"%o)
                file.close()
                m = 0
                k = k+1
print("PROCESS COMPLETED PRESS ENTER TO CLOSE THIS WINDOW")
os.remove("%s\\SW_RAW_DATA.txt"%(FILEPATH))
os.system("pause")     
