import sys
from datetime import datetime

from PyQt5.QtWidgets import *
from PyQt5.QtCore import Qt, QTimer


class MyWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        # Window
        self.setWindowTitle("Digital Clock")
        self.setToolTip("Tooltip Clock!")
        self.setWindowOpacity(0.8)
        self.setStyleSheet(f"""
            background: #333;
            color: white;
        """)
        self.setGeometry(500, 200, 900, 700)

        # Label
        self.label = QLabel()
        self.label.setStyleSheet(f"""
            font-size: 48px;
            font-weight: bold;
        """)
        self.label.setAlignment(Qt.AlignCenter)
        self.setCentralWidget(self.label)
        self.update_label()

        # Timer
        self.timer = QTimer()
        self.timer.timeout.connect(self.update_label)
        self.timer.setInterval(1000)
        self.timer.start()

    def update_label(self):
        now = datetime.now()
        hour = now.hour
        minute = now.minute
        second = now.second
        self.label.setText(f"{hour}:{minute}:{second}")


def main():
    app = QApplication(sys.argv)
    window = MyWindow()
    window.show()
    app.exec_()


if __name__ == '__main__':
    main()
