"""
************************************************************************************************************************
************************************************************************************************************************
author: Rinoob Kurian
email:  Rinoob.Kurian@arris.com
date: 11/May/2018

This script is used to convert CLM TP in pdf format to xls format

*************************************************** Usage **************************************************************
1.Install latest version of python
2.Install the modules PyPDF2,xlrd,xlwt and xlutils
3.Export TP (with Details) from CLM in PDF format and save it in a local folder
4.Open and edit the script in notepad/WordPad:  Change the PDF_FILE_NAME name accordingly to match with your saved PDF file name and folder path
5.Run the script
6.O/p will be created in the same folder where you keep the PDF file 

************************************************************************************************************************
************************************************************************************************************************

"""

import xlrd
import os
import xlwt
from xlutils.copy import copy
import glob
import PyPDF2
import sys

"""
DEFINE CONSTANTS
"""

#Define i/p pdf file name with Test Scripts exported from CLM 
PDF_FILE_NAME = r"C:\Users\general\Desktop\pdf2excel\22705 - [Library] - CR 40 Mercury v2 EOS Wake On Lan TP.pdf"
#define the xls column headings
XLS_COLUMN_HEADINGS=["ID","Test Case ID","Test Case Head Line","Test Steps and Expected Result"]
#Define PDF test scripts columns
PDF_TEST_SCRIPTS_COLUMNS=["ID", "Name", "State", "Script Type", "Owner", "Data Records", "Modified", "Validates Requirement"]



def createOutputXlsFile(PdfFileFullName):
    return PdfFileFullName[:-3] + 'xls' if PdfFileFullName.endswith('pdf') else print("Error..!! Unable to create xls file.")

def getOutputFile(outputFileName):
    if os.path.isfile(outputFileName):
        workbook2 = xlrd.open_workbook(outputFileName, formatting_info=True)
        print('\n\n File already exists,aborting the execution.Please delete the file and restart again..!!!\n')
        sys.exit(0)

	          
    else:
        # print('New File created')
        workbook2 = xlwt.Workbook()
        ws = workbook2.add_sheet('TestPlan')

        font = xlwt.Font()
        font.bold = True
        style = xlwt.XFStyle()
        style.font = font
        numberOfColumnsInXls=len(XLS_COLUMN_HEADINGS)
        currentColumnNumber=0
        while currentColumnNumber<numberOfColumnsInXls:
            column_width=len(XLS_COLUMN_HEADINGS[currentColumnNumber])
            ws.write(0, currentColumnNumber, XLS_COLUMN_HEADINGS[currentColumnNumber], style)
            current_col = ws.col(currentColumnNumber)
            current_col.width = 256 * (column_width+10)
            currentColumnNumber+= 1
        row_height = xlwt.easyxf('font:height 720;')
        first_row = ws.row(0)
        first_row.set_style(row_height)
        workbook2.save(outputFileName)



def readTestScriptsWriteToFile(outputFileName,PdfFileName):
    # open the pdf to read
    pdfFileShort = open(PdfFileName, 'rb')
    read_pdf = PyPDF2.PdfFileReader(pdfFileShort)
    number_of_pages = read_pdf.getNumPages()
    print("Number of pages in PDF file --> ",pdfFileShort, ": ", number_of_pages)

    # find the Test Scripts page number
    current_page_number = 0
    pageNumberFound = False
    while current_page_number < number_of_pages and pageNumberFound == False:
        page = read_pdf.getPage(current_page_number)
        current_page_number = current_page_number + 1
        page_content = page.extractText()

        for page_content_line_content in page_content.splitlines():
            if page_content_line_content == "Test Scripts":
                pageNumberFound = True
                testScriptsPageNumber = current_page_number
                print("Test Scripts page number: ", testScriptsPageNumber)
                break

    # find the Test Case Execution Records page number
    current_page_number = 0
    while current_page_number < number_of_pages:
        page = read_pdf.getPage(current_page_number)
        current_page_number = current_page_number + 1
        page_content = page.extractText()
        pageNumberFound = False

        for page_content_line_content in page_content.splitlines():
            if page_content_line_content == "Test Case Execution Records":
                pageNumberFound = True
                testCaseExecutionRecordsPageNumber = current_page_number
                print("Test Case Execution Records Page Number:", testCaseExecutionRecordsPageNumber)
                break

    # Copy the ID and name of the test cases to excel
    current_page_number = testScriptsPageNumber - 1
    columnNumber = 0
    test_scripts_text_found = False

    while current_page_number < testCaseExecutionRecordsPageNumber:
        page = read_pdf.getPage(current_page_number)
        current_page_number = current_page_number + 1
        validates_requirement_text_found = False
        counter = 0
        previous_first_column_counter = 0
        previous_second_column_counter = 1
        debug_printed=False
        page_content = page.extractText()

        for page_content_line_content in page_content.splitlines():

            # get the data to enter
            if current_page_number == testScriptsPageNumber:
              if page_content_line_content == "Test Scripts":
                test_scripts_text_found = True
                continue
            if not (test_scripts_text_found):
                continue

            if page_content_line_content == "Validates Requirement":
                validates_requirement_text_found = True
                continue
            if not (validates_requirement_text_found):
                continue
            if "https://clm.arrisi.com" in page_content_line_content:
                continue
            if ".xml" in page_content_line_content:
                continue

            # initialize the counter logic to get only the ID
            counter =counter+ 1
            if counter==1:
                previous_first_column_counter=1
                
            if counter==2:
                 previous_second_column_counter=2

            if (counter-previous_first_column_counter==8):
                previous_first_column_counter = counter
                
            if (counter - previous_second_column_counter == 8):
                previous_second_column_counter = counter
            # to avoid counter increment when multiple lines in single column happens. Observed with Name and Status combinations
            if (counter - previous_second_column_counter == 1 and page_content_line_content != "Draft"):
                    counter = counter - 1
                    continue

            if (counter!=1 and counter-previous_first_column_counter!=0 ):
                continue

            if current_page_number == testCaseExecutionRecordsPageNumber:
                if page_content_line_content == "Test Case Execution Records":
                    break

            workbook = xlrd.open_workbook(outputFileName, formatting_info=True)
            sheetName = workbook.sheet_by_name('TestPlan')
            lastRowToHaveData = sheetName.nrows
            wb = copy(workbook)
            sheetToWrite = wb.get_sheet('TestPlan')
            style = xlwt.XFStyle()
            style.alignment.wrap = 1
            font = xlwt.Font()
            font.bold = False
            style.font = font
            rowNumberToStart = lastRowToHaveData
            print("Writing row:  ",rowNumberToStart,"in xls with data: ",page_content_line_content)
            sheetToWrite.write(rowNumberToStart, 0, page_content_line_content, style)
           
            wb.save(outputFileName)


