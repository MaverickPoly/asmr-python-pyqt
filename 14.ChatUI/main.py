from PyQt5.QtWidgets import *
from PyQt5 import uic


class ChatUi(QMainWindow):
    def __init__(self):
        super().__init__()
        uic.loadUi("chat.ui", self)

        self.sendButton.clicked.connect(self.send_message)

    def send_message(self):
        text: str = self.lineEdit.text().strip()
        if text:
            self.chatListWidget.addItem(f"You: {text}")
            self.lineEdit.clear()
            self.statusBar().showMessage("New Message!")


def main():
    app = QApplication([])
    window = ChatUi()
    window.show()
    app.exec_()


if __name__ == '__main__':
    main()
