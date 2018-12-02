from PyQt5.QtWidgets import QTableWidget, QTableWidgetItem, QApplication
import sqlite3
from dbfunctions import *




app = QApplication([])

def getData():
    connection = sqlite3.connect('tracker.db')
    c = connection.cursor()
    data = GetTransByDateInterval(c, '2018-11-00', '2018-11-32')

def testTable():
    tableWidget = QTableWidget()
    tableWidget.setRowCount(0)
    tableWidget.setColumnCount(5)
    getData()
    for row_number, row_data in enumerate(data):
        tableWidget.insertRow(row_number)
        for column_number, column_data in enumerate(row_data):
            tableWidget.setItem(row_number, column_number, QTableWidgetItem(str(column_data)))

connection.close()


tableWidget.show()
app.exec_()
