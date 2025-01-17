#!/usr/bin/python3

import sys
import os
from PyQt5.QtWidgets import QApplication, QTableView, QAbstractTableModel, QVariant, QFileSystemModel, QHeaderView, QStyledItemDelegate, QWidget, QPushButton, QFileInfo
from PyQt5.QtCore import Qt, QModelIndex, QSortFilterProxyModel

def getxattr(path, name):
    if not os.path.exists(path):
        return []
    try:
        return [(name, getxattr(path, name)]
    except:
        return []

def setxattr(path, name, value):
    if not os.path.exists(path):
        return
    subprocess.check_call(["setfattr", "-n", name, "-v", value, path])

class ExtendedFileSystemModel(QAbstractTableModel):
    def __init__(self, directory, parent=None):
        super().__init__(parent)
        self.directory = directory
        self.file_system_model = QFileSystemModel()
        self.file_system_model.setRootPath(directory)
        self.file_system_model.setFilter(QDir.NoDotAndDotDot | QDir.Files | QDir.Readable)
        self.xattrs_model = XAttrModel(self.file_system_model, self.directory)

    def rowCount(self, parent=QModelIndex()):
        return self.xattrs_model.rowCount(parent)

    def columnCount(self, parent=QModelIndex()):
        return self.xattrs_model.columnCount(parent)

    def data(self, index, role=Qt.DisplayRole):
        if role == Qt.DisplayRole:
            return self.xattrs_model.data(index, role)
        return QVariant()

    def setData(self, index, value, role=Qt.EditRole):
        if role == Qt.EditRole:
            return self.xattrs_model.setData(index, value, role)
        return False

    def headerData(self, section, orientation, role=Qt.DisplayRole):
        if role == Qt.DisplayRole and orientation == Qt.Horizontal:
            if section == 0:
                return "Key"
            elif section == 1:
                return "Value"
        return QVariant()

class XAttrModel(QAbstractTableModel):
    def __init__(self, file_system_model, directory, parent=None):
        super().__init__(parent)
        self.file_system_model = file_system_model
        self.directory = directory
        self.xattrs = {}
        self.load_xattrs()

    def rowCount(self, parent=QModelIndex()):
        return len(self.xattrs)

    def columnCount(self, parent=QModelIndex()):
        return 2

    def data(self, index, role=Qt.DisplayRole):
        if role == Qt.DisplayRole:
            key, value = self.xattrs.items()[index.row()]
            if index.column() == 0:
                return key
            elif index.column() == 1:
                return value
        return QVariant()

    def setData(self, index, value, role=Qt.EditRole):
        if role == Qt.EditRole:
            key, value = self.xattrs.items()[index.row()]
            self.xattrs[key] = value
            self.dataChanged.emit(index, index, [Qt.DisplayRole])
            self.save_xattrs()
            return True
        return False

    def load_xattrs(self):
        for file_info in self.file_system_model.entries(self.directory):
            if file_info.isFile():
                xattrs = getxattr(os.path.join(self.directory, file_info.fileName()), "user.*")
                for xattr in xattrs:
                    key, value = xattr
                    self.xattrs[key] = value

    def save_xattrs(self):
        for key, value in self.xattrs.items

