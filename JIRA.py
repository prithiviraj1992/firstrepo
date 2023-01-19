#==========================================================================
# Copyright 2020, ARRIS Group, Inc., All rights reserved.
#==========================================================================
####################################################################
# Test Suite Name:      JIRA_CLM_CRITICAL_BLOCKER_PD_QUERY
# Author:               Prithiviraj sundarasamy
# Purpose:
#   The purpose of this tool is to send the Blocker and Critical PD's
#####################################################################

#=========================================== REQUIRED MODULE IMPORTING ============================================================
import os
import sys
import time
import jira
import smtplib
import datetime
from  jira.client import JIRA
from selenium import webdriver
from email.mime.text import MIMEText
from datetime import datetime, timedelta
from selenium.webdriver.common.by import By
from email.mime.multipart import MIMEMultipart
from selenium.webdriver.support.ui import WebDriverWait
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.support import expected_conditions as EC
import xlsxwriter

#===========================================   CLM & JIRA CREDENTIALS ============================================================
username = 'psundarasamy'
password = 'xxxxx'

# Storage path to store the report in HTML format
Storage_path = "C:\\DOC_SCRIPT\\CRITICAL_BLOCKER\\HCDTS\\"

#===========================================     CLM & JIRA VARIABLE LIST   ============================================================
Count_flag = 0
PD_flag = 0
CLM_ID =[]
CLM_Summary=[]
Result_CLM_FOUND_LOAD=[]
CLM_Severity=[]
CLM_hardware=[]
PD_NOT_AVAILABLE = 0
JIRA_ID =[]
JIRA_Summary=[]
JIRA_versions=[]
JIRA_Hardware=[]
JIRA_Severity=[]

#===========================================  FAILURE E-MAIL NOTIFICATION  ============================================================
def SCRIPT_FAILURE(REASON):    
    FROM_ADDR = "prithviraj.sundarasamy@commscope.com"
    TO_ADDR = ['prithviraj.sundarasamy@commscope.com','s.prithivraj@gmail.com']    
    MSG = MIMEMultipart()
    MSG['From'] = FROM_ADDR
    MSG['To'] = ', '.join(TO_ADDR)
    MSG['Subject'] = "!!!!!!!!!! I-HCDTS Critical Blocker PD's Script failure due to %s !!!!!!!!!!!!!!!"%(REASON)
    Script_result = "\n\n\nTODAY I-HCDTS PD ANALYSIS SCRIPT GOT STOPPED DUE TO %s."%(REASON)
    mail_body = Script_result+"\n\n\n This is an auto-generated mail. Please do not reply to this message."
    MSG.attach(MIMEText(mail_body, 'plain'))
    try:
        print("trying to establish connection..")
        server = smtplib.SMTP('smtp.commscope.com', timeout=120)
        server.ehlo()
        text = MSG.as_string()
        server.sendmail(FROM_ADDR, TO_ADDR, text)
        server.quit()
        print( "Successfully sent email")
    except:
        print ("Error: unable to send email")     
    sys.exit()       

#===========================================     CLM LOGIN   ============================================================

try:
    options = webdriver.ChromeOptions()
    options.add_argument("headless")
    LOGIN_BUTTON_XPATH = '//*[@id="jazz_app_internal_LoginWidget_0"]/div[1]/div[1]/div[3]/form/button'
    browser = webdriver.Chrome('C:\\Users\\general\\AppData\\Local\\Programs\\Python\\Python35-32\\selenium\\webdriver\\chrome\\chromedriver.exe', chrome_options=options)
    browser.get("https://clm.arrisi.com/ccm/web/projects/ARRIS%20DOCSIS%20CPE%20(CM)#action=com.ibm.team.workitem.runSavedQuery&id=_6XuW1cqZEeuZ7fm7op8KUQ")
    browser.find_element_by_id('jazz_app_internal_LoginWidget_0_userId').send_keys(username)
    browser.find_element_by_id('jazz_app_internal_LoginWidget_0_password').send_keys(password)
    time.sleep(0.3)
    button = browser.find_element_by_xpath(LOGIN_BUTTON_XPATH)
    button.click()
    time.sleep(20)
except:    
    SCRIPT_FAILURE("CLM_FAILED_TO_LOAD")     
        
