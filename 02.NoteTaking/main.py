from PyQt5.QtWidgets import *


class MyWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Note Taking App")
        self.setGeometry(200, 200, 800, 600)

        self.text_edit = QTextEdit()
        self.setCentralWidget(self.text_edit)

        self.current_file = None

        self.create_menu()
        self.statusBar().showMessage("Ready")

    def create_menu(self):
        menu_bar = self.menuBar()

        file_menu: QMenu = menu_bar.addMenu("File")

        new_action = QAction("New", self)
        new_action.triggered.connect(self.new_file)
        file_menu.addAction(new_action)

        open_action = QAction("Open", self)
        open_action.triggered.connect(self.open_file)
        file_menu.addAction(open_action)

        save_action = QAction("Save", self)
        save_action.triggered.connect(self.save_file)
        file_menu.addAction(save_action)

        exit_action = QAction("Exit", self)
        exit_action.triggered.connect(self.close)
        file_menu.addAction(exit_action)

    def new_file(self):
        self.text_edit.setPlainText("")
        self.current_file = None
        self.statusBar().showMessage("New file")

    def open_file(self):
        file_path, _ = QFileDialog.getOpenFileName(self, "Open File")

        if file_path:
            with open(file_path, "r") as f:
                content = f.read()
                self.text_edit.setPlainText(content)
                self.current_file = file_path
                self.statusBar().showMessage("Open file")

    def save_file(self):
        if not self.current_file:
            file_path, _ = QFileDialog.getSaveFileName(self, "Save File", "Text Files (*.txt")
            if not file_path:
                return
            self.current_file = file_path

        with open(self.current_file, "w") as file:
            file.write(self.text_edit.toPlainText())
            self.statusBar().showMessage("File Saved!")

    def closeEvent(self, event):
        reply = QMessageBox.question(
            self,
            "Exit",
            "Are you sure you want to quit?",
            QMessageBox.Yes | QMessageBox.No,
            QMessageBox.No
        )

        if reply == QMessageBox.Yes:
            event.accept()
        else:
            event.ignore()


def main():
    app = QApplication([])
    window = MyWindow()
    window.show()
    app.exec_()


if __name__ == '__main__':
    main()
