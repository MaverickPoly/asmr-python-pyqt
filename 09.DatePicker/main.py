import sys

from PyQt5.QtWidgets import *
from PyQt5.QtCore import Qt, QDate



class DatePicker(QWidget):
    def __init__(self):
        super().__init__()

        # Window
        self.setWindowTitle("Date Picker")

        # UI
        layout = QVBoxLayout()

        calendar = QCalendarWidget()
        calendar.setGridVisible(True)
        calendar.clicked.connect(self.date_selected)

        time_edit = QTimeEdit()

        self.label = QLabel("Selected Date: None")
        self.label.setStyleSheet("""
            font-size: 24px;
        """)
        self.label.setAlignment(Qt.AlignCenter)

        layout.addWidget(calendar)
        layout.addWidget(time_edit)
        layout.addWidget(self.label)

        self.setLayout(layout)

    def date_selected(self, date: QDate):
        self.label.setText(f"Selected Date: {date.toString('dd MMMM yyyy')}")


def main():
    application = QApplication(sys.argv)
    date_picker = DatePicker()
    # date_picker.showMaximized()
    date_picker.show()
    application.exec_()


if __name__ == '__main__':
    main()
