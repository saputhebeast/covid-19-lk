import requests
from prettytable import PrettyTable
import os
import webbrowser

api = "https://www.hpb.health.gov.lk/api/get-current-statistical"
json_data = (requests.get(api).json())['data']['hospital_data']

def PrettyTablePrint():
    hospitalDataTable = PrettyTable()
    hospitalDataTable.field_names = ["Hospital Name", "In Treatment", "Cimulative Treated"]

    hospitalDataTable.align["Hospital Name"] = "l"
    hospitalDataTable.align["In Treatment"] = "l"
    hospitalDataTable.align["Cimulative Treated"] = "l"

    for i in range(len(json_data)):
        hospitalDataTable.add_row([json_data[i]['hospital']['name'], json_data[i]['treatment_total'], json_data[i]['cumulative_total']])
    hospitalDataTable.sortby = ('Cimulative Treated')
    htmlBody = hospitalDataTable.get_html_string(attributes={"class":"data_table"})

    htmlHeader = """<html>\n<head>\n\t<title>Covid19 Hospital Records</title>\n\t<link rel="stylesheet" href="main.css">\n<head>\n<body>\n"""
    htmlFooter = """\n</body>\n</html>"""

    htmlCode = htmlHeader + htmlBody + htmlFooter

    with open("./Data/hospitalData.html", "w") as writter:
        writter.write(htmlCode)

def openInChrome():
    chrome_path = 'C:/Program Files/Google/Chrome/Application/chrome.exe %s'
    PrettyTablePrint()
    filename = 'file:///'+os.getcwd()+'/' + './data/hospitalData.html'
    webbrowser.get(chrome_path).open_new_tab(filename)
