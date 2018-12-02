from PyQt5.QtWidgets import QTableWidget, QTableWidgetItem, QApplication

app = QApplication([])

tableWidget = QTableWidget()
tableWidget.setRowCount(1)
tableWidget.setColumnCount(3)
tableWidget.insertRow(1)
tableWidget.show()
app.exec_()