#===========================================     CLM SMART QUERY   ============================================================
while PD_flag == 0 : 
    if (browser.find_elements_by_css_selector("tr.visibleRow") != None):               
        PD_flag = 1         
    for row in browser.find_elements_by_css_selector("tr.visibleRow"):        
        try:            
            ID = row.find_elements_by_tag_name("td")[2] 
            Summary = row.find_elements_by_tag_name("td")[3]
            try:
                CLM_FOUND_LOAD = row.find_elements_by_tag_name("td")[11]
            except:
                CLM_FOUND_LOAD = "NOT AVAILABLE"
            severity = row.find_elements_by_tag_name("td")[7]   
            try:
                Hardware = row.find_elements_by_tag_name("td")[12] 
            except:  
                Hardware = "NOT AVAILABLE"              
            Remove_clone = (Summary.text.encode("utf-8"))               
            Remove_clone = Remove_clone[0:5]
            Remove_copy = (Summary.text.encode("utf-8"))               
            Remove_copy = Remove_copy[0:4]            
            if Remove_clone != b'Clone' and Remove_clone != b'clone' and Remove_clone != b'CLONE' and Remove_copy != b'Copy' and Remove_copy != b'COPY' and Remove_copy != b'copy':                                             
                CLM_ID.append(ID.text)               
                CLM_Summary.append(Summary.text.encode("utf-8"))                       
                Result_CLM_FOUND_LOAD.append(CLM_FOUND_LOAD.text)
                CLM_Severity.append(severity.text)                                     
                CLM_hardware.append(Hardware.text)                            
                if CLM_ID[0] == CLM_ID[Count_flag]:
                    PD_flag = 1 
                Count_flag = Count_flag+1                                  
        except:
            SCRIPT_FAILURE("CLM_PASSWORD_EXPIRED")            

#===========================================     CLM NO PD FLAG   ============================================================
if len(CLM_ID) == 0:    
    PD_NOT_AVAILABLE = 1        

#===========================================     KILLING BROWSER SESSION   ============================================================
browser.quit()

#===========================================     JIRA LOGIN   ============================================================

jira_path   = 'https://odart.arrisi.com/'
servername = {'server':jira_path}

try:
  jira    = JIRA(basic_auth=(username, password), options=servername)
except:
  print ("Not able to open Jira. Please enter correct username and password and try again.")  
  SCRIPT_FAILURE("JIRA_PASSWORD_EXPIRED")

#===========================================     JIRA SMART QUERY   ============================================================
today = (datetime.now()).strftime("%Y/%m/%d %H:%M")
yesterday = (datetime.now() + timedelta(days=-1)).strftime("%Y/%m/%d %H:%M")
JIRA_smart_query = r' project != "DAD (DATE Automation Development)" AND summary ~ "\"[I-HCDTS]\"" AND resolution in (Unresolved, New, Pending, "Ready to Test", "In Progress", "In Review", "On Hold", "Work Complete", "To Be Fixed", "To Be Deferred", "Partially Verified", "Fixed Upstream", "Unreproducible", "Unresolved" , "Verified") AND Severity in (0-Blocker, 1-Critical)'
try:
    for issue in jira.search_issues(JIRA_smart_query):
        Remove_clone = issue.fields.summary.encode("utf-8")               
        Remove_clone = Remove_clone[0:5]
        Remove_copy = issue.fields.summary.encode("utf-8")              
        Remove_copy = Remove_copy[0:4]        
        if Remove_clone != b'Clone' and Remove_clone != b'clone' and Remove_clone != b'CLONE' and Remove_copy != b'Copy' and Remove_copy != b'COPY' and Remove_copy != b'copy':              
            JIRA_ID.append(issue.key)
            JIRA_Summary.append(issue.fields.summary.encode("utf-8"))  
            try: 
                JIRA_versions_data = (issue.fields.versions)
                JIRA_versions_data = list(JIRA_versions_data)
                JIRA_versions_data = JIRA_versions_data[0]
                JIRA_versions.append(JIRA_versions_data) 
            except:
                JIRA_versions.append("NOT AVAILABLE")
            try:            
                JIRA_Hardware_data = (issue.fields.customfield_10081)    
                JIRA_Hardware_data = list(JIRA_Hardware_data)    
                JIRA_Hardware_data = JIRA_Hardware_data[0]   
                JIRA_Hardware.append(JIRA_Hardware_data)
            except:           
                JIRA_Hardware.append("NOT AVAILABLE") 
            JIRA_Severity_data = (issue.fields.customfield_10032)
            JIRA_Severity_data = str(JIRA_Severity_data)
            JIRA_Severity_data = JIRA_Severity_data.split("-")
            JIRA_Severity_data = JIRA_Severity_data[1]   
            JIRA_Severity.append(JIRA_Severity_data)  
except:   
    SCRIPT_FAILURE("JIRA_FAILED_TO_LOAD")    
    pass

#===========================================     JIRA NO PD FLAG   ============================================================
if len(JIRA_ID) == 0:
    PD_NOT_AVAILABLE = PD_NOT_AVAILABLE + 1

#===========================================     CONVERT LIST TO INITEGER ============================================================
def convert(list):            
    s = [str(i) for i in list]           
    res = int("".join(s))       
    return(res) 
#===========================================     HTML DATA CREATION FUNCTION ============================================================

workbook = xlsxwriter.Workbook(r'C:\Users\general\Desktop\pds.xlsx')
worksheet = workbook.add_worksheet()

