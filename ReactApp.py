import requests
import json
import xlrd
from xlutils.copy import copy
from time import sleep

Domain_URL = "https://staging-jio.reverieinc.com/get_kgqa"
Input_File_Path = "C://Users//Reverie-PC//PycharmProjects//ReactAppAutomation//React_App_Test_Case.xls"
Work_Book_1 = xlrd.open_workbook(Input_File_Path)
sheet_indexing = Work_Book_1.sheet_by_index(0)
Input_Parameter = sheet_indexing.col_values(0)

Work_book_2 = copy(Work_Book_1)
get_sheet = Work_book_2.get_sheet(0)

for i in range(len(Input_Parameter)):

    payload = json.dumps({
        "query": Input_Parameter[i],
        "top_k": 10,
        "lang": "bn",
        "backend": "hybrid"
    })

    headers = {
        'Content-Type': 'application/json'
    }

    try:
        response = requests.request("POST", Domain_URL, headers=headers, data=payload)
        json_response = response.json()
        React_ID = json_response[0]['Id']
        get_sheet.write(i, 1, "Pass")
        sleep(.3)
        print(React_ID)

    except:
        get_sheet.write(i, 1, "Fail")
        pass

Work_book_2.save(Input_File_Path)



