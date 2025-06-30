import random
import sys

from PyQt5.QtWidgets import *
from PyQt5.QtGui import QFont


class NumberGenerator(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Random Number Generator")
        self.setGeometry(200, 200, 900, 600)

        """Generate random number between 0-100"""
        self.button = QPushButton("Generate", self)
        self.button.setFont(QFont("Arial", 28))
        self.button.setGeometry(self.size().width() // 2 - 300 // 2, self.size().height() // 2 - 80, 300, 80)
        self.button.clicked.connect(self.generate_random_number)

        self.label = QLabel("Random Number: ...", self)
        self.label.setFont(QFont("Arial", 24))
        self.label.setGeometry(self.size().width() // 2 - 400 // 2, self.size().height() // 2, 400, 100)

    def generate_random_number(self):
        number = random.randint(0, 100)
        self.label.setText(f"Random Number: {number}")


def main():
    app = QApplication(sys.argv)
    win = NumberGenerator()
    # win.showMaximized()
    win.show()
    app.exec_()


if __name__ == '__main__':
    main()
