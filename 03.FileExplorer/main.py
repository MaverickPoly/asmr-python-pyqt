import os.path
import sys

from PyQt5.QtWidgets import *
from PyQt5.QtCore import QDir, QModelIndex, Qt, QUrl
from PyQt5.QtGui import QDesktopServices



class FileExplorer(QWidget):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Simple File Explorer")
        self.setGeometry(300, 100, 1000, 700)

        self.history = ["", "C:/", "C:/Users", "C:/Users/User"]

        layout = QVBoxLayout()
        self.setLayout(layout)

        # Top bar
        top_bar = QHBoxLayout()
        self.back_button = QPushButton("Back")
        self.back_button.clicked.connect(self.go_back)
        self.back_button.setEnabled(True)

        self.path_display = QLineEdit()
        self.path_display.setReadOnly(True)
        self.path_display.setText(self.history[-1])

        top_bar.addWidget(self.back_button)
        top_bar.addWidget(self.path_display)
        layout.addLayout(top_bar)

        self.model = QFileSystemModel()
        self.model.setRootPath(QDir.rootPath())

        self.tree = QTreeView()
        self.tree.setModel(self.model)
        self.tree.setRootIndex(self.model.index(QDir.homePath()))
        self.tree.doubleClicked.connect(self.open_item)
        layout.addWidget(self.tree)

        self.tree.clicked.connect(self.display_path)

    def display_path(self, index: QModelIndex):
        path = self.model.filePath(index)
        self.path_display.setText(path)

    def open_item(self, index: QModelIndex):
        path = self.model.filePath(index)
        if os.path.isfile(path):
            QDesktopServices.openUrl(QUrl.fromLocalFile(path))
        elif os.path.isdir(path):
            current_root = self.model.filePath(self.tree.rootIndex())
            self.history.append(current_root)
            self.back_button.setEnabled(True)

            self.tree.setRootIndex(self.model.index(path))
            self.path_display.setText(path)

            print(self.history)

    def go_back(self):
        if self.history:
            previous_path = self.history.pop()
            self.tree.setRootIndex(self.model.index(previous_path))
            self.path_display.setText(previous_path)
        if not self.history:
            self.back_button.setEnabled(False)




if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = FileExplorer()
    window.show()
    sys.exit(app.exec_())
