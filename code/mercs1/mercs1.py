#!/usr/bin/env python
# This Python file uses the following encoding: utf-8

# MERCS = Metadata? Right-Click-Edit: Save.

import sys
from os import path
from AHAlodeck import AHAlodeck

from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QApplication, QTableWidgetItem
from PyQt5 import uic


class Ui(QtWidgets.QMainWindow):
    def __init__(self):
        super(Ui, self).__init__()          # Call the inherited classes __init__ method
        ui_mainwindow = path.abspath(path.join(path.dirname(__file__), 'mainwindow.ui'))
        uic.loadUi(ui_mainwindow, self)   # Load the .ui file
        self.show()                         # Show the GUI
        aha = AHAlodeck(main_window=self)

        self.metadata = aha.init_parameters()
        self.metadata_utf = aha.BinToUnicode(self.metadata)
        self.aha = aha                      # finally
        self.getContentLength()

        table = self.initTable(self.tableWidget)
        self.initTableData(table, self.metadata_utf)



    def getContentLength(self):
        aha = self.aha

        kv_list = aha.get_values(self.metadata_utf)
        #pprint(kv_list) # DEBUG DELME

        maxWord = {}
        maxWord['key'] = aha.longestWord(kv_list[0])
        maxWord['value'] = aha.longestWord(kv_list[1])
        print("MAX key: {}, value: {}".format(len(maxWord['key']), len(maxWord['value'])))
        self.maxWord = maxWord

    def initTable(self, table):
        table.setColumnCount(3)
        table.setRowCount(len(self.metadata))

        table.setHorizontalHeaderLabels(['Key', 'Value', 'Description'])
        table.setColumnWidth(0, len(self.maxWord['key']) * 7)       # "8" used as random char-width (in px)
        table.setColumnWidth(1, len(self.maxWord['value']) * 7)
        return table

    def initTableData(self, table, metadata):
        row = 0
        for key, value in metadata:
            #print("key: {}, value: {}".format(key, value))
            table.setItem(row, 0, QTableWidgetItem(key))
            table.setItem(row, 1, QTableWidgetItem(value))
            row += 1


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = Ui()
    sys.exit(app.exec_())