def readFullPdfWriteToFile(outputFileName,PdfFileName):
    # find the test case page number
    # open the output.xls and read the test case number and then find the page number
    workbook = xlrd.open_workbook(outputFileName, formatting_info=True)
    sheetName = workbook.sheet_by_name('TestPlan')
    lastRowHaveData = sheetName.nrows
    wb = copy(workbook)
    sheetToWrite = wb.get_sheet('TestPlan')
    style = xlwt.XFStyle()
    style.alignment.wrap = 1
    font = xlwt.Font()
    font.bold = False
    style.font = font
    current_row_number = 1
    while current_row_number<lastRowHaveData:
        row_values = sheetName.row_values(current_row_number)
        currentTestCaseID = row_values[0]
        # add a : to get the exact test case ID in pdf page
        currentTestCaseID = currentTestCaseID + ":"
        print("**********************************************************\n")
        print("Fetching details for the Test Case ID : ", row_values[0])
        print("\n**********************************************************\n")
       
        pdfFileFull = open(PdfFileName, 'rb')
        read_pdf = PyPDF2.PdfFileReader(pdfFileFull)
        number_of_pages = read_pdf.getNumPages()
        print("Number of pages in PDF file --> ",PdfFileName, ": ", number_of_pages)
        current_page_number = 0
        while current_page_number < number_of_pages:
            page = read_pdf.getPage(current_page_number)
            current_page_number = current_page_number + 1
            page_content = page.extractText()
            pageNumberFound = False
            for page_content_line_content in page_content.splitlines():
                if (currentTestCaseID in page_content_line_content):
                    pageNumberFound = True
                    testCasePageNumber = current_page_number
                    print("Test Case Page Number for test case ID ",currentTestCaseID," --> ", testCasePageNumber)
                    print("------------------------------------------------------------------")
                    break

        # read the contents
        pdfFileFull = open(PdfFileName, 'rb')
        read_pdf = PyPDF2.PdfFileReader(pdfFileFull)
        full_page_content = []
        manual_steps_text_found = False
        description_text_count=0
        test_case_name_counter=0

        # read the pages until 'Associated E-Signatures' line appears
        manual_steps_reading_completed = False
        while manual_steps_reading_completed != True:
            page = read_pdf.getPage(testCasePageNumber - 1)
            page_content = page.extractText()
            for page_content_line_content in page_content.splitlines():
                if(test_case_name_counter==1):
                    testCaseName = page_content_line_content.replace(currentTestCaseID,'')
                    print("Priniting page line contents: \n", page_content_line_content,"line number: ", test_case_name_counter)

                test_case_name_counter += 1
                #get the description
                if ("Description:" in page_content_line_content):
                    description_text_count+= 1
                if ("Manual Steps" in page_content_line_content):
                    manual_steps_text_found = True
                if ("Associated E-Signatures" in page_content_line_content):
                    manual_steps_reading_completed = True
                    break
                else:
                    if (manual_steps_text_found):
                        if not ("https://clm.arrisi.com" in page_content_line_content):
                            full_page_content.append("\n")
                            full_page_content.append(page_content_line_content)
                    if(description_text_count==1):
                        if not("Description:" in page_content_line_content):
                            testCaseDescription=page_content_line_content
                            description_text_count += 1
            testCasePageNumber += 1
        print("\n\nTest Case Headline: ", testCaseDescription)
        print("\n\nTest Case Details: \n", full_page_content)
        print("\nEnd of test case. Writing to xls...")
        print("------------------------------------------------------------------")
        print("\nTest Cases Completed: ",current_row_number,", Test Cases Remaining: ",lastRowHaveData-current_row_number)
        sheetToWrite.write(current_row_number, 1, testCaseName, style)
        sheetToWrite.write(current_row_number, 2, testCaseDescription, style)
        sheetToWrite.write(current_row_number, 3, full_page_content, style)
        current_row_number += 1
    wb.save(outputFileName)

OUTPUT_FILE_NAME= createOutputXlsFile(PDF_FILE_NAME)
print("Output Filename : ",OUTPUT_FILE_NAME)
getOutputFile(OUTPUT_FILE_NAME)
readTestScriptsWriteToFile(OUTPUT_FILE_NAME,PDF_FILE_NAME)
# Read the OUTPUT_FILE.xls and find the corresponding test case from PDF file and write test steps and other info in OUTPUT_FILE.xls
readFullPdfWriteToFile(OUTPUT_FILE_NAME,PDF_FILE_NAME)

print("\n\n**********************************************************\n")
print("PDF to EXCEL conversion completed...!!!")
print("\n**********************************************************\n")
