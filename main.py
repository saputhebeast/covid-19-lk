from tkinter import *
from tkinter.font import BOLD
import packages.latestUpdates
import packages.graphs
import packages.pcrTesting
import packages.hospitalData

root = Tk()
root.iconbitmap(default="./data/sri_lanka_flag.ico")
root.geometry("830x930")
root.title("Corona Tracking App")
root.configure(background='black')

heading = Label(root, font = ('Calibri', 34, BOLD), text="Covid19 Tracking App", bg="black", fg="red")
heading.pack(pady=20)

reloadData = Button(root, font=('Calibri', 18), text="Reload", command=packages.latestUpdates.getCasesData, bg="black", fg="white")
reloadData.pack(pady= 8)

virusData = Label(root, font = ('Calibri', 26), text=packages.latestUpdates.getCasesData(), bg="black", fg="white")
virusData.pack(pady=20)

confirmGraph = Button(root, font=('Calibri', 18), text="Total Cases", command=packages.graphs.confirmedCases, bg="#DC143C", fg = "white")
confirmGraph.pack(pady= 8)

recoveredGraph = Button(root, font=('Calibri', 18), text="Recovered", command=packages.graphs.recovered, bg="#32CD32", fg = "white")
recoveredGraph.pack(pady=8)

pcrGraph = Button(root, font=('Calibri', 18), text="Daily PCR Tests", command=packages.pcrTesting.pcrTesting, bg="#1E90FF", fg = "white")
pcrGraph.pack(pady=8)

hospitalRecords = Button(root, font=('Calibri', 18), text="Hospital Records", command=packages.hospitalData.openInChrome, bg="#FF4500", fg = "white")
hospitalRecords.pack(pady=8)

root.mainloop()