def Top_ten(A,B,C,D,E,loop_count):
    worksheet.write('A%s'%(loop_count), A)
    worksheet.write('B%s'%(loop_count), B)
    worksheet.write('C%s'%(loop_count), C)
    worksheet.write('D%s'%(loop_count), D)
    worksheet.write('E%s'%(loop_count), E)

#===========================================     HTML REPORT CREATION   ============================================================
suffix = (datetime.now()).strftime("%Y%m%d")
loop_count = 1
for pd_list in range (len(CLM_ID)):    
    Top_ten(str(CLM_ID[pd_list]),str(CLM_Summary[pd_list].decode("utf-8")),str(CLM_Severity[pd_list]),str(Result_CLM_FOUND_LOAD[pd_list]),str(CLM_hardware[pd_list]),loop_count)            
    loop_count = loop_count + 1
for JIRA_list in range (len(JIRA_ID)):
    Top_ten(JIRA_ID[JIRA_list],JIRA_Summary[JIRA_list].decode("utf-8"),str(JIRA_Severity[JIRA_list]),str(JIRA_versions[JIRA_list]),str(JIRA_Hardware[JIRA_list]),loop_count)                                                              
    loop_count = loop_count + 1
workbook.close()

# subprocess.run(["scp", FILE, "root@10.237.131.112:/home/httpd/html/ihcdts/assests/jira/"])
#e.g. subprocess.run(["scp", "foo.bar", "joe@srvr.net:/path/to/foo.bar"])

# os.system('sshpass -p "root" scp root@10.237.131.112:/home/httpd/html/ihcdts/assests/jira/hello.xlsx')


'''
#===========================================  FINAL E-MAIL HEADER AND SUBJECT  ============================================================
HEADER_DATE = (datetime.now()).strftime("%m-%d-%Y")
# e-mail portion to forward the date to all
# FROM_ADDR = "prithviraj.sundarasamy@commscope.com"
# TO_ADDR = ['geetha.alex@commscope.com', 'vijaya.devarasetti@commscope.com', 'chandru.gouda@commscope.com', 'manju.joseph@commscope.com', 'archana.krishnamurthy@commscope.com', 'niranjan.kumar2@commscope.com', 'rajesh.kumar3@commscope.com', 'rinoob.kurian@commscope.com', 'shankar.manurwar@commscope.com', 'amsaveni.murugan@commscope.com', 'deepak.nagendran@commscope.com', 'santosh.pattar@commscope.com', 'l.shakuntala@commscope.com', 'madhulika.singh@commscope.com', 'virendra.singh2@commscope.com', 'sanjayy.sreedhara@commscope.com', 'GraceDiana.Stephen@commscope.com', 'prithviraj.sundarasamy@commscope.com', 'dilip.vasudevan@commscope.com']
#TO_ADDR = ['prithviraj.sundarasamy@commscope.com', 'shankar.manurwar@commscope.com','rinoob.kurian@commscope.com', 'vijaya.devarasetti@commscope.com', 'sanjayy.sreedhara@commscope.com', 'manju.joseph@commscope.com']
#TO_ADDR = ['prithviraj.sundarasamy@commscope.com','s.prithivraj@gmail.com']
MSG = MIMEMultipart()
MSG['From'] = FROM_ADDR
MSG['To'] = ', '.join(TO_ADDR)
MSG['Subject'] = "BRCM Critical/Blocker PDs reported on (%s)"%(HEADER_DATE)

#===========================================  WEEKDAY CALCULATION  ============================================================
datetime.today().strftime('%A')
week = datetime.today().strftime('%A')

if week == "Sunday" or week == "Saturday":
    week_day_flag = 1
else:
    week_day_flag = 0

#===========================================  FINAL E-MAIL PORTION  ============================================================
if PD_NOT_AVAILABLE < 2:
    with open ('%sReport_%s.html'%(Storage_path,suffix),'r') as task:
        Mail_data =task.read()
    mail_body = Mail_data           
    MSG.attach(MIMEText(mail_body, 'html'))

else:
    mail_body = "Hi All\n\n\t There is no Critical/Blocker PDs reported by QA on (%s)\n\nRegards,\nBLR-QA"%(HEADER_DATE)
    MSG.attach(MIMEText(mail_body, 'plain'))

#if ((week_day_flag == 0 and PD_NOT_AVAILABLE >= 2) or PD_NOT_AVAILABLE < 2):
if (PD_NOT_AVAILABLE < 2):
    try:
        print("trying to establish connection..")
        server = smtplib.SMTP('smtp.commscope.com', timeout=120)
        server.ehlo()
        text = MSG.as_string()    
        server.sendmail(FROM_ADDR, TO_ADDR, text)
        server.quit()
        print( "Successfully sent email")
    except:
        print ("Error: unable to send email")
else:
    pass
'''
